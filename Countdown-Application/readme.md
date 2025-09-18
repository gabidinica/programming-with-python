# Demo Project: Countdown Application

## Technologies Used
- Python
- IntelliJ
- Git

## Project Description
Develop an application that allows the user to input a **goal** and a **deadline (date)**. The application should then calculate and display the **remaining time** until the specified deadline.

---

## User Input for Goal and Deadline

The application allows the user to provide input for a **goal** and its **deadline**.  

### Input Format
`goal:dd.mm.yyyy`

> *Example*: learn python:10.02.2024
> **Note:** The date format is **day.month.year**.


We **split** the string using the colon (`:`) as a separator. This produces a **list with two values**: the goal and the deadline.  

We can then save these values into two separate variables:

```python
user_input = "learn python:10.02.2024"
goal, deadline = user_input.split(":")
```

> goal now contains "learn python"
> deadline now contains "10.02.2024"

## Converting Deadline to `datetime`

To calculate how many days are left until the deadline, we need the **deadline as a `datetime` object** instead of a string.  

We can convert the deadline string using `datetime.strptime`:

```python
from datetime import datetime
```

user_input = "learn python:10.02.2024"
goal, deadline_str = user_input.split(":")

### Convert string to datetime
deadline = datetime.strptime(deadline_str, "%d.%m.%Y")

- deadline_str contains the string "10.02.2024"
- deadline is now a datetime object representing 10th February 2024
This conversion allows us to calculate the *remaining time* from today until the deadline.
