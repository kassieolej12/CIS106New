class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
    def discount_price(self):
        return self.sticker_price * 0.90
    def __str__(self):
        return (f"Car: {self.make} {self.model}\n"
                f"Sticker Price: ${self.sticker_price:,.2f}\n"
                f"Discount Price (90%): ${self.discount_price():,.2f}")
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = "N"
        self.sport_engine = "N"
        self.sport_interior = "N"
    def SportWheels(self, value):
        self.sport_wheels = value.upper()
    def SportEngine(self, value):
        self.sport_engine = value.upper()
    def SportInterior(self, value):
        self.sport_interior = value.upper()
    def price_with_options(self):
        price = self.discount_price()
        if self.sport_wheels == "Y":
            price += 1000.00
        if self.sport_engine == "Y":
            price += 3000.00
        if self.sport_interior == "Y":
            price += 2000.00
        return price
    def __str__(self):
        options = []
        if self.sport_wheels == "Y":
            options.append("Sport Wheels (+$1,000)")
        if self.sport_engine == "Y":
            options.append("Sport Engine (+$3,000)")
        if self.sport_interior == "Y":
            options.append("Sport Interior (+$2,000)")
        options_text = ", ".join(options) if options else "No Options"
        return (f"Sport Car: {self.make} {self.model}\n"
                f"Sticker Price: ${self.sticker_price:,.2f}\n"
                f"Discount Price (90%): ${self.discount_price():,.2f}\n"
                f"Options Selected: {options_text}\n"
                f"Price with Options: ${self.price_with_options():,.2f}")
def main():
    car = Car("Toyota", "Camry", 30000)
    print(car)
    print("\n" + "-" * 40 + "\n")
    sport_car = Sport("Ford", "Mustang", 50000)
    sport_car.SportWheels("Y")
    sport_car.SportEngine("Y")
    sport_car.SportInterior("N")
    print(sport_car)
if __name__ == "__main__":
    main()