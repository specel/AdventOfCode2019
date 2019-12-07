input_data = open("aoc3-1.txt", "r")

first_wire_data=input_data.readline().split(",")
second_wire_data=input_data.readline().split(",")

directions = {"R":(1, 0),
 "L": (-1, 0),
 "U": (0, 1),
 "D": (0,-1)}



def create_wire(wire):
    x, y, count = 0, 0, 0
    wire_info = {}
    for item in wire:
        command = item[0]
        value = int(item[1:])
        offset = directions[command]
        for _ in range(value):
            x += offset[0] 
            y += offset[1] 
            count += 1
            wire_info[(x, y)] = count
    return wire_info

first_wire  = create_wire(first_wire_data)
second_wire  = create_wire(second_wire_data)
intersections = first_wire.keys() & second_wire.keys()
distances = [abs(point[0])+abs(point[1]) for point in intersections]
print(min(distances))

steps = [first_wire[intersection] + second_wire[intersection] for intersection in intersections]
print(min(steps))
None
    
    