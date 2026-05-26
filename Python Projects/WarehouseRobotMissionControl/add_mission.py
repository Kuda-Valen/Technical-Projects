import heapq

# aisle locations
aisles = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "E1", "E2", "E3", "E4", "E5", "E6", "E6", "E7", "E8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8")



def add_mission():
    global missions
    global mission_id
    
    mission_id += 1
    priority = int(input("Enter priority [1-5] 1 being heighest priority: "))
    try:
        location = input("Enter location of mission e.g.[A5]: ")
        if not location in aisles:
            print("Location not found in aisles")
        elif location in aisles:
            location = location
        
    except ValueError:
        print("Invalid input")

    payload = input("Type of Load [Electronic, Furniture, Plastic]")
    status = input("Enter the status [pending, successful, failed]")

    a = 0
    while a < len(aisles):
        if aisles[a] == location:
            break
        else:
            a += 1
            
    if a < len(aisles):
        b = a/len(aisles)
        battery = b*100
    else:
        battery = 0

    mission_data = (priority ,mission_id, location, payload, status, battery)
    heapq.heappush(missions, (priority, mission_data))
    
