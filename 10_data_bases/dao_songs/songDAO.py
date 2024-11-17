from song import Song
import psycopg2
from psycopg2.extras import NamedTupleCursor
import re

conn = psycopg2.connect(dbname='hexlet', user='user')


class SongDAO:
    def __init__(self, conn):
        self.conn = conn

    def save_song(self, song):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            if song.id is None:
                cur.execute("INSERT INTO songs (title, artist_name) VALUES (%s, %s) RETURNING id",
                            (song.title, song.artist_name))
                song.id = cur.fetchone().id
            else:
                cur.execute("UPDATE songs SET title = %s, artist_name = %s WHERE id = %s",
                            (song.title, song.artist_name, song.id))
            self.conn.commit()

    def find_songs(self, substring):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute("SELECT * FROM songs ORDER BY title")
            songs = cur.fetchall()
            result = []
            for song in songs:
                if re.search(substring, song.title):
                    result.append(Song(id=song.id, title=song.title, artist_name=song.artist_name))
            return result


# new_song2 = Song('Its is my life', 'Dr.Alban')
# more_song = Song(title='disco', artist_name='ABBA')
# print(new_song2)
# SongDAO(conn).save_song(new_song2)
print(SongDAO(conn).find_songs('Disco'))



    # def find_all_by_title_contains(self, condition):
    #     with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
    #         sql = "SELECT * FROM songs WHERE title ILIKE %s ORDER BY title"
    #         search_pattern = f"%{condition}%"
    #         cur.execute(sql, (search_pattern,))
    #
    #         result = []
    #         for row in cur:
    #             song = Song(
    #                 id=row.id,
    #                 title=row.title,
    #                 artist_name=row.artist_name
    #             )
    #             result.append(song)
    #
    #     return result

