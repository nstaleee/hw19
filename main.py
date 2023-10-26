class Car:
    car_instances = []

    def __init__(self, producer, brand, year=2020):
       self.producer = producer
       self.speedometr = 0
       self.brand = brand
       self.year = year
       with open("car_information.csv", "a") as csv_file:
           csv_file.write(f' {self.producer}; {self.brand}\n')

    def __str__(self):
        return f'Car {self.producer}'

    __repr__=__str__

class Sportcar(Car):
    def __init__(self, produser, brand, cost, year=2020):
        super().__init__(produser, brand, year)
        self.cost = cost

class Lorry(Car):
    def __init__(self, produser, brand, load_capacity, year=2020):
        super().__init__(produser, brand, year)
        self.load_capacity = load_capacity

carsport = Sportcar(produser='Lamborghini', brand='Lamborghini', cost=260000, year=2021)
reno = Lorry(produser='Reno', brand='reno', load_capacity=1200, year=2017)