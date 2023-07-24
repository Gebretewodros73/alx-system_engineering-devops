# API Data Handling Repository

This repository contains Python scripts to gather data from an API, process it, and export it in various formats such as CSV and JSON. The API used provides information about employee TODO list progress.

## Tasks

### Task 0: Gather Data from an API

**Description:**
This script retrieves information about an employee's TODO list progress from a given employee ID using a REST API. The script uses either the `urllib` or `requests` module to make API requests.

**Requirements:**
- Use `urllib` or `requests` module for API requests
- Accept an integer as a parameter, representing the employee ID
- Display the employee TODO list progress in a specific format

**Usage:**
```bash
python3 1-export_to_CSV.py EMPLOYEE_ID
```

### Task 1: Export to CSV

**Description:**
Building on Task 0, this script extends the functionality to export the retrieved data in CSV format. The script will record all tasks owned by a specific employee and save them in a CSV file named `USER_ID.csv`.

**Requirements:**
- Use the data obtained from Task 0
- Save the data in CSV format with specific fields: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"

**Usage:**
```bash
python3 1-export_to_CSV.py EMPLOYEE_ID
```

### Task 2: Export to JSON

**Description:**
In this task, the script extends the functionality from Task 0 to export data in JSON format. The script will record all tasks owned by a specific employee and save them in a JSON file named `USER_ID.json`.

**Requirements:**
- Use the data obtained from Task 0
- Save the data in JSON format with the following structure:
```bash
{
  "USER_ID": [
    {
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS,
      "username": "USERNAME"
    },
    ...
  ]
}
```

**Usage:**
```bash
python3 3-dictionary_of_list_of_dictionaries.py
```

### Task 3: Dictionary of List of Dictionaries

**Description:**
This script extends the functionality from Task 0 to export data in JSON format for all employees. The script records all tasks from all employees and saves them in a JSON file named `todo_all_employees.json`.

**Requirements:**
- Use the data obtained from Task 0 for all employees
- Save the data in JSON format with the following structure:
```bash
{
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ],
  "USER_ID": [
    {
      "username": "USERNAME",
      "task": "TASK_TITLE",
      "completed": TASK_COMPLETED_STATUS
    },
    ...
  ],
  ...
}
```

**Usage:**
```bash
python3 3-dictionary_of_list_of_dictionaries.py
```

## Repository Structure

- GitHub repository: [alx-system_engineering-devops](https://github.com/gebretewodros73/alx-system_engineering-devops)
- Directory: 0x15-api
- Files:
  - [0-gather_data_from_an_API.py](./0-gather_data_from_an_API.py): Python script for Task 0
  - [1-export_to_CSV.py](./1-export_to_CSV.py): Python script for Task 1
  - [2-export_to_JSON.py](./2-export_to_JSON.py): Python script for Task 2
  - [3-dictionary_of_list_of_dictionaries.py](./3-dictionary_of_list_of_dictionaries.py): Python script for Task 3
