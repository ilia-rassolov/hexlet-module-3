from  songDAO import SongDAO
import psycopg2
from psycopg2.extras import NamedTupleCursor

conn2 = psycopg2.connect(dbname='hexlet', user='user')


class MusicService:
    def __init__(self, conn):
        self.conn = conn

    def get_song_by_title(self, substring):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute(f"SELECT * FROM songs ORDER BY title")
            all = cur.fetchall()
            result = []
            for row in all:
                if substring in row.title.lower():
                    result.append(tuple(row))
            return result

print(MusicService(conn2).get_song_by_title('sc'))
