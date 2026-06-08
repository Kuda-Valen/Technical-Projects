# Undo-Capable Flash-Sale Checkout System

"""
    1. Architectural Requirements
    You must implement and utilize these three data structures from scratch:
    Singly Linked List: Managing the product inventory catalog.
    Queue: Managing the incoming customer checkout pipeline (FIFO).
    Stack: Managing user action history to allow "undo" operations (LIFO).
    
    2. Core System Features to Build📦 
    Inventory Manager (Linked List)Each node stores: product_id, product_name, stock_count, and price.
    Method: add_product(id, name, stock, price) to add new items.
    Method: decrease_stock(id) to reduce stock by 1 when a purchase succeeds.
    
    👥 Traffic Controller (Queue)
    Incoming checkout requests line up in your custom Queue.
    Each node stores: user_id, product_id, and timestamp.
    Method: enqueue_request(user_id, product_id)Method: process_next_checkout() which dequeues 
    the request and updates the Inventory Manager.
    
    ↩️ System Order Historian (Stack)
    Every successful checkout pushes an order log onto your custom Stack.
    Each node stores: order_id, user_id, and product_id.
    Method: cancel_last_purchase() (Undo). 
    This pops the last order off the stack, returns the item to the inventory stock, and logs the cancellation.
"""

class Node: 
    def __init__(self, data):
        self. data = data      # this is to store the value
        self. Next = None      # this will point to the next node (for now there is nothing to point to)

class Product:
    def __init__(self, product_id, product_name, stock_count, price):
        self.head = None
        self.product_id = product_id
        self.product_name = product_name
        self.stock_count = stock_count
        self.price = price
    
    # Method to add a new node at the end
    def append(self, data):
        new_node = Node(data)

        # If the list is empty, we make this new head
        if not self.head:
            self.head = new_node
            return
        
        # Otherwise travel to the end of the list to the last node
        current = self.head
        while current.next:
            current = current.next
        # We link the last node to the new node
        current.next = new_node

    def add_product(self):
        # Adding a new product
        print("\nAdd New Product to Inventory\n")
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        stock_count = int(input("Enter number of product to add: "))
        price = float(input("Enter product price: R"))

        product = Product(product_id, product_name, stock_count, price)

        self.inventory.append(product)

        print(f"Product has been added successfully: |{product.product_name}|")

    def search_product(self): 
            print("|Add or Remove stock from directory|")
        
    def purchase(self):
        print("Purchasing product..")

    def view_products(self):
        # Viewing all products
        if not self.inventory:
            print("There are no products")
        
        else:
            for product in self.inventory:
                print(product)   


#if __name__ == "__main__":
    #product_manager = Product()
def main_menu():
    while True:
        print("\n<-- Undo-Capable Flash-Sale Checkout System -->\n")
        print("1. Add New Product")
        print("2. View All products")
        print("3. Purchase a product")
        print("10. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                inventory_manager.add_product()
            
            elif option == 2:
                inventory_manager.view_products()
            
            elif option == 10:
                print("Exiting...")
                break

            else:
                print("Invalid option, Choose a correct option!!!")
        
        except ValueError as e:
            print(f"Invalid Input, Error: {e}")
