#Task 5: Read Data into a DataFrame

import sqlite3
import pandas as pd

# Define database path
db_path = "../db/lesson.db"

def read_order_data_to_dataframe():
    try:
        # Connect to the database
        connection = sqlite3.connect(db_path)
        
        # SQL query to join line_items and products tables
        query = """
            SELECT 
                line_items.line_item_id,
                line_items.quantity,
                line_items.product_id,
                products.product_name,
                products.price
            FROM line_items
            JOIN products ON line_items.product_id = products.product_id
        """
        
        # Read the query results into a DataFrame
        df = pd.read_sql_query(query, connection)
        print("\nOrder Data DataFrame:")
        print(df)
        return df
        
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    except ImportError:
        print("Please install pandas: pip install pandas")
    finally:
        if 'connection' in locals():
            connection.close()

#Task 5-3:  Print the first 5 lines of the resulting DataFrame.

def print_first_five_rows():
    try:
        # Get the DataFrame
        df = read_order_data_to_dataframe()
        
        # Print first 5 rows
        print("\nFirst 5 rows of the DataFrame:")
        print(df.head())
        
    except Exception as e:
        print(f"Error printing DataFrame: {e}")

if __name__ == "__main__":
    print_first_five_rows()


#Task 5-4:  Add a column to the DataFrame called "total".    

def add_total_column():
    try:
        # Get the DataFrame
        df = read_order_data_to_dataframe()
        
        # Add total column (quantity * price)
        df['total'] = df['quantity'] * df['price']
        
        # Print first 5 rows with the new total column
        print("\nFirst 5 rows of the DataFrame with total column:")
        print(df.head())
        
    except Exception as e:
        print(f"Error adding total column: {e}")

if __name__ == "__main__":
    add_total_column()

#Task 5-5: Add groupby() code to group by the product_id.   

def group_by_product():
    try:
        # Get the DataFrame with total column
        df = read_order_data_to_dataframe()
        df['total'] = df['quantity'] * df['price']
        
        # Group by product_id and aggregate
        grouped_df = df.groupby('product_id').agg({
            'line_item_id': 'count',
            'total': 'sum',
            'product_name': 'first'
        }).reset_index()
        
        # Print first 5 rows of the grouped DataFrame
        print("\nFirst 5 rows of the grouped DataFrame:")
        print(grouped_df.head())
        
    except Exception as e:
        print(f"Error grouping data: {e}")

if __name__ == "__main__":
    group_by_product()

#Task 5-6: Sort the DataFrame by the product_name column.   

def sort_by_product_name():
    try:
        # Get the grouped DataFrame
        df = read_order_data_to_dataframe()
        df['total'] = df['quantity'] * df['price']
        
        # Group by product_id and aggregate
        grouped_df = df.groupby('product_id').agg({
            'line_item_id': 'count',
            'total': 'sum',
            'product_name': 'first'
        }).reset_index()
        
        # Sort by product_name
        sorted_df = grouped_df.sort_values('product_name')
        
        # Print the sorted DataFrame
        print("\nDataFrame sorted by product_name:")
        print(sorted_df)
        
    except Exception as e:
        print(f"Error sorting data: {e}")

if __name__ == "__main__":
    sort_by_product_name()

#Task 5-7: Add code to write this DataFrame to a file order_summary.csv.  

def write_to_csv():
    try:
        # Get the grouped and sorted DataFrame
        df = read_order_data_to_dataframe()
        df['total'] = df['quantity'] * df['price']
        
        # Group by product_id and aggregate
        grouped_df = df.groupby('product_id').agg({
            'line_item_id': 'count',
            'total': 'sum',
            'product_name': 'first'
        }).reset_index()
        
        # Sort by product_name
        sorted_df = grouped_df.sort_values('product_name')
        
        # Write to CSV file
        csv_path = "order_summary.csv"
        sorted_df.to_csv(csv_path, index=False)
        print(f"\nDataFrame written to {csv_path}")
        
        # Verify the file contents
        print("\nVerifying CSV file contents:")
        verification_df = pd.read_csv(csv_path)
        print(verification_df)
        
    except Exception as e:
        print(f"Error writing to CSV: {e}")

if __name__ == "__main__":
    write_to_csv()







