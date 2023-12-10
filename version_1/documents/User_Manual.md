# User Manual

### What to Expect:

This is an application that allows the user to track their time based on the input of ‘record, date, start time, end time, task, tag’. And the input will be stored and if the user wants to look back, they can query based on:

1. TAG
2. Date
3. Task

### User Input:

For the user to input their time manage they input the following:

```jsx
python3 file_name.py record date start_time end_time 'task' :TAG
```

For the user to query:

```jsx
python3 file_name.py query :STUDY
python3 file_name.py query 2023/12/10
python3 file_name.py query task
```

Record will allow the users inputs to be stored.

Query will allow the users inputs to be searched.