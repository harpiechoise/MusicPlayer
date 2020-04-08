from GUI.loading_window import Ui_CargandoWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QApplication
import os
import os
import glob
from pathlib import Path
import mutagen
from backend import dbQuerys as dq
from PyQt5.QtCore import Qt, QThread, pyqtSignal


class MusicLoader():
    def __init__(self, path):
        self.path = path
        self.allowed_files = ['.flac', '.mp3', '.wav', '.ogg']
        self._music = []

    def load_music(self):
        r = []
        for path in Path(self.path).rglob(r'*.*'):
            strpath = path.absolute().as_posix()
            if os.path.splitext(strpath)[1] in self.allowed_files:
                r.append(strpath)
        return r
    
class MetaReader(QThread):
    change_value = pyqtSignal(int)
    song_name = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, path):
        super(MetaReader, self).__init__()
        self._music = MusicLoader(path).load_music()
        self._progress = 0
        self._total = len(self._music)


    def get_metadata(self, song):
        mt_file = mutagen.File(song)
        minutes, secconds = divmod(round(mt_file.info.length), 60)
        secconds = secconds if len(str(secconds)) == 2 else "0"+str(secconds)
        song_duration = f"{minutes}:{secconds}"
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
        for i, song in enumerate(self._music, 1):
            self.get_metadata(song)
            self.change_value.emit(i)
            song_name = os.path.splitext(os.path.split(song)[-1])[0]
            self.song_name.emit(song_name)
        self.finished.emit()

SVG_ICON = os.path.join(os.getcwd(), 'GUI', 'UI', 'gear_2.gif')

class LoadingWindow(QtWidgets.QMainWindow, Ui_CargandoWindow):
    closed = pyqtSignal()

    def __init__(self, selected_path, parent=None):
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
        self.closed.emit()
        self.close()

    def setValue(self, progress):
        self.progressBar.setValue(self._percentaje_calculator(progress))

    def setName(self, name):
        self.InfoLabel.setText(f"Importando: {name}")

    def load(self):
        self.progressBar.setMinimum = 0
        self.progressBar.setMaximum = 100
        self.progressBar.setValue(0)
        self.thread = MetaReader(self.selected_path)
        self.thread.change_value.connect(self.setValue)
        self.thread.song_name.connect(self.setName)
        self.thread.finished.connect(self.finishLoading)
        self._total_songs = self.thread._total
        self.thread.start()
