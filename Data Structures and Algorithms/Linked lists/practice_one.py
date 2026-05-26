class Node: 
    def __init__(self, data):
        self.data = data      # This is to store the value
        self.next = None      # This points to the next node (none by default)

class LinkedList: 
    def __init__(self):
        self.head = None      # This is the first node in the list

    # method to add a new node at the end 
    def append(self, data): 
        new_node = Node(data)

        # If the list is empty, make this the head
        if not self.head: 
            self.head = new_node
            return
        
        # Otherwise, travel to the end of the list
        current = self.head
        while current.next:
            current = current.next
        # Link the last node to the new node
        current.next = new_node
    
    # Method to print teh list so we can see it
    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) +" -> None")


def main():
    print("\n<--Learning Linked Lists-->\n")
    my_list = LinkedList()
    
    while True:
        print("\n1. Add elements to the Linked List")
        print("2. View the Linked List")
        print("3. Remove elements from Linked List")
        print("4. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                element = input("\nEnter value of element to add to list: ")
                my_list.append(element)
                print(f"'{element}' was successfully added to list")
            
            elif option == 2:
                print("\nView the Linked list")
                my_list.display()
            
            elif option == 3:
                print("\nRemove elements from Linked List")

            elif option == 4:
                print("Exiting...")
                break  

            else: print("\n!!!!Invalid Option. Choose valid option!!!!")          
            
        except Exception as e:
            print(f"!!!Invalid input. This is the Error: {e}")

main()