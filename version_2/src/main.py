import argparse
from datetime import datetime, date, timedelta
import backend


def validate_and_format_time(time_str):
    try:
        return datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        try:
            return datetime.strptime(time_str, "%I:%M%p").time()
        except ValueError:
            print("Invalid time format. Please use the format HH:MM or H:MMAM/PM.")
            return None

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

    report_parser = subparsers.add_parser('report', help='Generate a report')
    report_parser.add_argument('start_date', help='Start date in the format YYYY/MM/DD')
    report_parser.add_argument('end_date', help='End date in the format YYYY/MM/DD')

    subparsers.add_parser('priority', help='Get priority task list')

    args = stringParser.parse_args()
    parse_command(args)


def parse_command(args):
    if args.command == 'query':
        handle_query(args.query)
    elif args.command == 'record':
        record_date = validate_and_format_date(args.date)
        if record_date:
            backend.insertdata(record_date, args.start_time, args.end_time, args.task, args.tag)
            print('Stored Successfully')
    elif args.command == 'report':
        handle_report(args.start_date, args.end_date)
    elif args.command == 'priority':
        result = handle_priority()
        print_result(result)
    elif args.command == 'clear':
        backend.drop_table()


def handle_priority():
    return backend.query_top_3_priority()
def handle_report(start_date, end_date):
    start_date = validate_and_format_date(start_date)
    end_date = validate_and_format_date(end_date)

    if not start_date or not end_date:
        return

    delta = end_date - start_date
    for i in range(delta.days + 1):
        current_date = start_date + timedelta(days=i)
        result = backend.query_by_date(current_date)

        if result:
            print_result(result)
            print()


def validate_and_format_date(date_str):
    if date_str.lower() == 'today':
        return date.today()
    try:
        return datetime.strptime(date_str, "%Y/%m/%d").date()
    except ValueError:
        print("Invalid date format. Please use the format YYYY/MM/DD.")
        return None


def handle_query(query_string):
    if ':' in query_string:
        result = backend.query_by_tag(query_string)
    elif '/' in query_string:
        query_date = validate_and_format_date(query_string)
        if query_date:
            result = backend.query_by_date(query_date)
        else:
            return
    elif query_string == 'today':
        result = backend.query_by_date(date.today())
    else:
        result = backend.query_by_task(query_string)
    print_result(result)


def print_result(result):
    for row in result:
        print(row)


if __name__ == "__main__":
    todoapp()
