from abc import ABC
from datetime import datetime

from engine.model.Class.battery import Battery

class NubbinBattery(Battery, ABC):
    def __init__(self,last_service_date):
        self.last_service_date = last_service_date
        self.srevice_criteria_years = 4
    
    def needs_service(self):
        diff = (datetime.today().date() - self.last_service_date)
        return diff.year > self.srevice_criteria_years