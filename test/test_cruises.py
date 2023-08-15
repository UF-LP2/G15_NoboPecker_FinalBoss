
import pytest
from src.ships import Cruise
def test_crucero_1():
   #todook
   crucero1 = Cruise(2100, 600, 90)
   assert crucero1.is_worth_it()>=20
   # menor a 20
   crucero1.draft = 10
   with pytest.raises(ValueError):
      crucero1.is_worth_it()
def test_crucero_2():
   crucero2 = Cruise(500, 100, 83)
   assert crucero2.is_worth_it() >=20
   crucero2.draft = 15
   with pytest.raises(ValueError):
      crucero2.is_worth_it()
def test_crucero_3():
   crucero3=Cruise(300,56,20)
   assert crucero3.is_worth_it()>=20
   crucero3.draft=8
   with pytest.raises(ValueError):
      crucero3.is_worth_it()

