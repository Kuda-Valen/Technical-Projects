
import heapq

mission_id = 0
missions = []
completed_missions = []


# aisle locations
aisles = ("A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8", "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8", "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "E1", "E2", "E3", "E4", "E5", "E6", "E6", "E7", "E8", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8")



def add_mission():
    global missions
    global mission_id
    
    mission_id += 1
    priority = int(input("Enter priority [1-5] 1 being heighest priority: "))
    found = 0
    while found != 1:
        try:
            location = input("Enter location of mission e.g.[A5]: ")
            if not location in aisles:
                print("Location not found in aisles")
                found = 0
                
            elif location in aisles:
                location = location
                found = 1
        
        except ValueError:
            print("Invalid input")

    payload = input("Type of Load [Electronic, Furniture, Plastic]")
    status = "pending"

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
    
def battery (a):
    charged = 100
    percent = True

    left = charged - a

    if left < 0:
        percent = True
    else:
        percent = False

    return percent


# Processing of the information which is mission execution
def execute():
    global percent
    global completed_missions
    global missions
    global percent

    # We need to take tasks according to their priority in the priority list
    priority, mission_data = heapq.heappop(missions)
    print(f"\nWe have accessed {mission_data[1]}, with the priority: {priority}")

    # check battery
    battery(mission_data[5])
    if percent == True:
        pass
    else:
        print("\nCannot continue mission because insuficient battery")
        new_priority = 1
        unfinished = (mission_data[0], mission_data[1], mission_data[2], mission_data[3], "Retry", mission_data[5])
        heapq.heappush(missions, (new_priority, unfinished))
        print(f"\nMission {mission_data[1]}, located in {mission_data[2]} has been readded to missions list.")
    
    # User input
    finish = input("\nWas the Mission finished [Y/N]: ").lower()
    
    if finish.lower() == 'y':
        finished = (mission_data[0], mission_data[1], mission_data[2], mission_data[3], "Completed", mission_data[5])
        completed_missions.append(finished)
        print(f"\nMission {mission_data[1]}, located in {mission_data[2]} has been added to completed stack")

    else:
        new_priority = 1
        unfinished = (mission_data[0], mission_data[1], mission_data[2], mission_data[3], "Retry", mission_data[5])
        heapq.heappush(missions, (new_priority, unfinished))
        print(f"\nMission {mission_data[1]}, located in {mission_data[2]} has been readded to missions list.")
    



def view_completed ():
    global completed_missions

    if not completed_missions:
        print("\nThere is no completed missions")
    
    else:
        for t in completed_missions: 
            print(t)


def view_mission():
    global missions

    if not missions:
        print("no missions available.")
        return
    for priority, mission_data in missions:
        print(f"Mission ID: {mission_data[1]}, in location: {mission_data[2]}, Payload of: {mission_data[3]}, Status: {mission_data[4]},takes battery of: {mission_data[5]}")

  
# Main menu
option = 0
while option != 5:
    print("\n=== Warehouse Robot Mission Control ===\n")
    print("1. Add new Mission")
    print("2. Execute the next mission")
    print("3. View all pending missions")
    print("4. View the mission history stack")
    print("5. Exit")

    try:
        option = int(input("\nChoose an option: "))

        if option == 1:
            add_mission()
        
        elif option == 2:
            execute()
        
        elif option == 3:
            view_mission()

        elif option == 4:
            view_completed()
        
        elif option == 5:
            print("Thank You! Bye")

        else:
            print("Invalid option. Choose a valid option [1-5]")

    except ValueError:
        print("Invalid input. Choose a valid option [1-5]")