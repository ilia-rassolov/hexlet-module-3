import psycopg2
import json


data_json = json.load(open('data.json'))
conn = psycopg2.connect(dbname='hexlet', user='user')
columns = {'id': 'SERIAL PRIMARY KEY', 'title': 'VARCHAR(50)', 'artist_name': 'VARCHAR(50)'}
# , 'price': 'INT'
class Table:
	def __init__(self, name: str, titles_types: dict):
		self.name = name
		self.titles_types = titles_types


	def create_table(self):
		params = [f"{title} {type}" for title, type in self.titles_types.items()]
		string_create = ', '.join(params)
		with conn.cursor() as curs:
			curs.execute(f"CREATE TABLE {self.name} ({string_create});")
			conn.commit()


	def add_data(self):
		with conn.cursor() as curs:
			titles_types_copy = self.titles_types.copy()
			titles_types_copy.pop('id')
			string_insert = ', '.join([f"{title}" for title in titles_types_copy])
			titles_data = ', '.join([f"%({title})s" for title in titles_types_copy])
			for row in data_json:
				add_data = f"INSERT INTO {self.name} ({string_insert}) VALUES ({titles_data});"
				curs.execute(add_data, row)
		conn.commit()


products_ = Table('songs', columns)
products_.create_table()
products_.add_data()
# print(', '.join([f"%({title})s" for title in products_.titles_types.keys()]))

