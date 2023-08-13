from class_ship import ship

class cruise(ship):
    def __init__(self, passengers, draft, crew):
        self.passengers = passengers

    def calculate_weight(self):
        weight=self.draft-self.crew*1.5-self.passengers*2.25
        return weight