#!/usr/bin/python3
"""Returns to-do list information for a given employee ID."""
import sys
import requests

def gather_data_from_api(employee_id):
    # API endpoint URL
    url = f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}'
    
    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        
        # Parse the JSON response
        todo_list = response.json()
        
        # Get employee name
        employee_name = todo_list[0]['username']
        
        # Filter completed tasks
        completed_tasks = [task for task in todo_list if task['completed']]
        
        # Prepare output
        output = f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todo_list)}):\n"
        for task in completed_tasks:
            output += f"\t{task['title']}\n"
        
        return output
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)
    
    employee_id = sys.argv[1]
    if not employee_id.isdigit():
        print("EMPLOYEE_ID must be an integer.")
        sys.exit(1)
    
    result = gather_data_from_api(int(employee_id))
    print(result)
