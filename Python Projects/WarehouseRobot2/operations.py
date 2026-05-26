import heapq
from data import missions, completed_missions
from utils import check_battery

def execute():
    if not missions:
        print("No missions available")
        return

    priority, mission_data = heapq.heappop(missions)

    print(f"\nExecuting mission {mission_data[1]} (Priority {priority})")

    if not check_battery(mission_data[5]):
        print("Insufficient battery → re-adding mission")
        heapq.heappush(missions, (1, mission_data))
        return

    finish = input("Mission finished? [Y/N]: ").lower()

    if finish == 'y':
        completed_missions.append(mission_data)
        print("Mission completed")
    else:
        heapq.heappush(missions, (1, mission_data))
        print("Mission re-added")