from src.product import Product


class Category:
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
        """Строковое отображение категории с суммой всех штук товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список категории."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, использующий строковое отображение продуктов."""
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    @property
    def products_list(self) -> list[Product]:
        return self.__products
