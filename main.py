from Hash import ChainingHashTable
from CSV import load_package_data, load_distance_data
from Truck import Truck
from Graph import Graph
from datetime import datetime, timedelta

print("\nWelcome!\n")
while True:
    user_input = input("Please enter a time after 0800 (in military time, e.g. 0912 or 1701) to check the status of all packages OR enter 'X' to exit:\n\nEnter time here (or 'X' for exit): ")
    if user_input == "X": 
        break
    elif len(user_input) != 4:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\nERROR: Invalid input.\n")
        continue
    invalid_char = False
    for char in user_input:
        if char not in "0123456789":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\nERROR: Invalid input.\n")
            invalid_char = True
            continue
    if invalid_char == True:
        continue
    hours = int(user_input[:2])
    minutes = int(user_input[2:])
    if hours < 8 or hours > 23:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\nERROR: Invalid input.\n")
        continue
    if minutes > 59:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\nERROR: Invalid input.\n")
        continue
    
    packages_ht = ChainingHashTable()
    load_package_data("package_file.csv", packages_ht)

    truck_1 = Truck()
    truck_2 = Truck()
    truck_3 = Truck()
    for key in packages_ht.table:
        for key_value_pair in key:
            package = key_value_pair[1]
            if package.package_id == 19:
                truck_1.add_package(package)
            elif "Can" in package.notes or "Delayed" in package.notes or "Wrong" in package.notes or package.package_id == 33 or package.package_id == 4:
                truck_2.add_package(package)
            elif package.deadline == "EOD":
                truck_3.add_package(package)
            else:
                truck_1.add_package(package)

    distances_graph = Graph()
    load_distance_data("distance_file.csv", distances_graph)

    total_mileage = 0
    total_timedelta = timedelta(0)
    end_time = datetime(2021, 11, 1, hours, minutes)
    last_delivered_package1 = last_delivered_package2 = last_delivered_package3 = deliveries_completed1 = deliveries_completed2 = deliveries_completed3 = None

    truck_1_clock = datetime(2021, 11, 1, 8, 0)
    if truck_1_clock < end_time:
        timedelta1, mileage1, last_delivered_package1, deliveries_completed1= truck_1.deliver_packages(distances_graph, truck_1_clock, end_time)
        truck_1_clock += timedelta1
        total_mileage += mileage1

    if deliveries_completed1 and truck_1_clock < end_time:
        dist_to_hub = float(distances_graph.edges[last_delivered_package1.address, "4001 South 700 East"])
        time_to_hub = timedelta(seconds=(dist_to_hub/18)*3600)
        if truck_1_clock + time_to_hub <= end_time:
            truck_1_clock += time_to_hub
            total_mileage += dist_to_hub

    truck_3_clock = truck_1_clock
    if deliveries_completed1 and truck_3_clock < end_time:
        timedelta3, mileage3, last_delivered_package3, deliveries_completed3 = truck_3.deliver_packages(distances_graph, truck_3_clock, end_time)
        truck_3_clock += timedelta3
        total_mileage += mileage3

    truck_2_clock = datetime(2021, 11, 1, 9, 5)
    if truck_2_clock < end_time:
        timedelta2, mileage2, last_delivered_package2, deliveries_completed2 = truck_2.deliver_packages(distances_graph, truck_2_clock, end_time)
        truck_2_clock += timedelta2
        total_mileage += mileage2

    if deliveries_completed2:
        truck_2_clock = max(datetime(2021, 11, 1, 10, 20),last_delivered_package2.get_time_delivered())
        if truck_2_clock < end_time:
            package9 = packages_ht.lookup(9)
            new_package9_address = "410 S State St"
            package9.address = new_package9_address
            dist_to_package9 = float(distances_graph.edges[last_delivered_package2.address, new_package9_address])
            time_to_package9 = timedelta(seconds=(dist_to_package9/18)*3600)
            if truck_2_clock + time_to_package9 <= end_time:
                truck_2_clock += time_to_package9
                total_mileage += dist_to_package9
                truck_2_clock_str = truck_2_clock.strftime("%H:%M:%S")
                package9.status = truck_2_clock_str + " delivered"

    print("\n--------------------------------------------------------------------\n")
    print(f"Total miles driven by all trucks: {round(total_mileage, 2)}")
    print("\n---------------------Packages By Truck-------------------------\n")
    print("Truck 1")
    for package in truck_1.packages:
        print(package)
    print(" ")
    print("Truck 2")
    for package in truck_2.packages:
        print(package)
    print(" ")
    print("Truck 3")
    for package in truck_3.packages:
        print(package)
    print(" ")












