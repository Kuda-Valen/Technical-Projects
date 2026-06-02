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

Inventory = []

class Product:
    def __init__(self, product_id, product_name, stock_count, price):
        self.product_id = product_id
        self.product_name = product_name
        self.stock_count = stock_count
        self.price = price

    def add_product(self):
        # Adding a new product
        print("\nAdd New Product to Inventory\n")
        product_id = input("Enter product ID: ")
        product_name = input("Enter product name: ")
        stock_count = int(input("Enter number of product to add: "))
        price = float(input("Enter product price: R"))

        product = {
            "product_id" : product_id, 
            "product_name" : product_name, 
            "stock_count" : stock_count, 
            "price" : price
        }
        
        Inventory.append(product)

        print(f"Product has been added successfully: |{Inventory(product)}|")

    def search_product(self): 
            print("|Add or Remove stock from directory|")
        
    def purchase(self):
        print("Purchasing product..")

    def view_products(self):
        # Viewing all products
        print(Inventory)    


if __name__ == "__main__":
    product_class = Product()

    while True:
        print("\n<-- Undo-Capable Flash-Sale Checkout System -->\n")
        print("1. Add New Product")
        print("2. View All products")
        print("3. Purchase a product")
        print("10. Exit")

        try:
            option = int(input("\nChoose an option: "))

            if option == 1:
                product_class.add_product()
            
            elif option == 2:
                product_class.view_products()
            
            elif option == 10:
                print("Exiting...")
                break

            else:
                print("Invalid option, Choose a correct option!!!")
        
        except ValueError as e:
            print(f"Invalid Input, Error: {e}")
