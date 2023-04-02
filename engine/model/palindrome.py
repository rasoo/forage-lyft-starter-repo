
from abc import ABC
from engine.splinder_battery import SplinderBattery
from engine.model.Class.car import Car
from engine.sternman_engine  import SternmanEngine

class Palindrome(SternmanEngine, SplinderBattery, Car, ABC):
    
    def needs_service(self):
        return Car.needs_service
