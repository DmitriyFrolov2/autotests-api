class Car:
    def __init__(self, engine, wheels, color):
        self.engine = engine
        self.wheels = wheels
        self.color = color

class CarBuilder:
    def __init__(self):
        self.engine = None
        self.wheels = 4
        self.color = "white"

    def set_engine(self, engine):
        self.engine = engine
        return self

    def set_color(self, color):
        self.color = color
        return self

    def build(self):
        return Car(self.engine, self.wheels, self.color)

# Использование:
builder = CarBuilder()
car = builder.set_engine("V8").set_color("red").build()
