from backend.dbArchitecture import Album, Artist, Song, Genre
def get_artists():
    return Artist.select()

def get_artist_albums(artist):
    return Album.select().where(Album.artist == artist)

def get_album_songs(album):
    return Song.select().where(Song.album == album)
    