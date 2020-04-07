from GUI.main_window import Ui_Pybar2000
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import QApplication
import backend.dbGet as g
import sys
import miniaudio
import os

class MainWindow(QtWidgets.QMainWindow, Ui_Pybar2000):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        
        # SetupUI
        self.setupUi(self)
        
        ICON_DIR = os.path.join(os.getcwd(), 'GUI', 'UI')
        # Icons
        self.noMuteIcon = QtGui.QIcon(os.path.join(ICON_DIR, 'altavoz.png'))
        self.MuteIcon = QtGui.QIcon(os.path.join(ICON_DIR, 'mudo.png'))

        # Artists Query
        self.artists_query = g.get_artists()
        
        # All lists
        self.artists = [user for user in self.artists_query]
        self.albumes_current = []
        self.songs_current = []
        
        # Query Artists
        self._populate_artist()

        # Artist Clicked
        self.Artistas.itemClicked.connect(self._artista_click)
        
        # Album Clicked
        self.Albumes.itemClicked.connect(self._albumes_click)
        
        # Song clicked
        self.Canciones.itemClicked.connect(self._canciones_click)
        
        # Play button click
        self.Play.clicked.connect(self._play_song)
        
        # Current selected artist 
        self.current_artist = None
        
        # Set Player
        self.player = QtMultimedia.QMediaPlayer()
        
        # Song on double click
        self.Canciones.itemDoubleClicked.connect(self._play_song)
        
        # Next
        self.Next.clicked.connect(self._play_next)

        # Prev
        self.Prev.clicked.connect(self._play_prev)


        # Configure Volume
        self.volume = 100
        self.Volumen.setMinimum(0)
        self.Volumen.setMaximum(100)
        self.Volumen.setValue(self.volume)
        self.Volumen.valueChanged.connect(self._volume_change)
    
        #  Pause Stop
        self.Pause.clicked.connect(self._pause)
        self.Stop.clicked.connect(self._stop)
        self.position = None
        self.muted = False

        # Toggle Audio Icon
        if not self.muted:
            self.ToggleAudio.setIcon(self.noMuteIcon)
        else:
            self.ToggleAudio.setIcon(self.MuteIcon)

        self.ToggleAudio.clicked.connect(self._toggle_audio)
        # On Exit
        self.closeEvent = self._close_event

    def _populate_artist(self):
        for artist in self.artists_query:
            self.Artistas.addItem(artist.name)
    
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

    def _populate_album(self, artist):
        album_query = g.get_artist_albums(artist)
        self.Albumes.clear()
        self.albumes_current = []
        for album in album_query:
            self.Albumes.addItem(album.name)
            self.albumes_current.append(album)

    def _albumes_click(self, item_clicked):
        selected_row = self.Albumes.row(item_clicked)
        current_album = self.albumes_current[selected_row]
        self._populate_songs(current_album)


    def _populate_songs(self, album):
        song_query = g.get_album_songs(album)
        self.Canciones.clear()
        self.songs_current = []
        for song in song_query:
            self.Canciones.addItem(song.title)
            self.songs_current.append(song)
    
    def _canciones_click(self, item_clicked):
        selected_row = self.Canciones.row(item_clicked)
        self.current_song = selected_row

    def _play_song(self):
        if self.player.state() == 2:
            if self.player.position:
                self.player.setPosition(self.position)
                self.player.play()
        else:
            self._make_playlist()
            self.player.setPlaylist(self.playlist)
            self.playlist.setCurrentIndex(self.current_song)
            self.player.setVolume(self.volume)
            self.player.play()

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
            media = QtMultimedia.QMediaContent(QtCore.QUrl.fromLocalFile(song.path))
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
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()