milk_can_length = 5
milk_can_height = 2
milk_can_breadth = int(input("what is the breadth of the container: "))

def milk_can_volume():
    volume = milk_can_breadth * milk_can_length * milk_can_height
    return volume

print(milk_can_volume())