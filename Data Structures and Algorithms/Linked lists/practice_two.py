# Learning how to manipulate Lists
print("\n || Learning Lists ||\n")

my_list = []


def add_element(element):
    my_list.append(element)
    print(f"{element} was successfully added to list")

def view_list():
    i = 0
    if not my_list: 
        print("\nYour list is empty...")
    
    else: 
        while i < len(my_list):
            print(f"{i} -> {my_list[i]}")
            i += 1

option = 0
while option != 4:
    print("\n1. Add elements to the list")
    print("2. View the List with indexes")
    print("3. Remove elements")
    print("4. View List")
    print("5. Exit")

    option = int(input("\nSelect an Option: "))

    if option == 1: 
        # Call the def to add elements
        element = input("Enter an element to add to your List: ")
        add_element(element)
    
    elif option == 2: 
        # Call the def to view the list
        view_list()
    
    elif option == 3: 
        # Call the def to remove elements
        pass
    elif option == 4: 
        print(f"\n{my_list}")
    elif option == 5: 
        # Call the def to Exit
        break

