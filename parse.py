import bs4
import json

class Parser:
    def __init__(self, source):
        self.source = source
        self.result = []

    def _return_product(self, tr):
        td = tr.td

        product = {}
        while td.find_next_sibling("td"):
            td = td.find_next_sibling("td")
            if len(product) != 0:
                product[next(reversed(product.keys())) + 1] = td.get_text().replace("\n", "").rstrip().lstrip()
            else:
                product[0] = td.get_text().replace("\n", "").rstrip().lstrip()

        return product

    def _read_file(self):
        contents = ""
        with open(self.source, 'r', encoding='utf-8') as f:

            contents = f.read()
        return contents

    def parse(self):
        soup = bs4.BeautifulSoup(self._read_file(), 'html.parser')

        tr = soup.find_all("tbody")[0].tr
        products_list = [self._return_product(tr)]

        while tr.find_next_sibling("tr"):
            tr = tr.find_next_sibling("tr")
            products_list.append(self._return_product(tr))

        titles = ["name", "proteins", "fat", "carbohydrates", "calories"]

        for product in products_list:
            for id in range(0, 5):
                product[titles[id]] = product.pop(id)

        result = []

        for product in products_list:
            product_dict = {titles[0]: product[titles[0]]}
            food_energy_dict = {}

            for key, value in product.items():
                if key != "name":
                    try:
                        food_energy_dict[key] = float(value)
                    except:
                        food_energy_dict[key] = 0.0

            product_dict["foodEnergy"] = food_energy_dict
            result.append(product_dict)

        self.result = result

        return self.result

    def save(self,file_path):
        with open(file_path, 'w', encoding='utf-8') as outfile:
            json.dump(self.result, outfile, ensure_ascii = False,  indent=4)
