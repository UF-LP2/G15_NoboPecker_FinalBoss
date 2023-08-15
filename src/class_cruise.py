from class_ship import ship

class cruise(ship):
    passengersWeight=2.25
    def __init__(self, passengers, draft, crew):
        self.passengers = passengers

    def calculate_weight(self):
        weight=self.draft-self.crew*ship.crewWeight-self.passengers*self.passengersWeight
        return weight