
from abc import ABC
from engine.nubbin_battery import NubbinBattery
from engine.model.Class.car import Car
from engine.willoughby_engine  import WilloughbyEngine

class Rorschach(WilloughbyEngine, NubbinBattery, Car, ABC):
    
    def needs_service(self):
        return Car.needs_service
