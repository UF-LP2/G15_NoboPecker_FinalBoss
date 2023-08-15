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
          aux_draft=convert_type(row[0])
          aux_crew=convert_type(row[1])
          ships.append(Ship(aux_draft,aux_crew))
        elif row[3]=='': #cruise
          aux_draft = convert_type(row[0])
          aux_crew = convert_type(row[1])
          aux_passengers=convert_type(row[2])
          ships.append(Cruise(aux_draft,aux_crew,aux_passengers))
        else: #cargo
          aux_draft = convert_type(row[0])
          aux_crew = convert_type(row[1])
          aux_quality=convert_type(row[3])
          if row[2]!='':
            aux_cargo=convert_type(row[2])
          else:
            aux_cargo=0.0
          ships.append(Cargo(aux_draft,aux_crew,aux_cargo,aux_quality))
      except ValueError as e:
        print (e.args)

if __name__ == "__main__":
  main()

