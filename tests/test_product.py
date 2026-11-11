import pytest
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone 15", "Gray", 210000.0, 8, 95.5, "15 Pro", 256, "Серый")


@pytest.fixture
def sample_grass():
    return LawnGrass("Газонная трава", "Элитная", 500.0, 20, "Россия", "14 дней", "Зеленый")


def test_product_init():
    product = Product("Samsung Galaxy", "256GB", 180000.0, 5)
    assert product.name == "Samsung Galaxy"
    assert str(product) == "Samsung Galaxy, 180000.0 руб. Остаток: 5 шт."


def test_smartphone_init(sample_smartphone):
    assert sample_smartphone.name == "iPhone 15"
    assert sample_smartphone.model == "15 Pro"
    assert sample_smartphone.memory == 256


def test_grass_init(sample_grass):
    assert sample_grass.name == "Газонная трава"
    assert sample_grass.country == "Россия"


def test_product_add(sample_smartphone):
    other_phone = Smartphone("iPhone 15", "Blue", 200000.0, 2, 95.5, "15 Pro", 256, "Синий")
    assert sample_smartphone + other_phone == 2080000.0


def test_product_add_type_error(sample_smartphone, sample_grass):
    with pytest.raises(TypeError):
        _ = sample_smartphone + sample_grass


def test_product_price_setter():
    product = Product("Test", "Desc", 100.0, 5)
    product.price = 150.0
    assert product.price == 150.0

    product.price = -10.0
    assert product.price == 150.0


def test_mixin_log_output(capsys):
    _ = Product("Тестовый Товар", "Описание", 500.0, 10)
    captured = capsys.readouterr()
    assert "Product" in captured.out
