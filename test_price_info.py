import price_info

def test_total_cost_shopping():
    result = price_info.total_cost_shopping('apple')

    assert (result == 6.0)

def test_cost_of_fruit():
    result = price_info.cost_of_fruits('apple', 10)

    assert (result == 12)
