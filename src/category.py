from abc import ABC, abstractmethod
from src.product import Product


class BaseOrderCategory(ABC):
    """Абстрактный класс для сущностей заказа и категорий товаров."""

    @abstractmethod
    def __str__(self) -> str:
        pass


class Category(BaseOrderCategory):
    """Класс для представления категории товаров."""

    name: str
    description: str
    __products: list[Product]

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product] = None) -> None:
        self.name = name
        self.description = description
        self.__products = []

        Category.category_count += 1

        if products is not None:
            for product in products:
                self.add_product(product)

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError("Добавлять в категорию можно только товары или их наследников!")
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    @property
    def products_list(self) -> list[Product]:
        return self.__products


class Order(BaseOrderCategory):
    """Класс для оформления заказа на один конкретный товар."""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("В заказ можно добавить только реальный товар или его наследника!")
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итоговая стоимость: {self.total_cost} руб."
