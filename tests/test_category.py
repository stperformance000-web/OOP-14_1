import pytest
from src.category import Category
from src.product import Product
from src.utils import load_data_from_json


@pytest.fixture
def products_list():
    return [
        Product("Samsung Galaxy C23 Ultra", "256GB, Gray", 180000.0, 5),
        Product("Iphone 15 Pro", "128GB, Blue", 210000.50, 3)
    ]


def test_category_init(products_list):
    """Тест корректности инициализации объекта Category."""
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Смартфоны", "Электронные гаджеты", products_list)

    assert category.name == "Смартфоны"
    assert category.description == "Электронные гаджеты"
    assert len(category.products_list) == 2


def test_category_products_getter(products_list):
    """Тест геттера products, который возвращает строку по шаблону ТЗ."""
    category = Category("Смартфоны", "Гаджеты", products_list)
    expected_output = (
        "Samsung Galaxy C23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15 Pro, 210000.5 руб. Остаток: 3 шт.\n"
    )
    assert category.products == expected_output


def test_category_counters(products_list):
    """Тест подсчета количества категорий и количества продуктов."""
    Category.category_count = 0
    Category.product_count = 0

    Category("Смартфоны", "Гаджеты", products_list)
    assert Category.category_count == 1
    assert Category.product_count == 2

    Category("Аксессуары", "Чехлы и зарядки", [])
    assert Category.category_count == 2
    assert Category.product_count == 2


def test_load_data_from_json():
    """Тест корректности загрузки данных из оригинального JSON файла."""
    Category.category_count = 0
    Category.product_count = 0

    categories = load_data_from_json("products.json")

    assert len(categories) == 2
    assert categories[0].name == "Смартфоны"
    assert categories[1].name == "Телевизоры"

    assert len(categories[0].products_list) == 3
    assert len(categories[1].products_list) == 1
