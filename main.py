class car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def drive(self):
        print(f'{self.brand},{self.model} is driving')

my_car = car('toyota','vios')
my_car.drive()