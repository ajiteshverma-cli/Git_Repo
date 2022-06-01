

def verticalOrder(trips, capacity_of_car):
    #as the total no of trips is till 1000, so we have an array with that limit
    length_of_trip = [0 for _ in range(1001)]

    for trip, pos_i, pos_j in trips:
        length_of_trip[pos_i] += trip # increament  when a pessanger is added
        length_of_trip[pos_j] -= trip # decrement when a pessanger is removed

    load_of_car = 0
    for i in range(len(length_of_trip)):
        load_of_car += length_of_trip[i]
        if load_of_car > capacity_of_car:
            return False
    return True


if __name__ == '__main__':
    trips = [[2,1,5],[3,3,7]]
    capacity = 4
    val = verticalOrder(trips, capacity)
    print(val)