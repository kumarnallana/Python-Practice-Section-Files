from os import execlpe
from pathlib import Path
import json
products = [
    {
        "product_id": 1001,
        "product_name": "Laptop",
        "category": "Electronics",
        "price": 65000,
        "quantity": 8,
    },
    {
        "product_id": 1002,
        "product_name": "Keyboard",
        "category": "Electronics",
        "price": 2500,
        "quantity": 25,
    },
    {
        "product_id": 1003,
        "product_name": "Mouse",
        "category": "Electronics",
        "price": 1200,
        "quantity": 40,
    },
]


class JsonManager:
    def __init__(self, products_data: list[dict[str: str | int]]):
        self.products_data = products_data
        self.base_dir = Path(__file__).parent
        self.json_folder = self.base_dir / "json_data"
        self.json_folder.mkdir(parents=True, exist_ok=True)
        self.file_path: Path | None = None
        self.json_file = self.json_folder / "json_data.json"

    def write_data(self):
        try:

            with open(self.json_file, "w", encoding="utf-8") as file:
                json.dump(self.products_data, file, indent=4)

            return f"Json file:{self.json_file.name} has been created successfully"

        except Exception as e:
            return e

    def read_data(self):
        try:

            with open(self.json_file, "r", encoding="utf-8") as file:
                json.load(file)

        except Exception as e:
            return e

    def append_data(self, add_product: dict[str: str | int]):
        try:

            with open(self.json_file, "a", encoding="utf-8") as file:
                json.dump(add_product, file, indent=4)

            return f"Added product into the json : {add_product}"

        except Exception as e:
            return e

    def find_data(self, target_id: int):
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:
                product_dict_data = json.load(file)

                for product in product_dict_data:
                    if product["product_id"] == target_id:
                        return json.dumps(product, indent=4)

        except Exception as e:
            return e

    def update_quantity(self, target_id: int, new_quantity: int):
        try:
            with open(self.json_file, "r", encoding="utf-8") as file:

                product_db = json.load(file)

                for product in product_db:
                    if product.get("product_id") == target_id:
                        product["quantity"] = new_quantity

                        with open(self.json_file, "w", encoding="utf-8") as file:
                            json.dump(product_db, file, indent=4)

                        return json.dumps(product, indent=4)

                return f"Product with ID {target_id} not found."
        except Exception as e:
            return e


new_product: dict[str: str | int] = {
    "product_id": 1004,
    "product_name": "Mobile stand with cooling pad",
    "category": "Electronics",
    "price": 800,
    "quantity": 25,
}

if __name__ == "__main__":
    manager = JsonManager(products)
    # print(manager.write_data())

    # print(manager.append_data(new_product))

    # print(manager.find_data(1004))

    print(manager.update_quantity(1003, 500))
