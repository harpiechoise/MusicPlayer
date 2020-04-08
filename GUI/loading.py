"""This is the loading window frontend."""
from GUI.loading_window import Ui_CargandoWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import os
from pathlib import Path
import mutagen
from backend import dbQuerys as dq
from PyQt5.QtCore import QThread, pyqtSignal


class MusicLoader():
    """
    Scans the path searching music files.

    Methods
    ------
    public load_music()
    ------
    Search all the music file in a given directory
    """

    def __init__(self, path):
        """
        Configure the path, allowed files format
        for scrape all the music files.
        """
        self.path = path
        self.allowed_files = ['.flac', '.mp3', '.wav', '.ogg']

    def load_music(self):
        """Get and filter all the music files."""
        r = []
        # r*.* -> any file with a period song (.) flac
        for path in Path(self.path).rglob(r'*.*'):
            # Return the posix string representation of the path
            strpath = path.absolute().as_posix()
            # split the file in text and extension to filter the files
            # by path
            if os.path.splitext(strpath)[1] in self.allowed_files:
                # if the file is allowed adds to a collection
                r.append(strpath)
        return r


class MetaReader(QThread):
    """
    A PyQt5 Thread to create the songs in the database.

        Properties
        -------------      -----------
       |change_value |    | Signals   |
       |song_name    | -> | to send   |
       |finished     |    | booleans  |
       |             |    | or values |
        -------------      ------------

       change_value: send a value to the progress bar
       song_name: send the song name for info label
       finished: tell to main window if the loading is finished
       TODO: make a state machine for finished values

       Methods
       -------
       get_metadata
        - args
            song: song_file_path
        run
            An internal method from QThread.
            when you call the method start QThread configures the class
            And run the method
    """

    change_value = pyqtSignal(int)
    song_name = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, path):
        """Init of the class."""
        # Instance of the superclass
        super(MetaReader, self).__init__()
        # Music file paths
        self._music = MusicLoader(path).load_music()
        # Progress bar value
        self._progress = 0
        # Total song
        self._total = len(self._music)

    def get_metadata(self, song):
        """
           Get metadata of the song, creates the song instance, and save the
           song in the database.
        """
        # Open the song with mutagen library
        mt_file = mutagen.File(song)
        # split the time and get the minutes and secconds
        minutes, secconds = divmod(round(mt_file.info.length), 60)
        # format the seconds
        secconds = secconds if len(str(secconds)) == 2 else "0"+str(secconds)
        # make the song duration string
        song_duration = f"{minutes}:{secconds}"
        # get the artist with the get method of dictionary
        # with a fallback value
        song_artist = mt_file.get('artist', ['Unknown Artist'])[0]
        genres = mt_file.get('genre', ['Unknow Genre'])
        album_name = mt_file.get('album', ['Unknow Album'])[0]
        album_year = mt_file.get('date', ["0000"])[0]
        song_track_number = mt_file.get('tracknumber', [0])[0]
        total_tracks = mt_file.get('totaltracks', [0])[0]
        total_discs = mt_file.get('totaldiscs', [0])[0]
        isrc = mt_file.get('isrc', ['No Info'])[0]
        song_disc_number = mt_file.get('discnumber', [0])[0]
        song_title = mt_file.get('title', [mt_file.filename])[0]
        song_encoder = mt_file.get('encoder', ['No Encoder Info'])[0]
        song_cover = mt_file.pictures

        album_image = None

        if song_cover:
            if not isinstance(song_cover, bytes):
                album_image = None
            else:
                album_image = song_cover[0].data
        # Create the song instance and saves it
        dq.CreateSong(song,
                      song_encoder,
                      song_duration,
                      song_artist,
                      genres,
                      album_name,
                      album_year,
                      total_tracks,
                      total_discs,
                      song_title,
                      isrc,
                      song_track_number,
                      song_disc_number,
                      album_image=album_image).save()

        return

    def run(self):
        """Qthread internal method."""
        for i, song in enumerate(self._music, 1):
            self.get_metadata(song)
            self.change_value.emit(i)
            song_name = os.path.splitext(os.path.split(song)[-1])[0]
            self.song_name.emit(song_name)
        self.finished.emit()


# The SVG Icon constant
# TODO: move constants to a configuration file
SVG_ICON = os.path.join(os.getcwd(), 'GUI', 'UI', 'gear_2.gif')


class LoadingWindow(QtWidgets.QMainWindow, Ui_CargandoWindow):
    """
    Loading window instance.

    Holds all the UI design values and display the loading UI.
    And make all the loading operations.
    """

    closed = pyqtSignal()

    def __init__(self, selected_path, parent=None):
        """Configure the window, the title and show the window."""
        super(LoadingWindow, self).__init__(parent=None)
        self.selected_path = selected_path
        self.setupUi(self)
        movie = QtGui.QMovie(SVG_ICON)
        self.MovieScreen.setMovie(movie)
        movie.start()
        self.setWindowTitle("Analizando Carpeta")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setFixedSize(self.width(), self.height())
        self.show()

    def _percentaje_calculator(self, part):
        if not part:
            return 0
        return int(100 * float(part)/float(self._total_songs))

    def finishLoading(self):
        """When load finish emits a signal to main and close the window."""
        self.closed.emit()
        self.close()

    def setValue(self, progress):
        """Set the progressBar progress percentage."""
        self.progressBar.setValue(self._percentaje_calculator(progress))

    def setName(self, name):
        """Put the info signal in the info label."""
        self.InfoLabel.setText(f"Importando: {name}")

    def load(self):
        """
        Set the progressbar to 0.

           Creates the music loader instance
           Connects all the signals to the corresponding functions
           and start the song library creation
        """
        self.progressBar.setMinimum = 0
        self.progressBar.setMaximum = 100
        self.progressBar.setValue(0)
        self.thread = MetaReader(self.selected_path)
        self.thread.change_value.connect(self.setValue)
        self.thread.song_name.connect(self.setName)
        self.thread.finished.connect(self.finishLoading)
        self._total_songs = self.thread._total
        self.thread.start()
