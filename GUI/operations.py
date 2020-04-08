"""The main window operations."""

from GUI.main_window import Ui_Pybar2000
from GUI.loading import LoadingWindow
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QApplication, QFileDialog
import backend.dbGet as g
import sys
import os

# TODO: Move the qss to a file
QSS = qss = """
QMenuBar {
    background-color: #595959
}
QMenuBar::item {
    spacing: 3px;
    padding: 2px 10px;
    background-color: #595959;
}
QMenuBar::item:selected {
    background-color: #757575;
}
QMenuBar::item:pressed {
    background: #757575;
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */

QMenu {
    background-color: #999999;
    border: 1px solid black;
    margin: 2px;
}
QMenu::item {
    background-color: transparent;
}
QMenu::item:selected {
    background-color: #bfbfbf;
    color: rgb(255,255,255);
}
"""

# TODO: Refactor, profile, find memory leaks

UI_PATH = os.path.join(os.getcwd(), 'GUI', 'UI')


class MainWindow(QtWidgets.QMainWindow, Ui_Pybar2000):
    """The main window controller."""

    def __init__(self, parent=None):
        """Configure al the desing, colors styles ui etc."""
        super(MainWindow, self).__init__(parent)
        STYLE = (':enabled{background-color: #565554;} ' +
                 ':disabled{background-color:#858585; color:#acadac}')
        # Stop
        self.STOP = QtGui.QIcon(os.path.join(UI_PATH, 'pause.png'))
        # Play
        self.PLAY = QtGui.QIcon(os.path.join(UI_PATH, 'play.png'))

        # SetupUI
        self.setupUi(self)
        # Window Design
        self.Information.setColumnCount(2)
        prop = QtWidgets.QTableWidgetItem('Propiedad')
        value = QtWidgets.QTableWidgetItem('Valor')
        prop.setBackground(QtGui.QColor(86, 85, 84))
        prop.setForeground(QtGui.QColor(255, 255, 255))
        value.setBackground(QtGui.QColor(86, 85, 84))
        value.setForeground(QtGui.QColor(255, 255, 255))
        self.Atras.setStyleSheet(STYLE)
        # self.Pause.setStyleSheet(STYLE)
        self.ToggleAudio.setStyleSheet(STYLE)
        self.Play.setStyleSheet(STYLE)
        # self.Pause.setStyleSheet(STYLE)
        self.Stop.setStyleSheet(STYLE)
        self.Prev.setStyleSheet(STYLE)
        self.Next.setStyleSheet(STYLE)
        self.Information.setHorizontalHeaderItem(0, prop)
        self.Information.setHorizontalHeaderItem(1, value)
        # Make Menu
        bar = self.menuBar()
        bar.setStyleSheet('background-color:#595959')
        file_menu = bar.addMenu('Archivo')

        # Test SubWindow
        # self.form_loading = LoadingWindow(parent=MainWindow)

        # Menu Actions
        self.add_folder_action = QtWidgets.QAction('Abrir Carpeta', self)
        self.close_app_action = QtWidgets.QAction('Salir', self)
        file_menu.addAction(self.add_folder_action)
        file_menu.addSeparator()
        file_menu.addAction(self.close_app_action)

        self.add_folder_action.triggered.connect(self._select_folder)

        # Icon DIR
        ICON_DIR = os.path.join(os.getcwd(), 'GUI', 'UI')
        # Icons
        self.noMuteIcon = QtGui.QIcon(os.path.join(ICON_DIR, 'altavoz.png'))
        self.MuteIcon = QtGui.QIcon(os.path.join(ICON_DIR, 'mudo.png'))
        # Duration
        self.duration = 0
        # Level
        self.level = 0

        # Button Atras
        self.Atras.setEnabled(False)

        # All lists
        self.albumes_current = []

        # When song clicked
        self.Canciones.currentRowChanged.connect(self._get_metadata)

        # Query Artists
        # self._populate_artist()

        # Artist Clicked
        # self.Artistas.itemClicked.connect(self._artista_click)

        # Album Clicked
        # self.Albumes.itemClicked.connect(self._albumes_click)

        self.Explorer.itemDoubleClicked.connect(self._explorer_dblClick)
        self.Explorer.itemClicked.connect(self._explorer_click)
        # Song clicked
        self.Canciones.itemClicked.connect(self._canciones_click)

        # Play button click
        self.Play.clicked.connect(self._play_song)

        # Current selected artist
        self.current_artist = None

        # Info Row Count
        self.Information.setRowCount(10)
        self.Information.verticalHeader().setVisible(False)
        # Set Player
        self.player = QtMultimedia.QMediaPlayer()
        # Signal
        self.player.durationChanged.connect(self._duration_changed)
        self.player.positionChanged.connect(self._position_changed)
        # Song on double click
        self.Canciones.itemDoubleClicked.connect(self._play_song)

        # Next
        self.Next.clicked.connect(self._play_next)

        # Prev
        self.Prev.clicked.connect(self._play_prev)

        # Atras
        self.Atras.clicked.connect(self._before)
        # Configure Volume
        self.volume = 100
        self.Volumen.setMinimum(0)
        self.Volumen.setMaximum(100)
        self.Volumen.setValue(self.volume)
        self.Volumen.valueChanged.connect(self._volume_change)

        #  Pause Stop
        # self.Pause.clicked.connect(self._pause)
        self.Stop.clicked.connect(self._stop)
        self.position = None
        self.muted = False

        # LEVEL SETTER
        self._set_level()
        # Toggle Audio Icon
        if not self.muted:
            self.ToggleAudio.setIcon(self.noMuteIcon)
        else:
            self.ToggleAudio.setIcon(self.MuteIcon)

        self.ToggleAudio.clicked.connect(self._toggle_audio)
        # On Exit
        self.closeEvent = self._close_event

    # def _populate_artist(self):
    #     for artist in self.artists_query:
    #         self.Explorer.addItem(artist.name)

    def _select_folder(self):
        folder = QFileDialog.getExistingDirectory(self,
                                                  "Escoge una carpeta",
                                                  "/home",
                                                  QFileDialog.ShowDirsOnly)

        self.form_loading = LoadingWindow(folder, parent=MainWindow)
        self.form_loading.load()
        self.songs_current, self.total = g.get_all_songs()
        self.form_loading.closed.connect(self._finish_import)

    def _finish_import(self):
        self._set_level()

    def _get_metadata(self, element):
        # Get current row
        row = self.Canciones.currentRow()
        # Get the songs
        current_song = self.songs_current[row]
        current_album = current_song.album
        current_artist = current_album.artist
        current_genre = current_album.genre
        # Set Items

        # Artist name
        artist_name_key = QtWidgets.QTableWidgetItem('Artist')
        artist_name_value = QtWidgets\
            .QTableWidgetItem(f'{current_artist.name}')
        # All the song info
        song_title_key = QtWidgets.QTableWidgetItem(f'Title')
        song_title_value = QtWidgets.QTableWidgetItem(f'{current_song.title}')
        song_duration_key = QtWidgets.QTableWidgetItem('Duration')
        song_duration_value = QtWidgets\
            .QTableWidgetItem(f'{current_song.duration}')
        song_track_number_key = QtWidgets.QTableWidgetItem('Track Number')
        song_track_number_value = QtWidgets\
            .QTableWidgetItem(f'{current_song.track}')
        song_disc_number_key = QtWidgets\
            .QTableWidgetItem("Song Disc")
        song_disc_number_value = QtWidgets\
            .QTableWidgetItem(f'{current_song.disc_number}')
        # All album info
        album_name_key = QtWidgets.QTableWidgetItem('Album Name')
        album_name_value = QtWidgets\
            .QTableWidgetItem(f'{current_album.name}')
        album_release_key = QtWidgets\
            .QTableWidgetItem('Album Release Date')
        album_release_value = QtWidgets\
            .QTableWidgetItem(f'{current_album.year}')
        album_genres_list = ", ".join(current_genre.genres
                                      .strip('][')
                                      .split(', ')).replace('\'', '')
        album_genres_key = QtWidgets.QTableWidgetItem('Genres')
        album_genres_value = QtWidgets\
            .QTableWidgetItem(f'{album_genres_list}')
        album_total_tracks_key = QtWidgets\
            .QTableWidgetItem('Album Total Tracks')
        album_total_tracks_value = QtWidgets\
            .QTableWidgetItem(f'{current_album.album_tracks}')
        album_disc_number_key = QtWidgets\
            .QTableWidgetItem('Album Disc Number')
        album_disc_number_value = QtWidgets\
            .QTableWidgetItem(f'{current_album.total_discs}')
        # Artist Name

        # Title
        self.Information.setItem(0, 0, song_title_key)
        self.Information.setItem(0, 1, song_title_value)
        # Artist
        self.Information.setItem(1, 0, artist_name_key)
        self.Information.setItem(1, 1, artist_name_value)
        # Album Name
        self.Information.setItem(2, 0, album_name_key)
        self.Information.setItem(2, 1, album_name_value)
        # Song Duration
        self.Information.setItem(3, 0, song_duration_key)
        self.Information.setItem(3, 1, song_duration_value)
        # Song Track Number
        self.Information.setItem(4, 0, song_track_number_key)
        self.Information.setItem(4, 1, song_track_number_value)
        # Song Disc Number
        self.Information.setItem(5, 0, song_disc_number_key)
        self.Information.setItem(5, 1, song_disc_number_value)
        # Album Release Key
        self.Information.setItem(6, 0, album_release_key)
        self.Information.setItem(6, 1, album_release_value)
        # Album Genres Key
        self.Information.setItem(7, 0, album_genres_key)
        self.Information.setItem(7, 1, album_genres_value)
        # Album Total Tracks
        self.Information.setItem(8, 0, album_total_tracks_key)
        self.Information.setItem(8, 1, album_total_tracks_value)
        # Album Disc Number
        self.Information.setItem(9, 0, album_disc_number_key)
        self.Information.setItem(9, 1, album_disc_number_value)

    def _set_level(self, element=False):
        # Level 0: Todo
        # Level 1: Artists
        self.songs_current, self.total = g.get_all_songs()
        if not self.songs_current:
            self.Explorer.setEnabled(False)

        if self.level == 0:
            self.Explorer.setEnabled(True)
            self.Explorer.clear()
            self.Atras.setEnabled(False)
            self._populate_songs()
            self.Explorer.addItem(f'Todo ({self.total})')
            self.Explorer.setCurrentRow(0)
            self._make_playlist()
            self.Canciones.setCurrentRow(0)
            self.current_song = 0

        if self.level == 1:
            self.current_artist, self.artists_str = g.get_artists()
            self.Explorer.clear()
            for artist in self.artists_str:
                self.Explorer.addItem(artist)
                self.Atras.setEnabled(True)
                self.Explorer.setCurrentRow(0)
                self._select_songs_artists()

        if self.level == 2:
            current_artist = self.current_artist[self.Explorer.row(element)]
            query = g.get_artists_albums(current_artist)
            self.current_albums, self.album_str = query
            self.Explorer.clear()
            for album in self.album_str:
                self.Explorer.addItem(album)
                self.Atras.setEnabled(True)
                self.Explorer.setCurrentRow(0)
                songs_current = g.get_song_from_album(self.current_albums[0])
                self.songs_current = songs_current

    def _before(self):
        if self.level != 0:
            self.level -= 1
            self._set_level()

    def _select_songs_artists(self, element=0):
        if isinstance(element, int):
            element = self.current_artist[element]
            self.songs_current = g.get_song_from_artist(element)
        else:
            selected_row = self.Explorer.row(element)
            element = self.current_artist[selected_row]
            self.songs_current = g.get_song_from_artist(element)
        self._populate_songs()

    def _select_album_songs(self, element=0):
        if isinstance(element, int):
            element = self.current_albums[element]
            self.songs_current = g.get_song_from_album(element)
        else:
            index = self.Explorer.row(element)
            current_album = self.current_albums[index]
            self.songs_current = g.get_song_from_album(current_album)
        self._populate_songs()

    def _explorer_dblClick(self, element):
        if self.level != 2:
            if self.level == 0:
                self.level = 1
                self._set_level(element)
            elif self.level == 1:
                self.level = 2
                self._set_level(element)

    def _explorer_click(self, element):
        if self.level == 1:
            self._select_songs_artists(element)
        if self.level == 2:
            self._select_album_songs(element)

    def _toggle_audio(self):
        if self.player.isMuted():
            self.ToggleAudio.setIcon(self.noMuteIcon)
            self.player.setMuted(False)
            self.player.setVolume(self.volume)

        else:
            self.ToggleAudio.setIcon(self.MuteIcon)
            self.volume = self.player.volume()
            self.player.setMuted(True)

    def _artista_click(self, item_clicked):
        selected_row = self.Artistas.row(item_clicked)
        current_artist = self.artists[selected_row]
        self._populate_album(current_artist)

    # def _populate_album(self, artist):
    #     album_query = g.get_artist_albums(artist)
    #     self.Explorer.clear()
    #     self.albumes_current = []
    #     for album in album_query:
    #         self.Explorer.addItem(album.name)
    #         self.albumes_current.append(album)

    # def _albumes_click(self, item_clicked):
    #     selected_row = self.Albumes.row(item_clicked)
    #     current_album = self.albumes_current[selected_row]
    #     self._populate_songs(current_album)

    def _populate_songs(self):
        self.Canciones.clear()
        for song in self.songs_current:
            self.Canciones.addItem(song.title)

    def _canciones_click(self, item_clicked):
        selected_row = self.Canciones.row(item_clicked)
        self.current_song = selected_row

    def _play_song(self):
        if self.player.state() == 2:
            if self.player.position:
                self.player.setPosition(self.position)
                self.player.play()
                self.Play.setIcon(self.STOP)

        elif self.player.state() == 0:
            self._make_playlist()
            self.player.setPlaylist(self.playlist)
            self.playlist.setCurrentIndex(self.current_song)
            self.player.setVolume(self.volume)
            self.player.play()
            self.Play.setIcon(self.STOP)

        elif self.player.state() == 1:
            self._pause()
            self.Play.setIcon(self.PLAY)

    def _duration_changed(self, duration):
        self.Progress.setMinimum = 0
        self.Progress.setMaximum = duration
        self.duration = duration

    def _percentaje_calculator(self, part):
        if not self.duration:
            return 0
        return int(100 * float(part)/float(self.duration))

    def _percentage_to_num(self, percent):
        return (percent * self.duration) / 100.0

    def _progress_value_changed(self, value):
        position = self._percentage_to_num(value)
        self.player.setPosition(position)

    def _position_changed(self, position):
        self.Progress.setValue(self._percentaje_calculator(position))

    def _play_next(self):
        self.playlist.setCurrentIndex(self.playlist.nextIndex())
        self.player.play()
        self.Canciones.setCurrentRow(self.playlist.currentIndex())

    def _play_prev(self):
        self.playlist.setCurrentIndex(self.playlist.previousIndex())
        self.player.play()
        self.Canciones.setCurrentRow(self.playlist.currentIndex())

    def _make_playlist(self):
        playlist = QtMultimedia.QMediaPlaylist()
        for song in self.songs_current:
            song_file = QtCore.QUrl.fromLocalFile(song.path)
            media = QtMultimedia.QMediaContent(song_file)
            playlist.addMedia(media)
        self.playlist = playlist

    def _volume_change(self, value):
        self.player.setVolume(value)
        self.volume = value

    def _pause(self):
        self.position = self.player.position()
        self.player.pause()

    def _stop(self):
        self.player.stop()

    def _close_event(self):
        pass


def main():
    """Run the program in the current module."""
    app = QApplication(sys.argv)
    form = MainWindow()
    app.setStyleSheet(QSS)
    form.show()
    app.exec()


if __name__ == "__main__":
    main()
