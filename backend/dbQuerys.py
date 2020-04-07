import backend.dbArchitecture as database
from backend.dbArchitecture import Album, Artist, Song, Genre, Image
from typing import List
import os


Genres = List[str]
DatabaseConnection = database.db
ReleaseYear = str

class CreateSong():
    def __init__(self,
                 song_file_path,
                 encoder,
                 song_duration,     
                 artist='Unknown Artist',
                 genres=['Unknow Genre'],
                 album_name='Unknow Album',
                 album_year='0000',
                 album_tracks=0,
                 album_total_discs=0,
                 song_title='Unknow Title',
                 isrc='Unknown ISRC',
                 song_track_number=0,
                 song_disc_number=0,
                 album_image=None):
        
        # Database Conection
        self.db = database.db
        # Table Creation
        self.db.create_tables([Artist, Song, Album, Genre, Image])

        # Song Technical Data
        self.song_file_path = song_file_path
        self.song_duration = song_duration
        
        # Song Metadata
        self.song_title = song_title
        self.song_isrc = isrc
        self.song_track_number = song_track_number
        self.song_disc_number = song_disc_number
        self.encoder = encoder
        # Artist Name
        self.artist_name = artist
        
        # Genres
        self.genres = genres

        # Album Metadata
        self.album_name = album_name
        self.album_name_year = album_year
        self.album_total_tracks = album_tracks
        self.album_total_discs = album_total_discs
        self.album_image = album_image

        try:
            self.db.connect()
        except:
            pass

    def _createArtist(self):
        artist, _ = Artist.get_or_create(name=self.artist_name)
        artist.save()
        return artist
        

    def _createAlbum(self):

        obj_artist = self._createArtist()
        genres, created = Genre.get_or_create(genres=str(self.genres))
        if created:
            genres.save()
        
        album, _ = Album.get_or_create(name=self.album_name)
        album.genre = genres
        album.artist = obj_artist
        album.year = self.album_name_year
        album.album_tracks = self.album_total_tracks
        album.total_discs = self.album_total_discs

        if self.album_image:
            album_image = Image.get_or_create(album_name=self.album_name, image=self.album_image)
            album.album_image = album_image
        
        album.save()
        return album
    
    def _create_song(self):
        song, _ = Song.get_or_create(title=self.song_title)
        album = self._createAlbum()
        song.album = album
        song.path = self.song_file_path
        song.duration = self.song_duration
        song.isrc = self.song_isrc
        song.track = self.song_track_number
        song.disc_number = self.song_disc_number
        song.encoder = self.encoder
        return song

    def _check_db(self):
        if not os.path.exists(os.path.join(os.getcwd(), 'my_database.db')):
            self.db.create_tables([Album, Artist, Song, Genre])

    def save(self):
        self._check_db()
        song = self._create_song()
        song.save()
