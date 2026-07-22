# Python CLI Alarm Clock

## Overview

This project is a simple Alarm Clock application built using Python as a Command Line Interface (CLI) application. The objective was to build a clean, maintainable solution while making appropriate engineering decisions within a limited time.

The application runs entirely in the terminal and does not use a web interface, database, or external frameworks.

---

# Problem Statement

Build a Python CLI Alarm Clock application that allows users to create and manage alarms. Since the assignment does not include a detailed specification, the scope and implementation decisions were defined before development.

---

# Requirements

The application should allow users to:

* Create an alarm
* View all alarms
* Delete an alarm
* Notify the user when an alarm time is reached
* Exit the application gracefully

---

# Non-Functional Requirements

* Python CLI application only
* No web UI
* No React
* No database
* Clean and modular code
* Easy to understand and maintain
* Input validation for user entries

---

# Assumptions

To keep the project focused and complete within the given time, the following assumptions were made:

* Alarms are stored only in memory.
* Alarm data is lost once the application exits.
* Alarm precision is one minute.
* Multiple alarms are supported.
* Internet access is not required.

---

# Features

* Add a new alarm
* View all scheduled alarms
* Delete an existing alarm
* Automatic alarm notification
* Input validation
* Graceful application exit

---

# Features Not Included

The following features were intentionally excluded because they were outside the scope of this exercise:

* Persistent storage
* Snooze functionality
* Recurring alarms
* Custom alarm sounds
* Time zone support
* Graphical User Interface (GUI)

---

# Architecture

The application follows a simple modular architecture.

```text
User
   │
   ▼
CLI Interface
   │
   ▼
Alarm Manager
   │
   ▼
Scheduler
   │
   ▼
Console Notification
```

---

# Engineering Decisions

### Why CLI?

The assignment explicitly requested a Command Line Interface application.

### Why No Database?

The assignment specifically stated that no database should be used. Therefore, alarms are maintained in memory during execution.

### Why In-Memory Storage?

Since persistence was not required, storing alarms in memory keeps the implementation lightweight and avoids unnecessary complexity.

### Why Modular Design?

Separating the CLI, alarm management, scheduler, and utility logic improves readability, maintainability, and future extensibility.

### Why Python Standard Library?

The implementation primarily relies on Python's standard library to minimize dependencies while providing reliable functionality.

---

# AI Usage

AI was used during the planning and development process to improve productivity and engineering quality.

AI assisted with:

* Refining project requirements
* Discussing possible architecture
* Creating an implementation plan
* Reviewing implementation ideas
* Identifying edge cases
* Improving documentation

All AI-generated suggestions were reviewed, validated, and adapted before being included in the final solution.

---

# Project Structure

```text
alarm-clock-cli/
│
├── alarm_clock/
│   ├── alarm.py
│   ├── scheduler.py
│   ├── cli.py
│   ├── utils.py
│   └── __init__.py
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

# How to Run

1. Clone the repository.

2. Navigate to the project directory.

3. Run the application.

```bash
python main.py
```

---

# Example Workflow

```text
1. Add Alarm
2. View Alarms
3. Delete Alarm
4. Exit

Choose an option: 1

Enter alarm time (HH:MM): 07:30

Alarm added successfully.
```

When the scheduled time is reached:

```text
********************************
ALARM!
Time: 07:30
Wake up!
********************************
```

---

# Testing

The application will be tested for:

* Valid time format
* Invalid time format
* Multiple alarms
* Alarm deletion
* Alarm triggering
* Invalid menu selection

---

# Limitations

* Alarm data is not saved after the application exits.
* Notifications are displayed only in the terminal.
* Alarm precision is limited to one minute.

---

# Future Improvements

Given additional development time, the following enhancements could be implemented:

* Persistent storage using a file or database
* Snooze functionality
* Recurring alarms
* Custom notification sounds
* Desktop notifications
* Time zone support
* Configuration file support
* Automated test coverage

---

# Conclusion

The primary objective of this project was to demonstrate engineering decision-making, clean architecture, modular implementation, and effective use of AI during the software development process, rather than maximizing the number of features.
