#!/usr/bin/python3
"""
Module Description; extends the functionality
from Task 0 to export data in JSON format
"""
import sys
import requests
import json


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


def export_to_json(employee_id, todo_list):
    # Get the employee's username
    username = todo_list[0]['username']

    # Prepare JSON file name
    filename = f"{employee_id}.json"

    # Prepare JSON data
    data = {employee_id: []}
    for task in todo_list:
        data[employee_id].append({"task": task['title'],  "completed": task['completed'], "username": username})
    
    # Write data to JSON file
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)
    
    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py EMPLOYEE_ID")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)
    
    todo_list = gather_data_from_api(int(employee_id))
    export_to_json(employee_id, todo_list)
