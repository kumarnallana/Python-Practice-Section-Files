def calculate_inventory_value(price: int, quantity: int) -> int:
    return price * quantity


def test_calculate_inventory_value():
    result = calculate_inventory_value(100, 5)

    assert result == 500


print(test_calculate_inventory_value())


def add(a, b):
    return a + b


def test_calc():
    result = add(4, 5)
    assert result == 9
