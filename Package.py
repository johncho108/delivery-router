from datetime import datetime

class Package:
    def __init__(self, package_id, address, city, state, zip, deadline, mass, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.mass = mass
        if notes == "":
            self.notes = "[N/A]"
        else:
            self.notes = notes
        self.status = "At the hub"

    def get_time_delivered(self):
        status = self.status
        if ("Delivered" in status):
            "Delivered at HH:MM:SS"
            hour = int(status[13:15])
            minute = int(status[16:18])
            second = int(status[19:21])
        return datetime(2021,11,1,hour,minute,second)

    def __str__(self):
        return f"Package ID: {self.package_id}, Address: {self.address}, City: {self.city}, State: {self.state}, Zip: {self.zip}, Deadline: {self.deadline}, Mass: {self.mass}, Notes: {self.notes}, Status: {self.status}."
    
