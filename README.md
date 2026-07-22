# Python CLI Alarm Clock

A simple, modular command-line Alarm Clock application built in Python.

The application allows users to create, view, and delete alarms while continuously monitoring scheduled alarms in the background. The solution focuses on clean architecture, maintainability, and engineering best practices rather than unnecessary features.

---

# Features

* Add alarms using `HH:MM` (24-hour) format
* View all scheduled alarms
* Delete existing alarms
* Prevent duplicate alarms
* Automatically sort alarms by time
* Background scheduler using threads
* Trigger each alarm only once
* Input validation with user-friendly error messages
* Modular and extensible project structure
* Unit tests for core functionality

---

# Project Structure

```text
alarm-clock-cli/
│
├── alarm_clock/
│   ├── __init__.py
│   ├── alarm.py
│   ├── alarm_manager.py
│   ├── scheduler.py
│   ├── cli.py
│   └── utils.py
│
├── tests/
│   └── test_alarm.py
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# Requirements

* Python 3.10 or later
* No external libraries required

---

# Installation

Clone the repository.

```bash
git clone <repository-url>
cd alarm-clock-cli
```

No additional packages are required.

---

# Running the Application

Start the application by running:

```bash
python main.py
```

You will see the interactive menu:

```text
==================================================
        PYTHON CLI ALARM CLOCK
==================================================
1. Add Alarm
2. View Alarms
3. Delete Alarm
4. Exit
==================================================
```

---

# Usage

## Add Alarm

Choose:

```text
1
```

Enter the alarm time in 24-hour format:

```text
07:30
```

Example output:

```text
Alarm scheduled for 07:30
```

---

## View Alarms

Choose:

```text
2
```

Example:

```text
Scheduled Alarms

1. 07:30    Pending
2. 18:00    Pending
```

---

## Delete Alarm

Choose:

```text
3
```

Select the alarm number to remove.

Example:

```text
Enter alarm number to delete: 1

Alarm deleted successfully.
```

---

# Architecture

The application follows a modular design with clear separation of responsibilities.

```text
main.py
   │
   ▼
AlarmCLI
   │
   ▼
AlarmManager
   │
   ▼
Alarm
   │
   ▼
Scheduler
```

## Component Responsibilities

### main.py

* Starts the application
* Displays the menu
* Starts the background scheduler

### AlarmCLI

Responsible only for user interaction.

* Reads user input
* Displays messages
* Delegates business logic to the AlarmManager

### AlarmManager

Contains all business logic.

Responsibilities:

* Add alarms
* Delete alarms
* List alarms
* Validate duplicate alarms
* Keep alarms sorted

### Alarm

Represents a single alarm object.

Stores:

* Alarm time
* Trigger status

### Scheduler

Runs in a background daemon thread.

Responsibilities:

* Continuously monitor alarms
* Trigger alarms when scheduled
* Prevent duplicate triggering

### utils.py

Contains helper functions.

Currently responsible for:

* Parsing and validating alarm time

---

# Design Decisions

Several design decisions were made to keep the solution simple, maintainable, and aligned with the assignment requirements.

## Object-Oriented Design

Each alarm is represented as an object using a Python dataclass, making the model clean and easy to extend.

## Separation of Concerns

Business logic is isolated inside `AlarmManager`, while the CLI only handles user interaction. This keeps the code easier to maintain and test.

## Background Scheduler

The scheduler runs in a daemon thread, allowing alarm monitoring to continue while the application remains responsive to user input.

## In-Memory Storage

Alarms are stored in memory because the assignment explicitly requested a CLI application without requiring database persistence.

## Standard Library Only

The application uses only Python's standard library, avoiding unnecessary dependencies while keeping setup simple.

---

# Validation

The application validates user input before creating alarms.

Examples of rejected input:

```text
99:99
25:00
07-30
abcd
7:3
```

Duplicate alarms are also prevented.

---

# Testing

Unit tests are included for the core functionality.

Run all tests using:

```bash
python -m unittest discover tests
```

Current tests cover:

* Valid alarm creation
* Invalid time format
* Duplicate alarm prevention
* Invalid delete operations

---

# Error Handling

The application handles common user errors gracefully.

Examples include:

* Invalid time format
* Duplicate alarms
* Invalid menu choices
* Invalid delete selection
* Empty alarm list

---

# AI Usage

AI was used as a development assistant during the implementation process.

It helped with:

* Reviewing project architecture
* Improving code organization
* Identifying edge cases
* Suggesting refactoring opportunities
* Improving documentation
* Reviewing code quality

All generated suggestions were manually reviewed, validated, and adapted before being incorporated into the final implementation.

---

# Assumptions

* Time is entered in 24-hour format (`HH:MM`).
* Alarms exist only while the application is running.
* Each alarm triggers only once.
* If the entered time has already passed for the current day, the alarm is scheduled for the next day.

---

# Future Improvements

Given additional time, the following enhancements could be implemented:

* Persistent alarm storage (JSON or SQLite)
* Recurring alarms
* Snooze functionality
* Custom alarm labels
* Sound notifications
* Logging
* Configuration file support
* Additional unit and integration tests

---

# Engineering Trade-offs

The focus of this implementation was maintainability, readability, and clean separation of responsibilities rather than maximizing the number of features.

Instead of introducing external dependencies or persistent storage, the application keeps alarms in memory and relies solely on Python's standard library. This keeps the solution lightweight while still demonstrating sound software engineering principles.

---

# Conclusion

This project demonstrates a modular, maintainable, and extensible Python CLI application that satisfies the assignment requirements while following clean coding practices and software design principles.
