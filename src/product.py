from typing import Self


class Product:
    """Класс для представления товара."""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self) -> str:
        """Строковое отображение продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Self) -> float:
        """Сложение двух продуктов (общая стоимость товаров на складе)."""
        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @classmethod
    def new_product(cls, product_data: dict, current_products: list = None) -> Self:
        """Создает объект Product из словаря. Если товар дублируется, объединяет их."""
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
