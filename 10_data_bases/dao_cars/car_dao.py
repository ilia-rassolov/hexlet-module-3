import psycopg2
from psycopg2.extras import NamedTupleCursor
from cars import Car
from users import User


conn = psycopg2.connect(dbname='hexlet', user='user')


class CarDAO:
    def __init__(self, conn_):
        self.conn = conn_

    def save_user(self, user):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            if user.id is None:
                cur.execute("INSERT INTO users (first_name, last_name, address) VALUES (%s, %s, %s) RETURNING id",
                            (user.first_name, user.last_name, user.address))
                user.id = cur.fetchone().id
            else:
                cur.execute("UPDATE users SET first_name = %s, last_name = %s, address = %s WHERE users.id = user.id",
                            (user.first_name, user.last_name, user.address))
            self.conn.commit()

    def save_car(self, car):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            if car.id is None:
                cur.execute("""INSERT INTO cars (manufacturer, model, plate, color, user_id) VALUES (%s, %s, %s, %s, %s)
                RETURNING id""", (car.manufacturer, car.model, car.plate, car.color, car.user_id))
                car.id = cur.fetchone().id
            else:
                cur.execute("""UPDATE cars SET manufacturer = %s, model = %s, plate = %s, color = %s, user_id = %s
                    WHERE car.id = cars.id""", (car.manufacturer, car.model, car.plate, car.color, car.user_id))
            self.conn.commit()

    def find_info_cars(self, car_plate):
        with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            cur.execute("SELECT * FROM cars WHERE cars.plate = %s", (car_plate,))
            record = cur.fetchone()
            if record is None:
                raise KeyError('Car is not found')
            else:
                car = Car(plate=record.plate, manufacturer=record.manufacturer, model=record.model,
                       color=record.color, owner=record.user_id, id=record.id)
                print(car.owner)
                cur.execute(f"SELECT * FROM users WHERE users.id = {car.owner}")
                record = cur.fetchone()
                user = User(first_name=record.first_name, last_name=record.last_name,
                             address=record.address, id=record.id)
                return car, user

# new_user = Users(first_name='Jo', last_name='Do', address='Samara')
# new_car = Cars(25, 'Mers', 'GL', 'a456kx763', 'blue')
# CarDAO(conn).save_user(new_user)
# CarDAO(conn).save_car(new_car)
# print(new_car.id)
# print(new_user.id)
print(CarDAO(conn).find_info_cars('a456kx763'))

class CarDAO:
    def __init__(self, conn):
        self.conn = conn

# BEGIN
#     def find(self, car_plate):
#         with self.conn.cursor(cursor_factory=NamedTupleCursor) as cur:
#             car_sql = "SELECT * FROM cars WHERE plate = %s"
#             cur.execute(car_sql, (car_plate,))
#             car_result = cur.fetchone()
#
#             if not car_result:
#                 return None
#
#             car = Car(
#                 manufacturer=car_result.manufacturer,
#                 model=car_result.model,
#                 plate=car_result.plate,
#                 color=car_result.color,
#                 id=car_result.id
#             )
#
#             owner_id = car_result.user_id
#             user_sql = "SELECT * FROM users WHERE id = %s"
#             cur.execute(user_sql, (owner_id,))
#             user_result = cur.fetchone()
#
#             user = User(
#                 first_name=user_result.first_name,
#                 last_name=user_result.last_name,
#                 address=user_result.address,
#                 id=user_result.id
#             )
#             car.owner = user
#
#             return car

