import psycopg2
from psycopg2.extras import DictCursor


def get_order_sum(conn, month):
    conn = psycopg2.connect('postgresql://user:secret@localhost:5432/hexlet')
    template = "Покупатель {customer} совершил покупок на сумму {total}".format
    with conn.cursor(cursor_factory=DictCursor) as cur:
        query = """
            SELECT
                customers.customer_name AS name,
                SUM(orders.total_amount) AS total
            FROM
                customers
            LEFT JOIN
                orders ON customers.customer_id = orders.customer_id
            WHERE
                EXTRACT(MONTH FROM orders.order_date) = %s
            GROUP BY
                customers.customer_name;"""
        month_formated = '{:02d}'.format(month)
        cur.execute(query, (month_formated,))
        result = []
        for row in cur:
            customer_name = row['name']
            total = row['total']
            result.append(template(customer=customer_name, total=total))
    conn.commit()
    return '\n'.join(result)
