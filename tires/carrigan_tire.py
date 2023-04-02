
from tires.tire import Tire



class CarriganTire(Tire):
    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values
        

    def needs_service(self):
        check_service_needed = False
        for i in self.tire_wear_values:
            if(i >= 0.9 ): check_service_needed = True
        
        return check_service_needed
