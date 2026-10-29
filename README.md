# 🧮 Python Calculator

A simple command-line calculator built with Python using **functions, modules, dictionaries, loops, exception handling, and user input**.

This project demonstrates how to separate calculation logic into a Python module and use that module from the main program.

---

## 📁 Project Structure

```text
calculator_project/
│
├── calculator.py
├── main.py
└── README.md
```

### `calculator.py`

Contains the basic mathematical operations:

* Addition
* Subtraction
* Multiplication
* Division

### `main.py`

Contains the main calculator application and user interaction.

---

## ⚙️ Features

* Addition `+`
* Subtraction `-`
* Multiplication `*`
* Division `/`
* Continuous calculations
* Clear current calculation using `c`
* Exit the calculator using `q`
* Handles invalid number input
* Preserves integer results for integer inputs and floating-point results for decimal inputs
* Handles invalid operators
* Prevents division by zero
* Uses a dictionary to map operators to functions
* Uses a separate Python module for calculator operations

---

## 🧩 Technologies Used

* Python 3
* Functions
* Modules
* Dictionary
* `while` loops
* `try-except`
* User input
* Conditional statements

---WORKFLOW OF PROGRAM
START
  │
  ▼
Import calculator.py
  │
  ▼
Create operations dictionary
  │
  ▼
Ask for first number
  │
  ├── q → Exit
  │
  ├── invalid → Ask again
  │
  ▼
Store number in result
  │
  ▼
Ask for operation
  │
  ├── q → Exit
  │
  ├── c → Clear → Ask for new first number
  │
  ├── invalid → Ask operation again
  │
  ▼
Ask for second number
  │
  ├── q → Exit
  │
  ├── invalid → Ask operation again
  │
  ├── division by zero → Ask operation again
  │
  ▼
Perform calculation
  │
  ▼
Update result
  │
  ▼
Print result
  │
  ▼
Ask for another operation
  │
  └───────────────┐
                  │
                  ▼
               Repeat

## ▶️ How to Run

### 1. Create a project folder

```text
calculator_project
```

### 2. Create two Python files

```text
calculator.py
main.py
```

### 3. Put the calculation functions inside `calculator.py`

### 4. Put the main program inside `main.py`

### 5. Open the terminal in the project folder

Run:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

---

## 💻 Example

```text
Calculator (enter c to clear or q to quit)

Enter a number: 10
Enter an operation (+, -, *, /), c to clear, or q to quit: +
Enter the next number: 5
Result: 15

Enter an operation (+, -, *, /), c to clear, or q to quit: *
Enter the next number: 2
Result: 30

Enter an operation (+, -, *, /), c to clear, or q to quit: /
Enter the next number: 3
Result: 10

Enter an operation (+, -, *, /), c to clear, or q to quit: q
Thank you for using the calculator.
```

---

## 🧠 Concepts Practiced

### 1. Functions

The mathematical operations are separated into functions:

```python
def add(a, b):
    return a + b
```

---

### 2. Modules

The calculation functions are stored in `calculator.py`.

They are imported into `main.py` using:

```python
import calculator
```

Then they can be accessed using:

```python
calculator.add()
calculator.sub()
calculator.mul()
calculator.div()
```

---

### 3. Dictionary of Functions

The program connects operators with their corresponding functions:

```python
operations = {
    "+": calculator.add,
    "-": calculator.sub,
    "*": calculator.mul,
    "/": calculator.div,
}
```

This allows the program to select the correct function dynamically.

For example:

```python
operations["+"](10, 5)
```

is equivalent to:

```python
calculator.add(10, 5)
```

---

### 4. Exception Handling

The program handles invalid number input:

```python
try:
    result = int(first_value)
except ValueError:
    try:
        result = float(first_value)
    except ValueError:
        print("Please enter a valid number.")
```

Integer input stays an integer when possible (for example, `10`), while decimal
input such as `10.0` stays a float. Division with a fractional quotient returns
a float; an exact quotient from integer inputs is displayed as an integer.

So entering:

```text
Enter a number: abc
```

doesn't crash the program.

---

### 5. Division by Zero

The program prevents:

```text
10 / 0
```

using:

```python
if op == "/" and operand == 0:
    print("Error: Division by zero is not allowed.")
    continue
```

---

## 🚨 Common Setup Error

If you get:

```text
ModuleNotFoundError: No module named 'calculator'
```

make sure your files are in the **same folder**:

```text
calculator_project/
│
├── calculator.py
└── main.py
```

Also make sure the file is actually named:

```text
calculator.py
```

and **not**:

```text
calculator.py.txt
calculator
Calculator.py
```

Python module names can also be affected by capitalization on some systems.

---

## 🔧 Important

Run the program from the project folder:

```bash
cd calculator_project
python main.py
```

Do **not** run `calculator.py` if you want to start the complete application.

The entry point of this project is:

```text
main.py
```

---

## 🎯 Future Improvements

Possible upgrades for this project:

* Add `%` modulo operation
* Add power `**`
* Add square root
* Add calculator history
* Add better error handling
* Add integer/decimal formatting
* Create a GUI using Tkinter
* Add unit tests
* Add calculation history to a file
* Convert it into an object-oriented calculator

---

## 👨‍💻 Author
**Bhavesh Pawar**
**Vishwajeet Mangude**

---

## 📌 Project Summary

This project is a beginner-friendly Python calculator designed to practice:

```text
Functions
   ↓
Modules
   ↓
Dictionaries
   ↓
Loops
   ↓
Exception Handling
   ↓
User Input
   ↓
Complete Python CLI Application
```
