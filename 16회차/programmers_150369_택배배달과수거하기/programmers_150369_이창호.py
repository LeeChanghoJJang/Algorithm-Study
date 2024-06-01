def solution(cap, n, deliveries, pickups):
    distance = 0
    delivery_demand = 0
    pickup_demand = 0

    for i in range(n - 1, -1, -1):
        delivery_demand += deliveries[i]
        pickup_demand += pickups[i]

        while delivery_demand > 0 or pickup_demand > 0:
            delivery_demand -= cap
            pickup_demand -= cap
            distance += (i + 1) * 2

    return distance
