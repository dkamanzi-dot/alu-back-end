\# ALU Back-End: Gather Data from an API



This project is a set of Python scripts that consume the

\[JSONPlaceholder](https://jsonplaceholder.typicode.com) REST API to

retrieve and export an employee's TODO list progress.



\## Description



Given an employee ID, the scripts fetch that employee's profile and

task list from the API, then either print a progress summary to

standard output or export the full task list to CSV / JSON.



\## Requirements



\- Python 3

\- `requests` module (`pip install requests`)

\- All scripts should follow the pycodestyle (PEP8) style guide

\- All files must be executable



\## Files



| File | Description |

| --- | --- |

| `api/0-gather\_data\_from\_an\_API.py` | For a given employee ID, prints the employee's name and TODO list progress (completed task count and titles) to stdout. |

| `api/1-export\_to\_CSV.py` | For a given employee ID, exports all of that employee's tasks (completed and not) to a CSV file named `USER\_ID.csv`. |

| `api/2-export\_to\_JSON.py` | For a given employee ID, exports all of that employee's tasks to a JSON file named `USER\_ID.json`. |

| `api/3-dictionary\_of\_list\_of\_dictionaries.py` | Exports the TODO list progress of \*\*all\*\* employees to a single JSON file named `todo\_all\_employees.json`. |



\## Usage



\\`\\`\\`bash

python3 api/0-gather\_data\_from\_an\_API.py <employee\_id>

python3 api/1-export\_to\_CSV.py <employee\_id>

python3 api/2-export\_to\_JSON.py <employee\_id>

python3 api/3-dictionary\_of\_list\_of\_dictionaries.py

\\`\\`\\`



\## Author



Written as part of the ALU Back-End Web Development curriculum.

