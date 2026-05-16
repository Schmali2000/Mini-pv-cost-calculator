from main import annuity_factor, annualized_cost, levelized_cost


def test_annuity_factor():
    assert round(annuity_factor(0.05, 20),4) == 0.1


def test_annualized_cost():
    assert round(annualized_cost(10000, 0.05, 20, 200), 2) == 1002.43


def test_levelized_cost():
    assert round(levelized_cost(1000, 5000), 2) == 0.20
