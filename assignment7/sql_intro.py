import sqlite3
import os

#Task 1-3: Create a New SQLite Database

# Define database path
db_path = "../db/magazines.db"

#Task 3-2

# Functions to insert data
def add_publisher(name):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
        connection.commit()
        print(f"Publisher '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")
    finally:
        connection.close()

def add_magazine(name, publisher_id):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
        connection.commit()
        print(f"Magazine '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Magazine '{name}' already exists or invalid publisher.")
    finally:
        connection.close()

def add_subscriber(name, address):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT id FROM subscribers WHERE name = ? AND address = ?", (name, address))
        if cursor.fetchone():
            print(f"Subscriber '{name}' at '{address}' already exists.")
        else:
            cursor.execute("INSERT INTO subscribers (name, address) VALUES (?, ?)", (name, address))
            connection.commit()
            print(f"Subscriber '{name}' added successfully.")
    except sqlite3.Error as e:
        print(f"Error adding subscriber: {e}")
    finally:
        connection.close()

def add_subscription(subscriber_id, magazine_id, expiration_date):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO subscriptions (subscriber_id, magazine_id, expiration_date) VALUES (?, ?, ?)", 
                       (subscriber_id, magazine_id, expiration_date))
        connection.commit()
        print(f"Subscription added for subscriber {subscriber_id} to magazine {magazine_id}.")
    except sqlite3.IntegrityError:
        print(f"Invalid subscriber or magazine ID.")
    finally:
        connection.close()

#Task 1-4: try block ----   except block
try:
    # Create the db directory if it doesn't exist
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    
    # Connect to the database
    connection = sqlite3.connect(db_path)
    print("Successfully connected to the database")
    
    # Enable foreign key enforcement
    connection.execute("PRAGMA foreign_keys = 1")
    
    # Create a cursor object
    cursor = connection.cursor()
    
    # Task 2-2: Define Database Structure
    # Create publishers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS publishers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
    """)
    
    # Create magazines table with foreign key referencing publishers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES publishers(id)
        );
    """)
    
    # Create subscribers table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscribers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL
        );
    """)
    
    # Create subscriptions table with foreign keys referencing magazines and subscribers
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS subscriptions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES subscribers(id),
            FOREIGN KEY (magazine_id) REFERENCES magazines(id)
        );
    """)
    
    connection.commit()
    print("Tables created successfully")
    
except sqlite3.Error as e:
    print(f"Database error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    if 'connection' in locals():
        connection.close()
        print("Database connection closed.")



# Task 3-3:
# Populating tables with sample data
if __name__ == "__main__":
    # Add publishers
    add_publisher("Tech Today")
    add_publisher("Science Monthly")
    add_publisher("Fashion Weekly")
    
    # Add magazines (publisher_id 1, 2, 3)
    add_magazine("AI Insights", 1)
    add_magazine("Space Discovery", 2)
    add_magazine("Trendy Looks", 3)
    
    # Add subscribers
    add_subscriber("Alice Johnson", "123 Main St")
    add_subscriber("Bob Smith", "456 Elm St")
    add_subscriber("Charlie Davis", "789 Oak St")
    
    # Add subscriptions
    add_subscription(1, 1, "2025-12-31")  # Alice subscribes to AI Insights
    add_subscription(2, 2, "2025-11-30")  # Bob subscribes to Space Discovery
    add_subscription(3, 3, "2025-10-15")  # Charlie subscribes to Trendy Looks


   # Task 4-1: Write SQL Queries
    
    # Query to retrieve all information from subscribers table
    def get_all_subscribers():
        try:
            connection = sqlite3.connect(db_path)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM subscribers")
            subscribers = cursor.fetchall()
            print("\nAll Subscribers:")
            for subscriber in subscribers:
                print(f"ID: {subscriber[0]}, Name: {subscriber[1]}, Address: {subscriber[2]}")
        except sqlite3.Error as e:
            print(f"Error retrieving subscribers: {e}")
        finally:
            connection.close()

# Task 4-2: Retrieve Magazines

def get_magazines_sorted():
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT magazines.id, magazines.name, publishers.name as publisher_name 
            FROM magazines 
            JOIN publishers ON magazines.publisher_id = publishers.id 
            ORDER BY magazines.name
        """)
        magazines = cursor.fetchall()
        print("\nAll Magazines (Sorted by Name):")
        for magazine in magazines:
            print(f"ID: {magazine[0]}, Name: {magazine[1]}, Publisher: {magazine[2]}")
    except sqlite3.Error as e:
        print(f"Error retrieving magazines: {e}")
    finally:
        connection.close()

# Task 4-3: Find Mgazines for a Particular Publisher,        

def get_magazines_by_publisher(publisher_name):
    try:
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT magazines.id, magazines.name, publishers.name as publisher_name
            FROM magazines 
            JOIN publishers ON magazines.publisher_id = publishers.id 
            WHERE publishers.name = ?
        """, (publisher_name,))
        magazines = cursor.fetchall()
        print(f"\nMagazines published by '{publisher_name}':")
        if magazines:
            for magazine in magazines:
                print(f"ID: {magazine[0]}, Name: {magazine[1]}")
        else:
            print(f"No magazines found for publisher '{publisher_name}'")
    except sqlite3.Error as e:
        print(f"Error retrieving magazines: {e}")
    finally:
        connection.close()        

# Task 4-4:  print out all the rows

def demonstrate_all_queries():
    print("\n=== Demonstrating All Database Queries ===\n")
    
    # 1. Get all subscribers
    print("1. All Subscribers:")
    get_all_subscribers()
    
    # 2. Get all magazines sorted by name
    print("\n2. All Magazines (Sorted by Name):")
    get_magazines_sorted()
    
    # 3. Get magazines for each publisher
    print("\n3. Magazines by Publisher:")
    publishers = ["Tech Today", "Science Monthly", "Fashion Weekly"]
    for publisher in publishers:
        get_magazines_by_publisher(publisher)

# Add this to the main block to run the demonstration
if __name__ == "__main__":
    # ... existing code ...
    
    # Demonstrate all queries
    demonstrate_all_queries()
   
