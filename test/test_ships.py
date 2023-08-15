import pytest
from src.ships import Ship
def test_calculateweight(self) -> None:
    barco= Ship(1200,500)
    assert barco.calculate_weight()== 450

