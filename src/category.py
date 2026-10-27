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

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в приватный список категории и обновляет счетчик уникальных товаров."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Геттер, возвращающий список товаров в виде строки по шаблону ТЗ."""
        result = ""
        for product in self.__products:
            result += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return result

    @property
    def products_list(self) -> list[Product]:
        """Вспомогательный геттер для тестов и внешних функций, чтобы получить сырой список объектов."""
        return self.__products
