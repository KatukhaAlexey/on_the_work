from datetime import datetime
def calculate_salary(year, month, day, salary):
    date1 = datetime(year, month, day)
    date2 = datetime.now()
    return salary * (date2 - date1).days
