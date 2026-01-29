class car:
    def __init__(self, model, color, for_sale, price):
        self.model = model
        self.color = color
        self.for_sale = for_sale
        self.price = price

    def drive(self):
        print(f"You vroom vroom in the {self.model}")

    def stop(self):
        print(f"You brakessssssssssssss in the {self.model}")

    def description(self):
        print(f"{self.model} {self.color} {self.price}")