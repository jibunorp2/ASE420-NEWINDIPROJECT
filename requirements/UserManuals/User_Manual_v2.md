# User Manual (User)

# **Time Tracker CLI User Manual**

## **Table of Contents**

1. **Introduction**
    - Overview
    - Features
2. **Installation**
    - Prerequisites
    - Download and Setup
3. **Getting Started**
    - Basic Commands
    - Recording Time
    - Generating Reports
4. **Additional Functionalities**
    - Querying Time Usage
    - Managing Tasks
    - Database Management
5. **Support**

## **1. Introduction**

### **Overview**

The Time Tracker CLI is a command-line interface application designed to help you record and manage your time usage efficiently. Whether you're tracking work hours or personal tasks, this tool provides a simple and effective way to organize your time.

### **Features**

- Record time usage with start and end times, task descriptions, and tags.
- Generate detailed reports for a specific date range.
- Prioritize tasks based on time spent.

## **2. Installation**

### **Prerequisites**

- Python 3.6 or higher
- SQLite3

### **Download and Setup**

1. **Clone the Repository:**
    
    ```bash
    
    git clone https://github.com/your-username/time-tracker-cli.git cd time-tracker-cli
    
    ```
    
2. **Install Dependencies:**
    
    ```bash
    
    pip install -r requirements.txt
    
    ```
    

## **3. Getting Started**

### **Basic Commands**

The Time Tracker CLI supports the following basic commands:

- **`record`**: Record time usage
- **`query`**: Query time usage
- **`report`**: Generate a report
- **`priority`**: Get priority task list
- **`clear`**: Drop the entire database table

### **Recording Time**

To record time usage, use the following command format:

```bash

python main.py record [date] [start_time] [end_time] "[task_description]" "[tag]"

```

### **Generating Reports**

Generate a report for a specific date range using the following command:

```bash

python main.py report [start_date] [end_date]

```

## **4. Additional Functionalities**

### **Querying Time Usage**

You can query time usage based on various criteria:

- By tag: **`python main.py query "[tag]"`**
- By date: **`python main.py query [date]`**
- By task: **`python main.py query "[task]"`**

### **Managing Tasks**

- To get the top 3 priority tasks: **`python main.py priority`**

### **Database Management**

The application manages data using an SQLite database. The database is automatically created upon the first run.

## **5. Support**

### **Support**

For any issues or questions, feel free to reach out to [[jibunorp2@nku.edu](mailto:your-email@example.com)].