from abc import ABC
from engine.model.Class.engine import Engine

class CapuletEngine(Engine, ABC):
    def __init__(self,current_mileage, last_service_mileage):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage
        self.service_criteria_mileage = 30000
    
    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > self.service_criteria_mileage
