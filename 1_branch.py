class Mashina:
    def __init__(self,madel,rang):
        self.madel=madel
        self.rang=rang

    def info(self):
        return f"madeli:{self.madel}, rangi:{self.rang}"


car=Mashina("Gentra","qora")
print(car.info())