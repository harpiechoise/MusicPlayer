"""This module is the definition of the database models for the indexing of the music library."""

# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship, sessionmaker
# from sqlalchemy.ext.declarative import declarative_base

# Base = declarative_base()
# Year = String

# class Artist(Base):
#     # Artist
#     __tablename__ = "artists"
#     _id = Column('id', Integer, primary_key=True)

#     name = Column('artist', String, unique=True, nullable=True)


# class Album(Base):
#     # Album
#     __tablename__ = "albums"
#     _id = Column('id', Integer, primary_key=True)
#     name = Column('album', String, unique=True, nullable=True)
#     artist_id = Column(Integer, ForeignKey('artist._id'))
#     artist = relationship('Artist', backref='albums', foreign_keys=[artist_id])
#     date = Column('date', Year, unique=True, nullable=True)
#     genre = Column('genre', String, unique=True, nullable=True)
#     album_tracks = Column('total_tracks', Integer, unique=True, nullable=True)
#     total_discs =  Column('disc_total', Integer, unique=True, nullable=True)

# class Song(Base):
#     __tablename__ = "songs"
#     _id = Column('id', Integer, primary_key=True)
#     album_id = Column(Integer, ForeignKey('album._id'), nullable=True)
#     album = relationship('Album', backref='songs', foreign_keys=[album_id])
#     title = Column('title', String, unique=False, nullable=True)
#     duration = Column('duration', String, unique=False, nullable=True)
#     encoder = Column('encoder', String, unique=False, nullable=True)
#     isrc = Column('ISRC', String, unique=False, nullable=False)
#     track = Column('track', Integer, unique=False, nullable=True)
#     disc_number = Column('disc_number', Integer, unique=False, nullable=True)


from peewee import Model, SqliteDatabase, CharField, IntegerField, ForeignKeyField, BlobField
db = SqliteDatabase('my_database.db')


class BaseModel(Model):
    """This is the base model, thats contains the database of all subsequent tables."""

    class Meta:
        """This class holds the corresponding database."""

        database = db

class Image(BaseModel):
    """This table is for parse the album images is Bytes."""

    album_name = CharField(null=False)
    image = BlobField(null=False)

class Artist(BaseModel):
    """This table stands for artists names."""

    name = CharField(null=False, unique=True)

class Genre(BaseModel):
    """This table stands for genres."""

    genres = CharField(null=False, unique=True)

class Album(BaseModel):
    """This table holds the album metadata."""

    name = CharField(null=False, unique=False)
    artist = ForeignKeyField(Artist, backref='albums', null=True)
    album_image = ForeignKeyField(Image, null=True)
    year = CharField(null=True, unique=False, max_length=4)
    genre = ForeignKeyField(Genre, backref='album', null=True)
    album_tracks = IntegerField(null=True, unique=False)
    total_discs = IntegerField(null=True, unique=False)

class Song(BaseModel):
    """This table holds the song metadata."""
    
    title = CharField(null=False, unique=False)
    album = ForeignKeyField(Album, backref='songs', null=True)
    path = CharField(null=True, unique=False)
    duration = CharField(null=True, unique=False, max_length=10)
    encoder = CharField(null=True, unique=False)
    isrc = CharField(null=True, unique=False)
    track = IntegerField(null=True, unique=False)
    disc_number = IntegerField(null=True, unique=False)

