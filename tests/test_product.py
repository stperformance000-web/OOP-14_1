import pytest
from src.product import Product, Smartphone, LawnGrass


@pytest.fixture
def sample_smartphone():
    return Smartphone("iPhone 15", "Gray space", 210000.0, 8, 95.5, "15 Pro", 256, "Серый")


@pytest.fixture
def sample_grass():
    return LawnGrass("Газонная трава", "Элитная", 500.0, 20, "Россия", "14 дней", "Зеленый")


def test_smartphone_init(sample_smartphone):
    """Тест корректности инициализации объекта Smartphone."""
    assert sample_smartphone.name == "iPhone 15"
    assert sample_smartphone.efficiency == 95.5
    assert sample_smartphone.model == "15 Pro"
    assert sample_smartphone.memory == 256
    assert sample_smartphone.color == "Серый"


def test_grass_init(sample_grass):
    """Тест корректности инициализации объекта LawnGrass."""
    assert sample_grass.name == "Газонная трава"
    assert sample_grass.country == "Россия"
    assert sample_grass.germination_period == "14 дней"
    assert sample_grass.color == "Зеленый"


def test_products_add_same_class(sample_smartphone):
    """Тест сложения продуктов одинакового класса."""
    other_phone = Smartphone("iPhone 15", "Blue", 200000.0, 2, 95.5, "15 Pro", 256, "Синий")
    # (210000 * 8) + (200000 * 2) = 1680000 + 400000 = 2080000
    assert sample_smartphone + other_phone == 2080000.0


def test_products_add_different_classes(sample_smartphone, sample_grass):
    """Тест, что сложение разных классов вызывает TypeError."""
    with pytest.raises(TypeError, match="Можно складывать товары только одного класса!"):
        _ = sample_smartphone + sample_grass
