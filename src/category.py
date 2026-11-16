from abc import ABC, abstractmethod
from src.product import Product


class ZeroQuantityError(Exception):
    """Пользовательское исключение при попытке добавить товар с нулевым количеством."""

    def __init__(self, message: str = "Товар с нулевым количеством не может быть добавлен") -> None:
        self.message = message
        super().__init__(self.message)


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
        """Добавляет продукт в категорию с полной обработкой исключений."""
        if not isinstance(product, Product):
            raise TypeError("Добавлять в категорию можно только товары или их наследников!")

        try:
            if product.quantity == 0:
                raise ZeroQuantityError()
        except ZeroQuantityError as e:
            print(e)
        else:
            self.__products.append(product)
            Category.product_count += 1
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self) -> float:
        """Подсчитывает средний ценник всех товаров категории."""
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

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

        try:
            if product.quantity == 0 or quantity == 0:
                raise ZeroQuantityError()
        except ZeroQuantityError as e:
            print(e)
            self.product = None
            self.quantity = 0
            self.total_cost = 0
        else:
            self.product = product
            self.quantity = quantity
            self.total_cost = product.price * quantity
            print("Товар успешно добавлен")
        finally:
            print("Обработка добавления товара завершена")

    def __str__(self) -> str:
        if self.product is None:
            return "Пустой или некорректный заказ"
        return f"Заказ: {self.product.name}, {self.quantity} шт. Итоговая стоимость: {self.total_cost} руб."
