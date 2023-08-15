import pytest
from src.ships import Cargo
def test_calculateweight() -> None:
    cargo1 = Cargo(1200, 500, 1, 0.5)
    cargo2 = Cargo(150, 25, 2, 0.25)
    cargo3 = Cargo(1000, 200, 10, 1)
    #with pytest.raises(ValueError):
    assert cargo1.calculate_weight() == 448
    assert cargo2.calculate_weight() == 111.5
    assert cargo3.calculate_weight() == 665



