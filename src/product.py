from abc import ABC, abstractmethod
from typing import Self


class MixinLog:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args, **kwargs) -> None:
        # Передаем управление дальше по цепочке MRO
        super().__init__(*args, **kwargs)
        # Выводим информацию о созданном объекте в консоль
        print(f"{self.__class__.__name__}({', '.join([repr(v) for v in args])})")


class BaseProduct(ABC):
    """Базовый абстрактный класс для всех продуктов."""

    @abstractmethod
    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Self) -> float:
        pass


class Product(MixinLog, BaseProduct):
    """Класс для представления стандартного товара."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        # Инициализируем миксин
        super().__init__(name, description, price, quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Self) -> float:
        if type(self) is not type(other):
            raise TypeError("Можно складывать товары только одного класса!")
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict, current_products: list = None) -> Self:
        name = product_data["name"]
        description = product_data["description"]
        price = product_data["price"]
        quantity = product_data["quantity"]

        if current_products is not None:
            for existing_product in current_products:
                if existing_product.name == name:
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    return existing_product

        return cls(name, description, price, quantity)

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            user_answer = input(f"Вы уверены, что хотите снизить цену товара с {self.__price} до {new_price}? (y/n): ")
            if user_answer.lower() != 'y':
                print("Снижение цены отменено.")
                return

        self.__price = new_price


class Smartphone(Product):
    """Класс-наследник для смартфонов. Наследуется строго от Product."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        efficiency: float, model: str, memory: int, color: str
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """Класс-наследник для газонной травы. Наследуется строго от Product."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int,
        country: str, germination_period: str, color: str
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
