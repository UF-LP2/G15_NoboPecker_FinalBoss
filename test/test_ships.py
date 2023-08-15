import pytest
from src.ships import Ship
def test_barco_1():
    barco1=Ship(122,56)
    #todo ok
    assert barco1.is_worth_it()>=20
    #menor a 20
    barco1.draft=10
    with pytest.raises(ValueError):
        barco1.is_worth_it()
def test_barco_2():
    barco2=Ship(500,120)
    #todo ok
    assert barco2.is_worth_it()>=20
    #menor a 20
    barco2.draft=30
    with pytest.raises(ValueError):
        barco2.is_worth_it()

def test_barco_3():
    barco3=Ship(900,600)
    #todo ok
    assert barco3.is_worth_it()>=20
    #menor a 20
    barco3.draft=500
    with pytest.raises(ValueError):
        barco3.is_worth_it()

