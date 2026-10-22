# Python Property Decorators: Getter, Setter, and Deleter

## 📌 Project Overview

This project demonstrates the use of Python's `@property`, `@data.setter`, and `@data.deleter` decorators to manage class attributes through a single property interface.

The example uses a `Bank` class to represent employee information, including employee data, name, working hours, and department. It demonstrates how to retrieve, update, and delete attributes using property decorators.

## 🎯 Objectives

* Understand Python's `@property` decorator.
* Implement getter, setter, and deleter methods.
* Manage class attributes through a property interface.
* Understand public, protected-style, and private-style attributes.
* Learn how to update multiple attributes using tuple unpacking.
* Explore attribute access using Python's `getattr()` function.

## 🛠️ Technologies Used

* **Programming Language:** Python 3
* **Concepts:** Object-Oriented Programming (OOP)
* **Decorators:** `@property`, `@data.setter`, `@data.deleter`
* **Built-in Function:** `getattr()`

## 📂 Project Structure

```text
Python-Property-Decorators/
│
├── bank.py
└── README.md
```

## 💻 Source Code

```python
class Bank:
    def __init__(self, TE, Mname, working_hour, dept):
        self.TE = TE
        self.name = Mname
        self._hour = working_hour
        self.__dept = dept

    @property
    def data:
        return (
            getattr(self, "TE", "employee_data"),
            getattr(self, "name", "name_data"),
            getattr(self, "_hour", "Hour_data"),
            getattr(self, "__dept", "dept_data"))

    @data.setter
    def data(self, values):
        self.TE, self.name, self._hour, self.__dept = values

    @data.deleter
    def data(self):
        del self.name, self.__dept


b = Bank(250, "Smith", 9, "Finance")

print(b.data)

b.data = (500, "Allen", 8, "Sales")
print(b.data)

del b.data
print(b.data)
```

## ⚙️ How It Works

### 1. Constructor (`__init__`)

The constructor initializes four attributes:

| Attribute | Description                      | Access Convention |
| --------- | -------------------------------- | ----------------- |
| `TE`      | Stores employee-related data     | Public            |
| `name`    | Stores the employee's name       | Public            |
| `_hour`   | Stores working hours             | Protected-style   |
| `__dept`  | Stores the employee's department | Private-style     |

**Note:** In Python, a single leading underscore indicates a non-public implementation detail by convention. A double leading underscore triggers name mangling; it does not provide strict privacy.

### 2. Getter (`@property`)

The getter allows the attributes to be accessed through `b.data` without explicitly calling a method.

```python
@property
def data(self):
    return (
        getattr(self, "TE", "employee_data"),
        getattr(self, "name", "name_data"),
        getattr(self, "_hour", "Hour_data"),
        getattr(self, "__dept", "dept_data")
    )
```

The `getattr()` function retrieves an attribute by name. If the requested attribute does not exist, it returns the specified default value.

**Important:** Because `__dept` is name-mangled by Python, `getattr(self, "__dept", "dept_data")` does not retrieve the department attribute created by the constructor. The actual attribute name is `_Bank__dept`.

### 3. Setter (`@data.setter`)

The setter updates all four attributes through a single assignment.

```python
@data.setter
def data(self, values):
    self.TE, self.name, self._hour, self.__dept = values
```

Example:

```python
b.data = (500, "Allen", 8, "Sales")
```

This updates the employee-related data, name, working hours, and department.

### 4. Deleter (`@data.deleter`)

The deleter removes the specified attributes when `del b.data` is executed.

```python
@data.deleter
def data(self):
    del self.name, self.__dept
```

Example:

```python
del b.data
```

This deletes `name` and `__dept`. It does not delete `TE` or `_hour`.

**Important:** After deletion, accessing `b.data` still works, but the getter returns default values for the deleted attributes. In the original code, the department value also resolves to the default because of the name-mangling issue described above.

## ▶️ Expected Output

```text
(250, 'Smith', 9, 'dept_data')
(500, 'Allen', 8, 'dept_data')
(500, 'name_data', 8, 'dept_data')
```

The department displays `'dept_data'` rather than `'Finance'` or `'Sales'` because the getter uses `"__dept"` instead of the name-mangled attribute name.

## 🚀 How to Run

### Prerequisites

Install Python 3 on your system.

### Steps

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the Python file:

```bash
python bank.py
```

On some systems, you may need to use:

```bash
python3 bank.py
```

## 📚 Key Learnings

By completing this project, you will learn:

* How property decorators provide controlled attribute access.
* How getters, setters, and deleters work in Python.
* How to update multiple attributes through tuple unpacking.
* How `getattr()` provides default values for missing attributes.
* How Python's name mangling affects double-underscore attributes.
* Why understanding attribute deletion is important when designing classes.

## 🔧 Possible Improvements

* Use `_Bank__dept` in the getter to retrieve the department correctly, or use a single-underscore attribute if strict privacy is unnecessary.
* Validate the number and types of values received by the setter.
* Delete all four attributes in the deleter if that is the intended behavior.
* Add exception handling to make the class more robust.
* Rename `TE` and `Mname` to clearer identifiers, such as `employee_id` and `name`.

## 👨‍💻 Author

**Python OOP Practice Project**

Created to practise Object-Oriented Programming concepts and property decorators in Python.

---

⭐ If you find this project useful for learning Python, consider starring the repository on GitHub.
