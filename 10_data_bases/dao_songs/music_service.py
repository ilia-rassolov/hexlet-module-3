from songDAO import SongDAO
import psycopg2


conn2 = psycopg2.connect(dbname='hexlet', user='user')


class MusicService:
    def __init__(self, conn):
        self.conn = conn

    def get_song_by_title(self, substring):
        without_register = f"(?i:{substring})"
        return SongDAO(self.conn).find_songs(without_register)


print(MusicService(conn2).get_song_by_title('Disc'))
