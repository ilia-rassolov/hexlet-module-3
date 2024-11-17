from car_dao import CarDAO
import psycopg2


conn = psycopg2.connect(dbname='hexlet', user='user')


class CarBase:
    def __init__(self, conn_):
        self.conn = conn_

    def get_info(self, car_plate):
        car, user = CarDAO(self.conn).find_info_cars(car_plate)
        return {'car_plate': car.plate, 'car_manufacturer': car.manufacturer, 'car_model': car.model,
                'car_color': car.color, 'user_first_name': user.first_name, 'user_last_name': user.last_name,
                'user_address': user.address}


print(CarBase(conn).get_info('a456kx763'))


# class CarBase:
#     def __init__(self, conn):
#         self.conn = conn
#
#     def get_info(self, car_plate):
#         dao = CarDAO(self.conn)
#         car = dao.find(car_plate)
#
#         if car is None:
#             raise KeyError("Car is not found")
#
#         owner = car.owner
#
#         return {
#             "manufacturer": car.manufacturer,
#             "model": car.model,
#             "plate": car.plate,
#             "color": car.color,
#             "owner": f"{owner.first_name} {owner.last_name}",
#             "owner_address": owner.address
#         }