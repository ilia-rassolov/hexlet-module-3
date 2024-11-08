# DROP TABLE IF EXISTS users, channels, channel_members, channel_messages;
#
# CREATE TABLE users (
#     id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#     username VARCHAR(50) NOT NULL,
#     phone_number VARCHAR(20) UNIQUE NOT NULL,
#     first_name VARCHAR(50),
#     last_name VARCHAR(50)
# );
#
# CREATE TABLE channels (
#     id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#     admin BIGINT REFERENCES users (id) NOT NULL,
#     name VARCHAR(50) UNIQUE NOT NULL,
#     slug VARCHAR(50) UNIQUE NOT NULL
# );
#
# CREATE TABLE channel_members (
#     id BIGINT GENERATED ALWAYS AS IDENTITY,
#     id_channel BIGINT REFERENCES channels (id),
#     id_users BIGINT REFERENCES users (id),
#     PRIMARY KEY (id_channel, id_users)
# );
#
# CREATE TABLE channel_messages (
#     id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
#     id_channel BIGINT REFERENCES channels (id) NOT NULL,
#     id_users BIGINT REFERENCES users (id) NOT NULL,
#     created_at TIMESTAMP,
#     body TEXT NOT NULL
# );
#
# INSERT INTO users (username, phone_number) VALUES
# ('bear', '+7902'), ('monkey', '+381');
# INSERT INTO channels (admin, name, slug) VALUES (1, 'mine', '/mine_01');
# INSERT INTO channel_members (id_channel, id_users) VALUES (1, 1), (1, 2);
# INSERT INTO channel_messages (id_channel, id_users, created_at, body) VALUES
# (1, 2, '2024-01-06', 'it is my first message');

# _____________________________________________________________
# import psycopg2_
def make_cars_table(conn):
    cursor_ = conn.cursor()
    request = '''CREATE TABLE cars (
        id SERIAL PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
        brand VARCHAR(50),
        model VARCHAR(50)
        )'''
    cursor_.execute(request)
    cursor_.close()


def populate_cars_table(conn, new_cars):
    cursor_ = conn.cursor()
    for new_car in new_cars:
        request = f"INSERT INTO cars (brand, model) VALUES {new_car}"
        cursor_.execute(request)
    cursor_.close()


def get_all_cars(conn):
    request = "SELECT * FROM cars ORDER BY brand"
    with conn:
        with conn.cursor() as curs:
            curs.execute(request)
            print(curs.fetchall())
    conn.close()

def make_cars_table(conn):
    with conn.cursor() as c:
        sql = """CREATE TABLE cars
                (id SERIAL PRIMARY KEY,
                brand VARCHAR(255),
                model VARCHAR(255))"""
        c.execute(sql)


def populate_cars_table(conn, cars):
    with conn.cursor() as c:
        sql = "INSERT INTO cars (brand, model) VALUES %s, %s;"
        c.execute(sql, cars)


def get_all_cars(conn):
    with conn.cursor() as c:
        sql = "SELECT * FROM cars ORDER BY brand ASC;"
        c.execute(sql)
        result = c.fetchall()
    return result

# conn = psycopg2_.connect('postgresql://tirion:secret@localhost:5432/tirion')
# make_cars_table(conn)
# get_all_cars(conn) # []
#
#
# cars = [('kia', 'sorento'), ('bmw', 'x5')]
# populate_cars_table(conn, cars)
# get_all_cars(conn)
# # [(1, 'kia', 'sorento'),
# #  (2, 'bmw', 'x5')]

