from backend.dbArchitecture import Album, Artist, Song, Genre
from typing import List

ArtistStr = List[str]
ArtistList = List[Artist]
AlbumStr = List[str]
AlbumList = List[Album]

def get_artists() -> (ArtistList, ArtistStr):
    artists = [artist for artist in Artist.select()]
    artists_str = []
    for artist in artists:
        artists_str.append(f"{artist.name} ({artist_n_songs(artist)})")
    return artists, artists_str

def get_song_from_artist(artist):
    for albums in artist.albums:
        songs = [song for song in albums.songs]
    return songs

def get_artists_albums(artist) -> (AlbumList, AlbumStr):
    album_str = [f'{album.name} ({album_n_songs(album)})' for album in artist.albums]
    album = [album for album in artist.albums]
    return album, album_str

def get_song_from_album(album):
    songs = [song for song in album.songs]
    return songs

def get_all_songs() -> (list, int):
    songs = [song for song in Song.select()]
    return songs, len(songs)

def artist_n_songs(artist) -> (list):
    artist = Artist.get_by_id(artist.id)
    for albums in artist.albums:
        songs = [song for song in albums.songs]
    return len(songs)

def album_n_songs(album) -> (list):
    songs = [song for song in album.songs]
    return len(songs)