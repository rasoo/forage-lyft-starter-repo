
from tires.tire import Tire



class OctopianTire(Tire):
    def __init__(self, tire_wear_values):
        self.tire_wear_values = tire_wear_values
        

    def needs_service(self):
        check_service_needed = False
        sum_all_tire_wear = 0
        for i in self.tire_wear_values:
            sum_all_tire_wear = sum_all_tire_wear + i
        
        if(sum_all_tire_wear >= 3):
                check_service_needed = True
        
        return check_service_needed
