from pprint import pprint

class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category} '


class Shop:

    __file_name = 'products.txt'

    def get_products(self):
        try:
            file = open(self.__file_name, 'r')
            data = file.read()
            file.close()
            return data.splitlines()
        except FileNotFoundError:
            print('Файл не найден. Cоздайте файл и добавьте товары.')
            return []

    def add(self, *products):
        existing_products = self.get_products()
        file = open(self.__file_name, 'a')
        for product in products:
            product_str = str(product)
            if product_str in existing_products:
                print(f'\nПродукт {product} уже есть в магазине')

            else:
                file.write(f'{product}\n')

        file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

pprint(s1.get_products())



