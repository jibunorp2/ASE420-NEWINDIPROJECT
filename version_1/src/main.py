import argparse
import datetime

import backend


def todoapp():
    stringParser = argparse.ArgumentParser(description='Time Tracker CLI')
    subparsers = stringParser.add_subparsers(dest='command', help='Available commands')

    record_parser = subparsers.add_parser('record', help='Record time usage')
    record_parser.add_argument('date', action="store", help='Input date in the format YYYY/MM/DD or "today"')
    record_parser.add_argument('start_time', action="store", help='Input Start Time in HH:MM format')
    record_parser.add_argument('end_time', action="store", help='Input Ending time in HH:MM format')
    record_parser.add_argument('task', action="store", help='Input Task Description')
    record_parser.add_argument('tag', action="store", help='Input Tag')

    query_parser = subparsers.add_parser('query', help='Query time usage')
    query_parser.add_argument('query', help='Query string')

    report_parser = subparsers.add_parser('report', help='Generate time usage report')
    report_parser.add_argument('start_date', help='Start date in the format YYYY/MM/DD')
    report_parser.add_argument('end_date', help='End date in the format YYYY/MM/DD')

    subparsers.add_parser('priority', help='Get priority task list')

    subparsers.add_parser('clear', help='Clear the database')

    args = stringParser.parse_args()
    if args.command == 'query':
        handle_query(args.query)
    elif args.command == 'record':
        # Validate and format the date input for recording
        if args.date.lower() == 'today':
            record_date = datetime.date.today()
        else:
            try:
                record_date = datetime.datetime.strptime(args.date, "%Y/%m/%d").date()
            except ValueError:
                print("Invalid date format. Please use the format YYYY/MM/DD.")
                return

        # Validate and format the start and end time inputs
        # try:
        #     # start_time = datetime.datetime.strptime(args.start_time, "%H:%M").time()
        #     # end_time = datetime.datetime.strptime(args.end_time, "%H:%M").time()
        # except ValueError:
        #     print("Invalid time format. Please use the 24-hour format HH:MM.")
        #     return

        backend.insertdata(record_date, args.start_time, args.end_time, args.task, args.tag)
        print('Stored Successfully')
    elif args.command == 'report':
        # Handle report command
        pass
    elif args.command == 'priority':
        # Handle priority command
        pass
    elif args.command == 'clear':
        backend.drop_table()
        pass


def handle_query(query_string):
    # Call the function in backend.py to fetch and print data based on the query
    # result = backend.query_by_tag(query_string)
    # print_result(result)
    if ':' in query_string:
        result = backend.query_by_tag(query_string)
    elif '/' in query_string:
        try:
            query_date = datetime.datetime.strptime(query_string, "%Y/%m/%d").date()
        except ValueError:
            print("Invalid date format. Please use the format YYYY/MM/DD.")
            return
        result = backend.query_by_date(query_date)
    elif query_string == 'today':
        result = backend.query_by_date(datetime.date.today())
    else:
        result = backend.query_by_task(query_string)
    print_result(result)


def print_result(result):
    # Print the fetched data
    for row in result:
        print(row)

    # if hasattr(args, 'date') and args.date.lower() == 'today':
    #     args.date = datetime.date.today()
    # elif hasattr(args, 'date'):
    #     args.date = pc.parse(str(args.date)).date()
    #
    # if args.command == 'record':
    #     backend.insertdata(args.date, args.start_time, args.end_time, args.task, args.tag)
    #     print('Stored Successfully')
    # if args.command == 'query':
    #     # Query by tag using LIKE for partial matches
    #     results = backend.query_by_tag(f"%{hasattr(args, 'tag')}%")
    #     print("Query Results:")
    #     for row in results:
    #         print(row)
    #
    # def display_data():
    #     print("Stored Data:")
    #     for row in backend.view():
    #         print(row)

    # display_data()


if __name__ == "__main__":
    todoapp()
