from ashan import AshanParser
from db import DB
from magnit import MagnitParser
from perekrestok import PerekrestokParser


if __name__ == '__main__':
    ashan = AshanParser(stockId=1)
    ashan_products = ashan.start()

    magnit = MagnitParser(stockId=773797)
    magnit_products = magnit.start()

    perekrestok = PerekrestokParser(stockId=400)
    prods = perekrestok.start()

    db1 = DB(file='prods.db')
    db1.init_table()
    db1.add_products(prods, shop='perekrestok')
    db1.add_products(magnit_products, shop='magnit')
    db1.add_products(ashan_products, shop='ashan')


