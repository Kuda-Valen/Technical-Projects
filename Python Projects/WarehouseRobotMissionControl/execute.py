import battery 
import heapq

# Processing of the information which is mission execution
def execute():
    global percent
    global completed_missions
    global missions

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
    
        

    
