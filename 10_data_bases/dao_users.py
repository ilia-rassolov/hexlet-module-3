from dao_models import User
import dao_db

conn = dao_db.get_connection()


user = User(username="John Doe", phone="1234567890")
print(user, user.id) # None

new_user = dao_db.save_user(conn, user)
# делаем коммит после каждого изменения
dao_db.commit(conn)
print(new_user, new_user.id) # тут уже выводится какой-то id

found_user = dao_db.find_user(conn, 6)
dao_db.commit(conn)
print(found_user) # здесь выводится найденный user
drop_user = dao_db.drop_user(conn, 5)
# закрываем соединение
dao_db.commit(conn)
conn.close()
