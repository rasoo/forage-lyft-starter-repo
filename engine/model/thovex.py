from abc import ABC
from engine.nubbin_battery import NubbinBattery
from engine.model.Class.car import Car
from engine.capulet_engine  import CapuletEngine

class Thovex(CapuletEngine, NubbinBattery, Car, ABC):
    
    def needs_service(self):
        return Car.needs_service
