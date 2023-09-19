from collections import deque

pumps = deque()
number_of_pumps = int(input())
for _ in range(number_of_pumps):
    pumps.append([int(x) for x in input().split()])

total_distance = 0
for i in range(len(pumps)):
    total_distance += pumps[i][1]
number_of_pumps = len(pumps)
start_pump_index = 0
fuel_left = 0
for pump_index in range(number_of_pumps):
    fuel, distance = pumps[0]
    if fuel + fuel_left >= distance:
        start_pump_index = pump_index
        fuel_left += fuel - distance
        total_distance -= distance
        if total_distance > 0:
            pumps.rotate(-1)
    else:
        start_pump_index = 0
        pumps.rotate(-1)

print(start_pump_index)
print(total_distance)
print(pumps)