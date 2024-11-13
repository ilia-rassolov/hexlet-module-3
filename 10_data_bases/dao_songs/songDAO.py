from  song import  Song
import psycopg2
from psycopg2.extras import NamedTupleCursor

conn = psycopg2.connect(dbname='hexlet', user='user')

class SongDAO:
    def __init__(self, conn):
        self.conn = conn


    def save_song(self, song):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            if song.id is None:
                cur.execute(f"INSERT INTO songs (title, artist_name) VALUES (%s, %s) RETURNING id",
                            (song.title, song.artist_name))
                song.id = cur.fetchone().id
            else:
                cur.execute(f"UPDATE songs SET title = %s, artist_name = %s WHERE id = %s",
                            (song.title, song.artist_name, song.id))
            self.conn.commit()

    def find_songs(self, substring):
        with self.conn.cursor() as cur:
            cur.execute(f"SELECT * FROM songs WHERE title LIKE %s ORDER BY id", (f"%{substring}%",))
            result = cur.fetchall()
            return  result

new_song = Song('Its is my life', 'Dr.Alban')
# SongDAO(conn).save_song(new_song)
# print(SongDAO(conn).find_songs('sc'))