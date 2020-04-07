# -*- coding: utf8 -*-
from scoop import futures
import os
import glob
from pathlib import Path
import mutagen
from backend import dbQuerys as dq
from multiprocessing import Pool 
from queue import Queue as Q
from time import sleep

class MusicLoader():
    def __init__(self, path):
        self.path = path
        self.allowed_files = ['.flac', '.mp3', '.wav', '.ogg'] 

    def load_music(self):
        r = []
        for path in Path(self.path).rglob(r'*.*'):
            strpath = path.absolute().as_posix()
            if os.path.splitext(strpath)[1] in self.allowed_files:
                r.append(strpath)
        return r
    
class MetaReader(MusicLoader):
    def __init__(self, path):
        super().__init__(path)
        self._music = self.load_music()
    
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

        sleep(0.1)
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

    def populate(self, n_threads=10):
        cpu = os.cpu_count()
        p = Pool(processes=cpu)
        p.map(self.get_metadata, self._music)

if __name__ == "__main__":
   loader =  MetaReader('/home/jaime/Música')
   r = loader.load_music()
   loader.populate()