
import pytest
from src.class_cruise import cruise
from src.class_ship import ship


def test_calculateweight():
    crucero = cruise(1200, 50, 100)
    crucero2 = cruise(2100, 200, 65)

    assert crucero.calculate_weight() == 900
    assert crucero2.calculate_weight()==1653.75
