class Catalogue:

    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        return [item for item in self.products if item.startswith(first_letter)]

    def __repr__(self):
        string_output = f"Items in the {self.name} catalogue:\n"
        string_output += '\n'.join(sorted(self.products))
        return string_output


catalogue = Catalogue('TASHAK')
catalogue.add_product('putka s kosam')
catalogue.add_product('mamka mu')
catalogue.add_product('Shi ta prusna liolio uu Yea')
catalogue.add_product('vdigai telefona putko')
# print(catalogue.get_by_letter('p'))
print(catalogue.__repr__())