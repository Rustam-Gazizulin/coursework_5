from abc import ABC, abstractmethod


class AbstractCar(ABC):
    @abstractmethod
    def delivery_by_land(self):
        pass


class AbstractShip(ABC):
    @abstractmethod
    def delivery_by_sea(self):
        pass


class AbstractTransportFactory(ABC):
    @abstractmethod
    def create_car(self) -> AbstractCar:
        pass

    @abstractmethod
    def create_ship(self) -> AbstractShip:
        pass


class TeslaX(AbstractCar):
    def delivery_by_land(self):
        print("Fast delivery")


class HeavyTruck(AbstractCar):
    def delivery_by_land(self):
        print("Slow delivery")


class RubberBoat(AbstractShip):
    def delivery_by_sea(self):
        print("Fast deliver sea")


class CargoShip(AbstractShip):
    def delivery_by_sea(self):
        print("Slow deliver sea")


class UsualTransportFactory(AbstractTransportFactory):
    def create_car(self) -> AbstractCar:
        return TeslaX()

    def create_ship(self) -> AbstractShip:
        return RubberBoat()


class CargoTransportFactory(AbstractTransportFactory):
    def create_car(self) -> AbstractCar:
        return HeavyTruck()

    def create_ship(self) -> AbstractShip:
        return CargoShip()


class Warehouse:
    factory: AbstractTransportFactory

    def __init__(self, factory: AbstractTransportFactory):
        self.factory = factory

    def deliver_with_ship(self):
        ship = self.factory.create_ship()
        ship.delivery_by_sea()

    def deliver_with_car(self):
        car = self.factory.create_car()
        car.delivery_by_land()


warehouse = Warehouse(factory=CargoTransportFactory())
warehouse.deliver_with_car()
warehouse.deliver_with_ship()

warehouse = Warehouse(factory=UsualTransportFactory())
#warehouse.deliver_with_car()
warehouse.deliver_with_ship()
