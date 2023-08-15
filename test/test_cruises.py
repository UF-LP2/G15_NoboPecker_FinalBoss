
import pytest
from src.ships import Cruise


def test_is_worth_it():
   #todo ok
   crucero1=Cruise(2100,600,90)
   crucero2=Cruise(500,100,83)
   crucero3=Cruise(300,56,20)
   assert crucero1.is_worth_it()==997.5
   assert crucero2.is_worth_it()==163.25
   assert crucero3.is_worth_it() == 171

#menor a 20
   crucero1.draft=-10
   crucero2.draft=15
   crucero3.draft=80

   with pytest.raises(ValueError):
      crucero1.is_worth_it()
   with pytest.raises(ValueError):
      crucero2.is_worth_it()
   with pytest.raises(ValueError):
      crucero3.is_worth_it()