from abc import ABC
from array import array

class Tire(ABC):
    tire_wear_values = array('i', [0,0,0,0])
    def needs_service(self):
        pass
