class Product(object):
    def _init_(price, name, weight, brand, status):
        self.price = price
        self.tax = tax
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = status
        self.display_all()

    def Return(self, reason):
        if reason == "defective":
            self.status = "defective"
            self.price = 0
        elif reason == "still in box":
            self.status = "for sale"
        else:
            self.status = "used"
            

