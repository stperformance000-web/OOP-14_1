import pytest
from src.category import Category
from src.product import Product, Smartphone


@pytest.fixture
def products_list():
    return [
        Product("Samsung Galaxy C23 Ultra", "256GB, Gray", 180000.0, 5),
        Smartphone("iPhone 15", "Gray space", 210000.0, 8, 95.5, "15 Pro", 256, "Серый")
    ]


def test_category_init(products_list):
    category = Category("Электроника", "Гаджеты", products_list)
    assert category.name == "Электроника"
    assert len(category.products_list) == 2


def test_category_add_product_invalid():
    """Тест, что добавление не-продукта вызывает TypeError."""
    category = Category("Электроника", "Гаджеты", [])
    with pytest.raises(TypeError, match="Добавлять в категорию можно только товары или их наследников!"):
        category.add_product("Не товар, а просто строка")


def test_category_str(products_list):
    category = Category("Электроника", "Гаджеты", products_list)
    assert str(category) == "Электроника, количество продуктов: 13 шт."
