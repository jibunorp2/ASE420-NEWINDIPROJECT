# User Manual (User)

# **Time Tracker CLI User Manual**

## **Table of Contents**

1. **Introduction**
    - Overview
    - Prerequisites
2. **Usage**
    - Command Line Arguments
    - Commands
    - Examples
3. **Database Management**
    - Database Setup
    - Data Retrieval
4. **Testing**
    - Running Unit Tests
    - Adding Tests
5. **Contributing**
    - Bug Reports
    - Feature Requests
    - Pull Requests
6. Troubleshooting

## **1. Introduction**

### **Overview**

The Time Tracker CLI is a command-line interface application written in Python using the SQLite database. It allows users to record and track time usage, generate reports, and manage tasks efficiently.

### **Prerequisites**

- Python 3.6 or higher
- SQLite3

## 2**. Usage**

### **Command Line Arguments**

The CLI uses command-line arguments for various functionalities. Here are the available commands:

- **`record`**: Record time usage
- **`query`**: Query time usage based on task, date, or tag

### **Examples**

### Record Time Usage

```bash

python main.py record 2023/01/01 09:00 17:00 "Task description" "Tag"

```

### Generate a query

```bash

python main.py query Tag
```

## **4. Database Management**

### **Database Setup**

The application uses SQLite3 for data storage. The database file (**`main.db`**) is created automatically upon the first run.

### **Data Retrieval**

You can retrieve data from the database using the **`backend.py`** functions. For example:

```python
pythonCopy code
import backend # Get all records all_records = backend.view() # Query by tag tag_records = backend.query_by_tag("Tag") # Query by date date_records = backend.query_by_date("2023/01/01")

```

## 6**. Support**

### **Support**

For any issues or questions, feel free to reach out to jibunorp2@nku.edu.