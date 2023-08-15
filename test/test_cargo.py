import pytest
from src.ships import Cargo
def test_is_worth_it() -> None:
    #todoOk
    cargo1 = Cargo(1200, 500, 1, 0.5)
    cargo2 = Cargo(150, 25, 2, 0.25)
    cargo3 = Cargo(1000, 200, 10, 1)
    assert cargo1.is_worth_it() == 448
    assert cargo2.is_worth_it() == 111.5
    assert cargo3.is_worth_it() == 665

    #menor a 20
    cargo1.draft=0
    cargo2.draft=10
    cargo3.draft=100
    with pytest.raises(ValueError):
        cargo1.is_worth_it()
    with pytest.raises(ValueError):
        cargo2.is_worth_it()
    with pytest.raises(ValueError):
        cargo3.is_worth_it()

def test_constructor() -> None:






