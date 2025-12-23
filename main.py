class car:
    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def drive(self):
        print(f'{self.brand},{self.model} is driving')

my_car = car('toyota','vios')
my_car.drive()


class electriccar:
    def __init__(self,model,brand,battery_size):
        super().__init__(model)
        self.battery_size = battery_size

    def charge(self):
        print(f'the {self.battery_size}kwh battery is charge')

my_car = car('toyota','vios')
my_car.drive()
my_ev = electriccar('tesla','model 3',75)
my_ev.drive()
my_ev.charge()

    
        