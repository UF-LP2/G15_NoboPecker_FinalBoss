import csv
from src.ships import Ship
from src.ships import Cargo
from src.ships import Cruise

def main() -> None:
  ships=[]
  with open("ships.csv") as file: #abro el archivo
    reader=csv.reader(file)
    next(file) #me salteo el titulo

    for row in reader: #recorro y voy guardando
      try:
        if row[2]=='' and row[3]=='': #ship
          aux_draft=Ship.convert_type(row[0])
          aux_crew=Ship.convert_type(row[1])
          ships.append(Ship(aux_draft,aux_crew))
        elif row[3]=='': #cruise
          aux_draft = Ship.convert_type(row[0])
          aux_crew = Ship.convert_type(row[1])
          aux_passengers=Ship.convert_type(row[2])
          ships.append(Cruise(aux_passengers,aux_draft,aux_crew))
        else: #cargo
          aux_draft = Ship.convert_type(row[0])
          aux_crew = Ship.convert_type(row[1])
          aux_quality=Ship.convert_type(row[3])
          if row[2]!='':
            aux_cargo=Ship.convert_type(row[2])
          else:
            aux_cargo=0.0
          ships.append(Cargo(aux_cargo,aux_quality,aux_draft,aux_crew))
      except ValueError as e:
        print (e.args)
if __name__ == "__main__":
  main()

