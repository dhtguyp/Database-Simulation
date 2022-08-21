class Hat:
    def __init__(self, _id, _topping, _supplier_id, _quantity):
        self.id = _id
        self.topping = _topping
        self.supplier = _supplier_id
        self.quantity = _quantity


class Supplier:
    def __init__(self, _id, _name):
        self.id = _id
        self.name = _name


class Order:
    def __init__(self, _location, _hat_id):
        self.location = _location
        self.hat = _hat_id
