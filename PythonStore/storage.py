import json
from pathlib import Path

from product import Product


class ProductStorage:
    """يقرأ المنتجات من ملف JSON ويحفظها فيه."""

    def __init__(self, file_path=None):
        if file_path is None:
            file_path = Path(__file__).with_name("products.json")
        self.file_path = Path(file_path)

    def load_products(self):
        if not self.file_path.exists():
            return []

        with self.file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            raise ValueError("يجب أن يحتوي ملف المنتجات على قائمة JSON.")
        return [Product.from_dict(item) for item in data]

    def save_products(self, products):
        data = [product.to_dict() for product in products]
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
