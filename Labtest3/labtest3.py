class Product:
    def __init__(self, partNo, description, quantity):
        self.partNo = partNo
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return "Product {0}: {1} ({2})".format(self.partNo, self.description, self.quantity)
    
class ProductList:
    def __init__(self):
        self.list = []

    def add(self, ProVar):
        self.list.append(ProVar)
    
    def getProducts(self):
        prodStr = ''
        i = 0
        for item in self.list:
            prodStr += "/ " + str(self.list[i]) + " "
            i += 1
        prodStr += "/"
        return prodStr

def test_Product():
    p = Product(123, 'Apple juice', 3)
    assert p.partNo == 123
    assert p.description == 'Apple juice'
    assert p.quantity == 3

def test_add_getProducts():
    pl = ProductList()
    pl.add(Product(301, 'Frying Pan', 10))
    pl.add(Product(101, 'Baby Ruth', 50))
    pl.add(Product(201, 'Pencil', 25))

    products = pl.getProducts()
    assert products == '/ Product 301: Frying Pan (10) / Product 101: Baby Ruth (50) / Product 201: Pencil (25) /'

def test_find():
    pl = ProductList()
    pl.add(Product(301, 'Frying Pan', 10))
    pl.add(Product(101, 'Baby Ruth', 50))
    pl.add(Product(201, 'Pencil', 25))

    p = pl.find(101)
    assert p != None
    assert p.partNo == 101
    assert p.description == 'Baby Ruth'

    p = pl.find(102)
    assert p == None

def test_getSorted():
    pl = ProductList()
    pl.add(Product(301, 'Frying Pan', 10))
    pl.add(Product(101, 'Baby Ruth', 50))
    pl.add(Product(201, 'Pencil', 25))

    products = pl.getSorted()
    assert products == '/ Product 301: Frying Pan (10) / Product 201: Pencil (25) / Product 101: Baby Ruth (50) /'