import sqlite3

from model import ProductModel

class DB:
    def __init__(self, file='products.db') -> None:
        self.file = file
        self.tablename = 'products'


    def init_table(self):
        connection = sqlite3.connect(self.file)

        cursor = connection.cursor()
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {self.tablename} (
            id INTEGER PRIMARY KEY,
            shop TEXT NOT NULL,
            product_id INT UNIQUE,
            name TEXT NOT NULL,
            code TEXT NOT NULL,
            category_name TEXT NOT NULL,
            category_code TEXT NOT NULL,
            price INTEGER
            )
            ''')

        connection.commit()
        connection.close()


    def add_products(self, products: list[ProductModel], shop):
        connection = sqlite3.connect(self.file)
        cursor = connection.cursor()

        for p in products:
            cursor.execute(f'INSERT OR IGNORE INTO {self.tablename} (shop, product_id, name, code, category_name, category_code, price) VALUES (?, ?, ?, ?, ?, ?, ?)',
                        (shop, p.product_id, p.name, p.code, p.category,
                            p.category_code, p.price))

        connection.commit()
        connection.close()
