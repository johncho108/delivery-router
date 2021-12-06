import csv
from Package import Package

def load_package_data(filename, hash_table):
    with open(filename) as package_file:
        package_data = csv.reader(package_file, delimiter=",")
        next(package_data)
        for package in package_data:
            id = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zip = package[4]
            deadline = package[5]
            mass = int(package[6])
            notes = package[7]

            package_object = Package(id, address, city, state, zip, deadline, mass, notes)

            hash_table.insert(id, package_object)

def load_distance_data(filename, graph):
    with open(filename) as distance_file:
        distance_data = csv.reader(distance_file, delimiter=",")
        distance_data = list(distance_data)
        len_graph = len(distance_data)
        for i in range(1, len_graph):
            graph.add_vertex(distance_data[i][0])
        for i in range(1, len_graph):
            v1 = distance_data[i][0]
            for j in range(1, len_graph):
                v2 = distance_data[0][j]
                if distance_data[i][j] == 0:
                    graph.add_edge(v1, v2, 0)
                    break
                graph.add_edge(v1, v2, distance_data[i][j])
