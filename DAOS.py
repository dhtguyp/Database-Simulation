class Hats:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, hat):
        self._conn.execute("""INSERT INTO hats (id, topping, supplier, quantity) VALUES (?,?,?,?)""",
                           [hat.id, hat.topping, hat.supplier, hat.quantity])

    def get_topping_supplier_id(self, topping):
        c = self._conn.cursor()
        c.execute("""SELECT supplier FROM hats WHERE topping=?""", [topping])
        result = c.fetchone()
        return result[0]

    def get_hat_id(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""SELECT id FROM hats WHERE supplier=?""", [supplier_id])
        result = c.fetchone()
        return result[0]

    def decrease_quantity(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""SELECT quantity FROM hats WHERE supplier=?""", [supplier_id])
        row = c.fetchone()
        old_quantity = row[0]
        if old_quantity == 1:
            self._conn.execute("""DELETE FROM suppliers WHERE id=?""", [supplier_id])
        else:
            c.execute("""UPDATE hats SET quantity = quantity - 1 WHERE id=?""", [supplier_id])


class Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""INSERT INTO suppliers (id, name) VALUES (?, ?)""", [supplier.id, supplier.name])

    def get_sup_id(self, name):
        c = self._conn.cursor()
        c.execute("""SELECT * FROM suppliers WHERE name=?""", [name])
        result = c.fetchone()
        return result[0]

    def get_supplier_name(self, supplier_id):
        c = self._conn.cursor()
        c.execute("""SELECT name FROM suppliers WHERE id=?""", [supplier_id])
        result = c.fetchone()
        return result[0]


class Orders:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, order):
        self._conn.execute("""
               INSERT INTO orders (location, hat) VALUES (?, ?)
           """, [order.location, order.hat])
