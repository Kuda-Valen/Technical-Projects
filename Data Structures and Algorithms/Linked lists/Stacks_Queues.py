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

class ProductNode:
    def __init__(self, product_id, product_name, stock_count, price):
        self.product_id = product_id
        self.product_name = product_name
        self.stock_count = stock_count
        self.price = price
        self.next = None

class InventoryManager: 
    def __init__(self):
        self.head = None      # this will point to the next node (for now there is nothing to point to)

    def add_product(self):
        # Adding a new product
        print("\nAdd New Product to Inventory\n")
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        stock_count = int(input("Enter number of product to add: "))
        price = float(input("Enter product price: R"))

        new_product = ProductNode(product_id, product_name, stock_count, price)

        # If list is empty
        if self.head is None:
            self.head = new_product
            return
        
        # Otherwise we traverse
        current = self.head

        while current.next:
            current = current.next
        
        current.next = new_product

        print(f"Product has been added successfully: |{new_product.product_name}|")

    def search_product(self, product_id): 
            current = self.head

            while current: 
                if current.product_id == product_id:
                    return current
                
                current = current.next
        
            return None
        
    def purchase(self, product_id):
        
        product = self.search_product(product_id)

        if product is None:
            print("Product Not found")
            return False
        
        if product.stock_count <=  0:
            print("Out of Stock")
            return False
        
        product.stock_count -= 1

        print(f"{product.product_name} has been purchased successfully.")

        return True

    def view_products(self):
        # Viewing all products
        if self.head is None:
            print("There are no products")
            return
        
        current = self.head

        while current:
            print(f"ID : {current.product_id} |")
            print(f"Name : {current.product_name} |")
            print(f"Stock : {current.stock_count} |")
            print(f"Price: R{current.price} |")

            current = current.next   


if __name__ == "__main__":
    inventory_manager = InventoryManager()

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

