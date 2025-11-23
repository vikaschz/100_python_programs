"""
Program: Elevator Simulation
Description: Simulate elevator requests and movement.

Hint:
- Track current floor and direction.

"""
# Elevator Simulation Program

current_floor = 0
print("Elevator starting at Floor", current_floor)

# Taking floor requests as input
requests = list(map(int, input("Enter floor requests (space separated): ").split()))

while requests:
    target = requests.pop(0)   # Take the first request

    print("\nNext target floor:", target)

    # Move UP
    if target > current_floor:
        while current_floor < target:
            current_floor += 1
            print("Moving UP to floor", current_floor)

    # Move DOWN
    elif target < current_floor:
        while current_floor > target:
            current_floor -= 1
            print("Moving DOWN to floor", current_floor)

    # When reached
    print(">> Stopped at floor", current_floor)

print("\nAll requests completed.")
