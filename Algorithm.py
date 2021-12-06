def nearest_neighbor(current_address, packages, graph, visited):
    min_distance = float('inf')
    nearest = None
    for neighbor in packages:
        neighbor_address = neighbor.address
        neighbor_distance = float(graph.edges[current_address, neighbor_address])
        if neighbor not in visited and neighbor_distance < min_distance and neighbor.package_id != 9: 
            min_distance = neighbor_distance
            nearest = neighbor
    return nearest