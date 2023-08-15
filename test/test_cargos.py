import pytest
from src.ships import Cargo
def test_cargo1() -> None:
    #todoOk
    cargo1 = Cargo(1200, 500, 1, 0.5)
    assert cargo1.is_worth_it() >= 20
    #menor a 20
    cargo1.draft=0
    with pytest.raises(ValueError):
        cargo1.is_worth_it()
def test_cargo2() -> None:
    #todoOk
    cargo2 = Cargo(150, 25, 2, 0.25)
    assert cargo2.is_worth_it() >= 20
    #menor a 20
    cargo2.draft=10
    with pytest.raises(ValueError):
        cargo2.is_worth_it()
def test_cargo3() -> None:
    #todoOk
    cargo3 = Cargo(1000, 200, 10, 1)
    assert cargo3.is_worth_it() >= 20
    #menor a 20
    cargo3.draft=100
    with pytest.raises(ValueError):
        cargo3.is_worth_it()
    #valor invalido para calidad
    cargo3.draft=1000
    cargo3.quality=7
    with pytest.raises(ValueError):
        cargo3.is_worth_it()
