class car:
    def __init__(self,model,brand,is_moving=True):
        self.model = model
        self.brand = brand
        self.is_moving = is_moving

    def drive(self):
        print(f'{self.brand},{self.model} is driving')

    def apply_brake(self):
        print(f"slowing down ={self.is_moving}")
    

class electriccar(car):
    def __init__(self,model,brand,battery_size,is_moving=True):
        super().__init__(model,brand)
        self.battery_size = battery_size
        self.is_moving = is_moving

    def charge(self):
        print(f'the {self.battery_size} kwh battery is charge')

my_car = car('toyota','vios')
my_car.drive()
ev_car= electriccar('tesla','model 3',75)
ev_car.drive()
ev_car.charge()
my_car.apply_brake()



    
        