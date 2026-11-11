import pytest
from src.category import Category, Order
from src.product import Product
from src.utils import load_data_from_json


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy", "256GB", 180000.0, 5)


def test_category_init(sample_product):
    Category.category_count = 0
    Category.product_count = 0
    category = Category("Смартфоны", "Гаджеты", [sample_product])
    assert category.name == "Смартфоны"
    assert len(category.products_list) == 1
    assert "Samsung Galaxy" in category.products
    assert str(category) == "Смартфоны, количество продуктов: 5 шт."


def test_category_add_invalid():
    category = Category("Тест", "Описание", [])
    with pytest.raises(TypeError):
        category.add_product("Не продукт")


def test_order_creation(sample_product):
    order = Order(sample_product, 2)
    assert order.product.name == "Samsung Galaxy"
    assert order.total_cost == 360000.0
    assert str(order) == "Заказ: Samsung Galaxy, 2 шт. Итоговая стоимость: 360000.0 руб."


def test_order_creation_invalid():
    with pytest.raises(TypeError):
        _ = Order("Строка вместо объекта", 5)


def test_load_data_from_json():
    Category.category_count = 0
    Category.product_count = 0
    categories = load_data_from_json("products.json")
    assert len(categories) > 0

    # Проверка на несуществующий файл
    assert load_data_from_json("missing.json") == []
