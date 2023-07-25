#!/usr/bin/python3
"""
Module Description; extends the functionality to export the retrieved data in CSV format
"""
import sys
import requests
import csv

def gather_data_from_api(employee_id):
    # API endpoint URL
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        
        # Parse the JSON response
        todo_list = response.json()
        return todo_list
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        sys.exit(1)

def export_to_csv(employee_id, todo_list):
    # Get the employee's username
    username = todo_list[0]['username']
    
    # Prepare CSV file name
    filename = f"{employee_id}.csv"
    
    # Write data to CSV file
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_list:
            writer.writerow([employee_id, username, task['completed'], task['title']])
    
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py EMPLOYEE_ID")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)
    
    todo_list = gather_data_from_api(int(employee_id))
    export_to_csv(employee_id, todo_list)
