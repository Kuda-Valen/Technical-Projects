import heapq
from data import missions, aisles, mission_id

def add_mission():
    global mission_id
    mission_id += 1

    priority = int(input("Enter priority [1-5]: "))

    while True:
        location = input("Enter location [A5]: ")
        if location in aisles:
            break
        print("Location Does not exist.")

    payload = input("Type of Load: ")
    status = "pending"

    index = aisles.index(location)
    battery = (index / len(aisles)) * 100

    mission_data = (priority, mission_id, location, payload, status, battery)
    heapq.heappush(missions, (priority, mission_data))