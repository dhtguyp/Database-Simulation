import atexit
import os
import sqlite3
import sys

import DAOS
import DTO


class Repository:
    def __init__(self):
        if not os.path.isfile(sys.argv[4]):
            with open(sys.argv[4], 'w') as _:
                pass
        self.conn = sqlite3.connect(sys.argv[4])
        self.hat_dao = DAOS.Hats(self.conn)
        self.supplier_dao = DAOS.Suppliers(self.conn)
        self.order_dao = DAOS.Orders(self.conn)

    def close(self):
        self.conn.commit()
        self.conn.close()

    def create_tables(self):
        self.conn.executescript("""
        CREATE TABLE IF NOT EXISTS hats (
            id INTEGER PRIMARY KEY,
            topping TEXT NOT NULL,
            supplier INTEGER REFERENCES suppliers(id),
            quantity INTEGER NOT NULL 
        );
            
        CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        );
        
        CREATE TABLE IF NOT EXISTS  orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            location TEXT NOT NULL,
            hat INTEGER REFERENCES hats(id)
        );
        """)

    def execute_order(self, location, topping):
        supplier_id = self.hat_dao.get_topping_supplier_id(topping)
        supplier_name = self.supplier_dao.get_supplier_name(supplier_id)
        hat_id = self.hat_dao.get_hat_id(topping, supplier_id)
        self.hat_dao.decrease_quantity(hat_id, supplier_id)
        self.create_order_record(location, hat_id)
        return topping, supplier_name, location

    def create_order_record(self, location, hat_id):
        self.order_dao.insert(DTO.Order(location, hat_id))


repo = Repository()
atexit.register(repo.close)
