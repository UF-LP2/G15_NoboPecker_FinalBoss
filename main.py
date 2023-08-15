import csv
from src.ships import Ship
from src.ships import Cargo
from src.ships import Cruise
def convert_type(value) -> float:
  try:
    aux= float(value)
  except ValueError as e:
    print(e.args)
  else:
    if aux>=0:
      return aux
  raise ValueError("El valor ingresado no es valido")
def main() -> None:
  ships=[]
  with open("ships.csv") as file: #abro el archivo
    reader=csv.reader(file)
    next(file) #me salteo el titulo

    for row in reader: #recorro y voy guardando
      try:
        if row[2]=='' and row[3]=='': #ship
          aux1=convert_type(row[0])
          aux2=convert_type(row[1])
          ships.append(Ship(aux1,aux2))
        elif row[3]=='': #cruise
          aux1 = convert_type(row[0])
          aux2 = convert_type(row[1])
          aux3=convert_type(row[2])
          ships.append(Cruise(aux1,aux2,aux3))
        else: #cargo
          aux1 = convert_type(row[0])
          aux2 = convert_type(row[1])
          aux4=convert_type(row[3])
          if row[2]!='':
            aux3=convert_type(row[2])
          else:
            aux3=0.0
          ships.append(Cargo(aux1,aux2,aux3,aux4))
      except ValueError as e:
        print (e.args)

if __name__ == "__main__":
  main()

