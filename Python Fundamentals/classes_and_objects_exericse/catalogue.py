class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        new_list = []
        for product in self.products:
            if product[0] == first_letter:
                new_list.append(product)
        return new_list

    def __repr__(self):
        self.products.sort()
        results = f"Items in the {self.name} catalogue:\n"
        for product in self.products:
            results += product + "\n"

        return results

catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
