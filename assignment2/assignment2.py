import csv
import traceback
import os  # Add import for os module
import custom_module  # Add import for custom_module
from datetime import datetime

print("--------------Task2-----------------------------------")
def read_employees():
    # Initialize empty dict and list
    result_dict = {}
    rows_list = []
    
    try:
        with open('../csv/employees.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            
            # Get all rows
            all_rows = list(csv_reader)
            
            # Store headers in dict
            result_dict['fields'] = all_rows[0]
            
            # Store remaining rows in list
            rows_list = all_rows[1:]
            
            # Add rows to dict
            result_dict['rows'] = rows_list
            
            return result_dict
            
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        exit(1)

# Call the function and store result in global variable
employees = read_employees()
print(employees) 

print("--------------Task3-----------------------------------")

def column_index(column_name):
    return employees["fields"].index(column_name)

# Call the function and store result in global variable
employees = read_employees()
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"Employee ID column index: {employee_id_column}") 

print("--------------Task4-----------------------------------")

def first_name(row_number):
    # Get the index of the first_name column
    first_name_index = column_index("first_name")
    # Get the value from the specified row at that index
    return employees["rows"][row_number][first_name_index]

# Call the function and store result in global variable
employees = read_employees()
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"Employee ID column index: {employee_id_column}")

# Test the first_name function
print(f"First name in row 0: {first_name(0)}")

print("--------------Task5-----------------------------------")


def employee_find(employee_id):
    # Define inner function to match employee IDs
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    # Use filter to find matching rows
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# Call the function and store result in global variable
employees = read_employees()
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"Employee ID column index: {employee_id_column}")

# Test the first_name function
print(f"First name in row 0: {first_name(0)}")

# Test the employee_find function
print(f"Matching rows for employee_id 1: {employee_find(1)}")


print("--------------Task6-----------------------------------")


def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# Call the function and store result in global variable
employees = read_employees()
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"Employee ID column index: {employee_id_column}")

# Test the first_name function
print(f"First name in row 0: {first_name(0)}")

# Test both employee_find functions
print(f"Matching rows for employee_id 1 (original): {employee_find(1)}")
print(f"Matching rows for employee_id 1 (lambda): {employee_find_2(1)}")

print("--------------Task7-----------------------------------")

def sort_by_last_name():
    # Get the index for last_name column
    last_name_index = column_index("last_name")
    # Sort the rows in place using a lambda to specify the sort key
    employees["rows"].sort(key=lambda row: row[last_name_index])
    return employees["rows"]

# Call the function and store result in global variable
employees = read_employees()
print("Original employees dict:")
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"\nEmployee ID column index: {employee_id_column}")

# Test the first_name function
print(f"\nFirst name in row 0: {first_name(0)}")

# Test both employee_find functions
print(f"\nMatching rows for employee_id 1 (original): {employee_find(1)}")
print(f"\nMatching rows for employee_id 1 (lambda): {employee_find_2(1)}")

# Sort and print the results
sorted_rows = sort_by_last_name()
print("\nEmployees sorted by last name:")
print(employees)

print("--------------Task8-----------------------------------")

def employee_dict(row):
    # Standard approach
    result = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":  # Skip employee_id
            result[field] = row[i]
    return result

    # Alternative approach using zip
    # return {field: value 
    #         for field, value in zip(employees["fields"], row) 
    #         if field != "employee_id"}

# Call the function and store result in global variable
employees = read_employees()
print("Original employees dict:")
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"\nEmployee ID column index: {employee_id_column}")

# Test the first_name function
print(f"\nFirst name in row 0: {first_name(0)}")

# Test both employee_find functions
print(f"\nMatching rows for employee_id 1 (original): {employee_find(1)}")
print(f"\nMatching rows for employee_id 1 (lambda): {employee_find_2(1)}")

# Sort and print the results
sorted_rows = sort_by_last_name()
print("\nEmployees sorted by last name:")
print(employees)

# Test employee_dict function with first row
print("\nFirst employee as dictionary:")
print(employee_dict(employees["rows"][0]))

print("--------------Task9-----------------------------------")

