class Car:
    def __init__(self, model_name, mileage, manufacture):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        print(f"{self.model_name}の燃費は{self.mileage}です")

    def brakes(self):
        print(f"{self.manufacture}社の{self.model_name}はブレーキを掛けました！")


if __name__ == "__main__":
    Aqua = Car("Aqua", 32, "Toyota")
    Mazda3 = Car("Mazda3", 20, "Mazda")
    Fit = Car("Fit", 27, "Honda")

    print(Fit.manufacture)

    Mazda3.gas()
    Mazda3.brakes()

    Aqua.brakes()
    Aqua.gas()