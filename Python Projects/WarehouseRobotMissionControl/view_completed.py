

def view_completed ():
    global completed_missions

    if not completed_missions:
        print("\nThere is no completed missions")
    
    else:
        for t in completed_missions: 
            print(t)