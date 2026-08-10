class MobilePhone:
    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price

    def display_info(self):
        print(f"Name: {self.name}, Brand: {self.brand}, Price: ${self.price}")


m1 = MobilePhone("Sony Xperia 1 III", "Sony", 1199)
m2 = MobilePhone("Samsung Galaxy S21", "Samsung", 799)
m3 = MobilePhone ("iPhone 13 Pro", "Apple", 999)
mobiles = [m1, m2, m3]

for mobile in mobiles:
    mobile.display_info()

print(MobilePhone.count)