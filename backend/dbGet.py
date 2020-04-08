"""This is an inteface for all database operations."""

from backend.dbArchitecture import Album, Artist, Song, Genre
from typing import List

ArtistInstance = Artist
AlbumInstance = Album
SongInstance = Song
ArtistStr = List[str]
ArtistList = List[ArtistInstance]
SongsList = List[SongInstance]
AlbumStr = List[str]
AlbumList = List[AlbumInstance]
NumberOfSongs = int


def get_artists() -> (ArtistList, ArtistStr):
    """
    Fetch all artists from the database.

    Returns
    -------
    ArtistList: The list of the artist object
    ArtistStr: A colection of strings representations for artist Object 
               and the number of songs
    """
    artists = [artist for artist in Artist.select()]
    artists_str = []
    for artist in artists:
        artists_str.append(f"{artist.name} ({artist_n_songs(artist)})")
    return artists, artists_str

def get_song_from_artist(artist: ArtistInstance) -> (SongsList):
    """
    Fetch all songs from an artist.

    Params
    ------
    artist: Artist Instance.

    Returns:
    --------
    SongList: A collection of all songs instances of a given ArtistInstance.
    """
    for albums in artist.albums:
        songs = [song for song in albums.songs]
    return songs

def get_artists_albums(artist: ArtistInstance) -> (AlbumList, AlbumStr):
    """
    Fetch all the albums of a given artist instance.
    
    Params:
    -------
    Artist: An artist instance.

    Returns:
    -------
    AlbumList: A collection of AlbumObjects.
    AlbumStr: A collection of strings representation of Album instances-
    """
    album_str = [f'{album.name} ({album_n_songs(album)})' for album in artist.albums]
    album = [album for album in artist.albums]
    return album, album_str

def get_song_from_album(album: AlbumInstance) -> (SongList):
    """
    Fetch all songs of a given album instance.
    
    Params
    -------
    Album: Album instances.
    
    Returns
    -------
    SongList: A collection of SongInstances.
    """
    songs = [song for song in album.songs]
    return songs

def get_all_songs() -> (SongsList, NumberOfSongs):
    """
    Fetch all song on the database.
    
    Returns:
    -------
    SongList: A collection of SongInstances.
    NumberOfSongs: The total number of songs in the collection.
    """
    songs = [song for song in Song.select()]
    return songs, len(songs)

def artist_n_songs(artist:ArtistInstance) -> (NumberOfSongs):
    """
    Count the songs of a given artist instance.
    
    Params:
    ------
    ArtistInstance: An artist object instance

    Returns:
    -------
    NumberOfSongs: The total number of songs in the collection.

    TODO: Deprecate all _n_songs functions
    """
    artist = Artist.get_by_id(artist.id)
    for albums in artist.albums:
        songs = [song for song in albums.songs]
    return len(songs)

def album_n_songs(album: AlbumInstance) -> (NumberOfSongs):
    """
    Count the songs of a given album instance.
    
    Params:
    ------
    AlbumInstance: An album object instance.

    Returns:
    -------
    NumberOfSongs: The total number of songs in the collection.

    TODO: Deprecate all _n_songs functions
    """
    songs = [song for song in album.songs]
    return len(songs)