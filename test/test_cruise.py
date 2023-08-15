
import pytest
from src.ships import Cruise


def test_calculateweight():
    crucero = Cruise(1200, 50, 100)
    crucero2 = Cruise(2100, 200, 65)

    assert crucero.calculate_weight() == 900
    assert crucero2.calculate_weight()==1653.75
