

def view_mission():
    global missions

    if not missions:
        print("no missions available.")
        return
    for priority, mission_data in missions:
        print(f"Mission ID: {mission_data[1]}, in location: {mission_data[2]}, Payload of: {mission_data[3]}, Status: {mission_data[4]},takes battery of: {mission_data[5]}")
    