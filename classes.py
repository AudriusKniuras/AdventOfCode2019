class Car:
    def __init__(self, name):
        self.name = name
        
    def drive(self):
        return f"Driving a {self.name}"

class Audi(Car):
    def __init__(self, name, model):
        Car.__init__(self, name)
        self.model = model
    
    def get_model(self):
        return f"Model is {self.model}"

c = Audi("masina", "A8")

print(c.drive())
print(c.get_model())