def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        # Get employee_id from the row as a string
        emp_id = row[employee_id_column]  # Remove the int() conversion
        # Create employee dict for this row and store it
        result[emp_id] = employee_dict(row)
    return result

# Call the function and store result in global variable
employees = read_employees()
print("Original employees dict:")
print(employees)

# Get the index of employee_id column
employee_id_column = column_index("employee_id")
print(f"\nEmployee ID column index: {employee_id_column}")

# Test the first_name function
print(f"\nFirst name in row 0: {first_name(0)}")

# Test both employee_find functions
print(f"\nMatching rows for employee_id 1 (original): {employee_find(1)}")
print(f"\nMatching rows for employee_id 1 (lambda): {employee_find_2(1)}")

# Sort and print the results
sorted_rows = sort_by_last_name()
print("\nEmployees sorted by last name:")
print(employees)

# Test employee_dict function with first row
print("\nFirst employee as dictionary:")
print(employee_dict(employees["rows"][0]))

# Test all_employees_dict function
print("\nAll employees as dictionary of dictionaries:")
print(all_employees_dict())

print("--------------Task10-----------------------------------")

def get_this_value():
    # Get the environment variable, with a default value in case it's not set
    value = os.getenv('THISVALUE')
    if value is None:
        return "ABC"  # Return default value if environment variable is not set
    return value

    print("--------------Task11-----------------------------------")


def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# Test the secret setting
set_that_secret("my new secret")
print(f"Current secret: {custom_module.secret}")



def read_csv_to_dict(filename):
    """Helper function to read CSV file and return dict with fields and tuple rows"""
    result_dict = {}
    try:
        with open(filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            # Get all rows
            all_rows = list(csv_reader)
            # Store headers in dict
            result_dict['fields'] = all_rows[0]
            # Store remaining rows as tuples
            result_dict['rows'] = [tuple(row) for row in all_rows[1:]]
            return result_dict
    except Exception as e:
        print(f"Error reading {filename}: {str(e)}")
        return None

    print("--------------Task12-----------------------------------")    

def read_minutes():
    # Read both CSV files using the helper function
    minutes1 = read_csv_to_dict('../csv/minutes1.csv')
    minutes2 = read_csv_to_dict('../csv/minutes2.csv')
    return minutes1, minutes2

# Call read_minutes and store results in global variables
minutes1, minutes2 = read_minutes()

# Print the results
print("\nMinutes 1:")
print(minutes1)
print("\nMinutes 2:")
print(minutes2)

print("--------------Task13-----------------------------------")

def create_minutes_set():
    # Create a set from the rows in both minutes1 and minutes2
    # Using set() to automatically remove duplicates
    combined_set = set(minutes1['rows'] + minutes2['rows'])
    return combined_set

# Test create_minutes_set
minutes_set = create_minutes_set()
print("\nUnique minutes entries:")
print(minutes_set)

print("--------------Task14-----------------------------------")

def create_minutes_list():
    # Convert set to list
    minutes_list = list(minutes_set)
    
    # Map each element to convert the date string to datetime object
    # Keep the name unchanged, but convert the date
    result = list(map(
        lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),
        minutes_list
    ))
    
    return result

# Call the function and store in global variable
minutes_list = create_minutes_list()
print("\nMinutes list with datetime objects:")
print(minutes_list)

print("--------------Task15-----------------------------------")

def write_sorted_list():
    # Sort minutes_list by datetime (second element of each tuple)
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    
    # Convert datetime objects back to strings
    converted_list = list(map(
        lambda x: (x[0], x[1].strftime("%B %d, %Y")),
        sorted_minutes
    ))
    
    # Write to CSV file
    try:
        with open('./minutes.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            # Write headers from minutes1
            writer.writerow(minutes1['fields'])
            # Write data rows
            writer.writerows(converted_list)
    except Exception as e:
        print(f"Error writing CSV file: {str(e)}")
        return None
    
    return converted_list

# Call the function and check results
sorted_converted_list = write_sorted_list()
print("\nSorted and converted minutes list:")
print(sorted_converted_list)




