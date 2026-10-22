#Вариант 1
class Building:
    className = 'Building'
    objectsCount = 0

    def __init__(self, area, price, residents):
        self._area = area
        self._price = price
        self._residents = residents
        Building.objectsCount = Building.objectsCount + 1

    def get_area(self):
        return self._area

    def set_area(self, area):
        if area > 0:
            self._area = area
        else:
            self._area = 1

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price > 0:
            self._price = price
        else:
            self._price = 1

    def get_residents(self):
        return self._residents

    def set_residents(self, residents):
        if residents > 0:
            self._residents = residents
        else:
            self._residents = 1

    def info(self):
        print(f'Площадь: {self._area} кв. м')
        print(f'Стоимость 1 кв м: {self._price}')
        print(f'Количество проживающих: {self._residents}')

    def totalCost(self):
        print(f'Общая стоимость: {self._area * self._price}')

    def __add__(self, other):
        if type(self) == type(other):
            return self._area + other._area
        else:
            print(f'Нельзя сложить объекты разных классов: {self.className} и {other.className}')
            return None

class VillageHouse(Building):
    className = 'VillageHouse'

    def __init__(self, area, price, residents, land_area):
        super().__init__(area, price, residents)
        self._land_area = land_area

    def set_land_area(self, land_area):
        if land_area > 0:
            self._land_area = land_area
        else:
            self._land_area = 1

    def info(self):
        super().info()
        print(f'Тип: {VillageHouse.className}')
        print(f'Площадь участка (соток): {self._land_area}')

    def costPerResident(self):
        print(f'Стоимость на одного проживающего: {self._area * self._price / self._residents}')

class CityHouse(Building):
    className = 'CityHouse'

    def __init__(self, area, price, residents, apartments):
        super().__init__(area, price, residents)
        self._apartments = apartments

    def set_apartments(self, apartments):
        if apartments > 0:
            self._apartments = apartments
        else:
            self._apartments = 1

    def info(self):
        super().info()
        print(f'Тип: {CityHouse.className}')
        print(f'Количество квартир: {self._apartments}')

    def costPerResident(self):
        print(f'Стоимость на одного проживающего: {self._area * self._price / self._residents}')


b = Building(100, 50000, 4)
b.info()
b.totalCost()

print('\n')

v = VillageHouse(80, 40000, 3, 10)
v2 = VillageHouse(120, 45000, 5, 15)
v.info()
v.totalCost()
v.costPerResident()

print('\n')

c = CityHouse(3000, 90000, 120, 60)
c.info()
c.totalCost()
c.costPerResident()

print('\n')

print(f'Суммарная площадь двух деревенских домов: {v + v2}')
result = v + c

print(f'Objects count: {Building.objectsCount}')
