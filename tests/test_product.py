import pytest
from src.product import Product


@pytest.fixture
def sample_product():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Gray", 180000.0, 5)


def test_product_init(sample_product):
    """Тест корректности инициализации объекта Product."""
    assert sample_product.name == "Samsung Galaxy C23 Ultra"
    assert sample_product.description == "256GB, Gray"
    assert sample_product.price == 180000.0
    assert sample_product.quantity == 5


def test_product_price_setter(sample_product):
    """Тест изменения цены через сеттер (положительная цена)."""
    sample_product.price = 200000.0
    assert sample_product.price == 200000.0


def test_product_price_setter_invalid(sample_product, capsys):
    """Тест сеттера при попытке установить нулевую или отрицательную цену."""
    sample_product.price = -100.0
    assert sample_product.price == 180000.0  # Цена не изменилась
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_classmethod():
    """Тест создания продукта через класс-метод new_product."""
    product_data = {
        "name": "Iphone 15 Pro",
        "description": "128GB, Blue",
        "price": 210000.50,
        "quantity": 3
    }
    product = Product.new_product(product_data)
    assert product.name == "Iphone 15 Pro"
    assert product.price == 210000.50
    assert product.quantity == 3


def test_new_product_duplicate_handling():
    """Тест объединения дубликатов товаров с выбором максимальной цены."""
    product_data_1 = {"name": "Test Phone", "description": "Desc", "price": 100.0, "quantity": 2}
    product_data_2 = {"name": "Test Phone", "description": "Desc", "price": 150.0, "quantity": 3}

    p1 = Product.new_product(product_data_1)
    current_products = [p1]

    # Создаем дубликат, передавая список текущих товаров
    p2 = Product.new_product(product_data_2, current_products)

    assert p2.quantity == 5  # 2 + 3
    assert p2.price == 150.0  # max(100.0, 150.0)
