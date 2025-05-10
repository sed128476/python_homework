import sqlite3

# Connect to the database
conn = sqlite3.connect('../db/lesson.db')
cursor = conn.cursor()

# Enable foreign key constraints
conn.execute("PRAGMA foreign_keys = 1")


#Task 1: Complex JOINs with Aggregation


# SQL query to find total price of first 5 orders
query = """
SELECT 
    o.order_id,
    SUM(p.price * li.quantity) as total_price
FROM orders o
JOIN line_items li ON o.order_id = li.order_id
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5
"""

# Execute the query
cursor.execute(query)

# Fetch and print results
print("Order ID | Total Price")
print("----------------------")
for row in cursor.fetchall():
    order_id, total_price = row
    print(f"{order_id:8} | ${total_price:.2f}")


#Task 2: Understanding Subqueries    

# SQL query to find average order price per customer
query2 = """
SELECT 
    c.customer_name,
    COALESCE(AVG(order_totals.total_price), 0) as average_total_price
FROM customers c
LEFT JOIN (
    SELECT 
        o.customer_id as customer_id_b,
        SUM(p.price * li.quantity) as total_price
    FROM orders o
    JOIN line_items li ON o.order_id = li.order_id
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.order_id
) order_totals ON c.customer_id = order_totals.customer_id_b
GROUP BY c.customer_id
"""

# Execute the query
cursor.execute(query2)

# Fetch and print results
print("\nCustomer Average Order Prices:")
print("Customer Name | Average Order Price")
print("--------------------------------")
for row in cursor.fetchall():
    customer_name, avg_price = row
    print(f"{customer_name:13} | ${avg_price:.2f}")


#Task 3: Creating a New Order with Line Items

try:
    # Start transaction
    conn.execute("BEGIN TRANSACTION")
    
    # Get customer_id for Perez and Sons
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons'")
    customer_id = cursor.fetchone()[0]
    
    # Get employee_id for Miranda Harris
    cursor.execute("SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris'")
    employee_id = cursor.fetchone()[0]
    
    # Get the 5 least expensive products
    cursor.execute("""
        SELECT product_id 
        FROM products 
        ORDER BY price 
        LIMIT 5
    """)
    product_ids = [row[0] for row in cursor.fetchall()]
    
    # Create the order
    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id, date)
        VALUES (?, ?, date('now'))
        RETURNING order_id
    """, (customer_id, employee_id))
    order_id = cursor.fetchone()[0]
    
    # Create line items for each product
    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, 10)
        """, (order_id, product_id))
    
    # Commit the transaction
    conn.commit()
    
    # Print the order details
    print("\nNew Order Details:")
    print("Line Item ID | Quantity | Product Name")
    print("------------------------------------")
    cursor.execute("""
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?
        ORDER BY li.line_item_id
    """, (order_id,))
    
    for row in cursor.fetchall():
        line_item_id, quantity, product_name = row
        print(f"{line_item_id:11} | {quantity:8} | {product_name}")

except Exception as e:
    # Rollback in case of error
    conn.rollback()
    print(f"Error occurred: {e}")


# Task 4: Aggregation with HAVING

# SQL query to find employees with more than 5 orders
query4 = """
SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    COUNT(o.order_id) as order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC
"""

# Execute the query
cursor.execute(query4)

# Print results
print("\nEmployees with More Than 5 Orders:")
print("Employee ID | First Name | Last Name | Order Count")
print("------------------------------------------------")
for row in cursor.fetchall():
    employee_id, first_name, last_name, order_count = row
    print(f"{employee_id:11} | {first_name:10} | {last_name:9} | {order_count:11}")

# Close the connection
conn.close()
