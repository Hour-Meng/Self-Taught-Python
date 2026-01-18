class Car:
    def __init__(self, model, year, engine, color):
        self.model = model
        self.year = year
        self.engine = engine
        self.color = color
    def driving(self):
        print("The car is driving")
    def stop(self):
        print("The car is stopped")