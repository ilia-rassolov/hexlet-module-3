import psycopg2
from psycopg2.extras import DictCursor

conn_ = psycopg2.connect(dbname='hexlet', user='user')


def get_db(app):
    return psycopg.connect(app.config['DATABASE_URL'])


class ProductsRepository:
    def __init__(self, conn):
        self.conn = conn

    def get_entities(self):
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
        # with self.conn.cursor() as cur:
            cur.execute("SELECT * FROM products")
            return [dict(row) for row in cur]

    def find(self, id):
        with self.conn.cursor(cursor_factory=DictCursor) as cur:
            cur.execute("SELECT * FROM products WHERE id = %s", (id,))
            row = cur.fetchone()
            return dict(row) if row else None

    def save(self, product):
        if 'id' not in product or not product['id']:
            with self.conn.cursor(cursor_factory=DictCursor) as cur:
                cur.execute(
                    """INSERT INTO products (title, price) VALUES
                    (%s, %s) RETURNING id""",
                    (product['title'], product['price'])
                )
                id = cur.fetchone()[0]
                product['id'] = id
            self.conn.commit()
