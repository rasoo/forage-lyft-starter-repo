from abc import ABC
from engine.capulet_engine import CapuletEngine
from engine.model.Class.car import Car
from engine.splinder_battery  import SplinderBattery

class Calliope(CapuletEngine, SplinderBattery, Car, ABC):
    
    def needs_service(self):
        return Car.needs_service
