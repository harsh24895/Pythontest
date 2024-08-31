# class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def printsku(self):
        print("the sku is {}".format(self.sku))


# class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def printGarmaent(self):
        print("the garment  is in section {} {}".format(self.section, self.type))


# child class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)  # initialing the attributes from parent class
        Garment.__init__(self, section, type)

    def printShirt(self):
        print("{} {} on the sale ".format(self.name, self.color))


Better = Shirts("123", "40", "shirt", "Better", "blue")

Better.printsku()
Better.printGarmaent()
Better.printShirt()