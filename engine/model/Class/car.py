
from abc import ABC
from engine.model.Class.battery import Battery
from engine.model.Class.engine import Engine


class Car(Engine, Battery, ABC):   
    def __init__(self):
        self.engine_service_needed = Engine.needs_service
        self.battery_service_needed = Battery.needs_service
        
    def needs_service(self):
       return (self.engine_service_needed or self.battery_service_needed)
        
