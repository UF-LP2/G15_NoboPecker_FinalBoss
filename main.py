import csv
from src.ships import Ship
from src.ships import Cargo
from src.ships import Cruise
def check_type(value) -> bool:
  if type(value) == int or type(value) == float:
    return True
  else:
    raise ValueError("El valor ingresado no es un numero")
def main() -> None:
  ships=[]
  with open("ships.csv") as file: #abro el archivo
    reader=csv.reader(file)
    next(file) #me salteo el titulo

    for row in reader: #recorro y voy guardando
      if row[2]=='' and row[3]=='':
        if check_type(row[0]) and check_type(row[1]):
          ships.append(Ship(row[0],row[1]))
      elif row[3]=='':
        if check_type(row[0]) and check_type(row[1]) and check_type(row[2]):
          ships.append(Cruise(row[0],row[1],row[2]))
      elif check_type(row[0]) and check_type(row[1]) and check_type(row[3]):
        if row[2]=='':
          aux=0
        elif check_type(row[2]):
          aux=row[2]
        ships.append(Cargo(row[0],row[1],aux,row[3]))


if __name__ == "__main__":
  main()

