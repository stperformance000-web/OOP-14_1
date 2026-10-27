import json
import os
from src.category import Category
from src.product import Product


def load_data_from_json(file_path: str) -> list[Category]:
    """Загружает данные из JSON файла с использованием защищенных методов."""
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    categories = []
    for category_data in data:
        products = []
        for product_data in category_data.get("products", []):
            # Создаем продукт через класс-метод
            product = Product.new_product(product_data)
            products.append(product)

        category = Category(
            name=category_data["name"],
            description=category_data["description"],
            products=products
        )
        categories.append(category)

    return categories
