\# 0x00. AirBnB clone - API (Gather Data from an API)



\## Project Description



This directory contains Python scripts that consume the

\[JSONPlaceholder](https://jsonplaceholder.typicode.com) REST API to

retrieve and export an employee's TODO list progress.



\## Files



| File | Description |

| --- | --- |

| `0-gather\_data\_from\_an\_API.py` | For a given employee ID, prints the employee's name and TODO list progress (number of completed tasks / total tasks) to stdout, followed by the title of each completed task. |

| `1-export\_to\_CSV.py` | For a given employee ID, exports all of that employee's tasks (completed and not) to a CSV file named `USER\_ID.csv`. |

| `2-export\_to\_JSON.py` | For a given employee ID, exports all of that employee's tasks to a JSON file named `USER\_ID.json`. |

| `3-dictionary\_of\_list\_of\_dictionaries.py` | Exports the TODO list progress of all employees to a single JSON file named `todo\_all\_employees.json`. |



\## Requirements



\- Python 3

\- `requests` module

\- Ubuntu 20.04 LTS style shebang: `#!/usr/bin/python3`

\- All code follows the pycodestyle (PEP8) style guide



\## Usage



```bash

python3 0-gather\_data\_from\_an\_API.py <employee\_id>

python3 1-export\_to\_CSV.py <employee\_id>

python3 2-export\_to\_JSON.py <employee\_id>

python3 3-dictionary\_of\_list\_of\_dictionaries.py

```



\## Example



```bash

$ python3 0-gather\_data\_from\_an\_API.py 2

Employee Ervin Howell is done with tasks(8/20):

&#x09; distinctio vitae autem nihil ut molestias quo

&#x09; voluptas quo tenetur perspiciatis explicabo natus

&#x09; aliquam aut quasi

&#x09; veritatis pariatur delectus

&#x09; nemo perspiciatis repellat ut dolor libero commodi blanditiis omnis

&#x09; repellendus veritatis molestias dicta incidunt

&#x09; excepturi deleniti adipisci voluptatem et neque optio illum ad

&#x09; totam atque quo nesciunt

```

