from Algorithm import nearest_neighbor
from datetime import time, timedelta, datetime

# Truck object. The time complexity and space complexity for the deliver_packages method is described in Algorithm.py. See documentation "logic comments" for more information about the logic of this code.
class Truck:
    def __init__(self):
        self.packages = []
        self.mileage = 0
    
    def add_package(self, package):
        self.packages.append(package)

    def deliver_packages(self, graph, start_time, end_time):
        delivered = {}
        packages = self.packages
        total_delta = timedelta(0)
        current_time = start_time
        last_delivered_package = None
        deliveries_completed = False

        for package in packages:
            package.status = "En route"
        starting_package = nearest_neighbor("4001 South 700 East", packages, graph, delivered)
        distance = float(graph.edges["4001 South 700 East", starting_package.address])
        delta = timedelta(seconds=(distance/18)*3600)
        if current_time + delta > end_time:
            return (total_delta, self.mileage, last_delivered_package)
        last_delivered_package = starting_package
        delivered[last_delivered_package] = True
        current_time += delta
        current_time_str = current_time.strftime("%H:%M:%S")
        last_delivered_package.status = "Delivered at " + current_time_str 
        self.mileage += distance
        total_delta += delta
        
        while True:
            next_package = nearest_neighbor(last_delivered_package.address, packages, graph, delivered)
            if next_package == None:
                deliveries_completed = True
                break
            distance = float(graph.edges[last_delivered_package.address, next_package.address])
            delta = timedelta(seconds=(distance/18)*3600)
            if current_time + delta > end_time:
                break
            last_delivered_package = next_package
            delivered[last_delivered_package] = True
            current_time += delta
            current_time_str = current_time.strftime("%H:%M:%S")
            last_delivered_package.status = "Delivered at " + current_time_str 
            self.mileage += distance
            total_delta += delta

        return (total_delta, self.mileage, last_delivered_package, deliveries_completed)

            

