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