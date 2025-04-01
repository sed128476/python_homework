import pandas as pd
import numpy as np # load the numpy library


print('----------------------task 1-1 -----------------------------')
print("Convert the list of dictionaries into a DataFrame")
task1_data_frame = pd.DataFrame ({ 'Name': ['Alice', 'Bob', 'charlie'], 
                                    'Age': [25, 30, 35], 
                                   'City': ['New York', 'Los Angeles', 'Chicago']})


print(task1_data_frame)

print('----------------------------task 1-2 ------------------------')
print(' Make a copy of the DataFrame  DataFrame_Name.copy')
task1_with_salary = task1_data_frame.copy()

print("Add a new column called DataFrame_Name['Salary']")
task1_with_salary['Salary'] = [70000, 80000, 90000]

print(task1_with_salary)

print('----------------------------task 1-3 ------------------------')

#Make a copy of task1_with_salary
task1_older = task1_with_salary.copy()

# Increment the Age column by 1
task1_older['Age'] = task1_older['Age'] + 1

# Print the modified DataFrame
print(task1_older)



print('----------------------------task 1-4 ------------------------')
# Save the DataFrame to a CSV file without the index
task1_older.to_csv('employees.csv', index=False)

# Verify by reading the contents of the CSV file
with open('employees.csv', 'r') as file:
    print(file.read())


print('-------------------------task 2-1 ---------------------------')

# Load the CSV file into a new DataFrame
task2_employees = pd.read_csv('employees.csv')

# Print the DataFrame to verify the contents
print(task2_employees)

print('--------------------------task 2-2 --------------------------')


# Create the JSON file
additional_employees = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

# Save the JSON data to a file
import json
with open('additional_employees.json', 'w') as json_file:
    json.dump(additional_employees, json_file)

# Load the JSON file into a DataFrame
json_employees = pd.read_json('additional_employees.json')

# Print the DataFrame to verify it loaded correctly
print(json_employees)

print('------------------------task 2-3-------------------------------')


# Combine the two DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)

# Print the combined DataFrame
print(more_employees)


print('----------------------task 3-1 ------------------------------')

# Get the first three rows of the DataFrame
first_three = more_employees.head(3)

# Print the variable to verify
print(first_three)

print('----------------------tsk 3-2 ----------------------------')

# Get the last two rows of the DataFrame
last_two = more_employees.tail(2)

# Print the variable to verify
print(last_two)

print('-------------------------------task3-3------------------------')

# Get the shape of the DataFrame
employee_shape = more_employees.shape

# Print the variable to verify
print(employee_shape)

print('-----------------------------------task 3-4 -----------------------------')


# Print a concise summary of the DataFrame
more_employees.info()


print('--------------------task 4-1  -----------------------------')

# Create a DataFrame from the CSV file
dirty_data = pd.read_csv('dirty_data.csv')

# Print the dirty data to verify its contents
print("Dirty Data:")
print(dirty_data)

# Create a copy of the dirty data for cleaning
clean_data = dirty_data.copy()

# Print the copy to confirm creation
print("\nClean Data Copy:")
print(clean_data)


print('--------------------------- task 4-2 -----------------------')

# Remove duplicate rows from the DataFrame
clean_data = dirty_data.drop_duplicates()

# Print the DataFrame to verify changes
print("Clean Data without duplicates:")
print(clean_data)


print('------------------------ task 4-3 -------------------------')

# Convert the 'Age' column to numeric and handle missing values by filling them with the mean
clean_data = clean_data.copy()
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())

# Print the cleaned DataFrame to verify changes
print("Clean Data with numeric Age and handled missing values:")
print(clean_data)


print('-------------------------- task 4-4 ---------------------')

# Replace placeholders 'unknown' and 'n/a' with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a'], np.nan)

# Convert the 'Salary' column to numeric
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# Print the cleaned DataFrame to verify changes
print("Clean Data with numeric Salary and placeholders replaced:")
print(clean_data)


print('------------------------task  4-5 ------------------------------')

# Fill missing values in 'Age' with the mean
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())

# Fill missing values in 'Salary' with the median
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())


# Print the cleaned DataFrame to verify changes
print("Clean Data with missing values filled:")
print(clean_data)

print('------------------------------ task 4-6 ----------------------')

# Convert the 'Hire Date' column to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')

# Print the cleaned DataFrame to verify changes
print("Clean Data with Hire Date as datetime:")
print(clean_data)


print('-------------------------------- task 4-7 ------------------------------')


# Strip extra whitespace and convert 'Name' and 'Department' columns to uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

# Print the cleaned DataFrame to verify changes
print("Clean Data with standardized Name and Department:")
print(clean_data)
