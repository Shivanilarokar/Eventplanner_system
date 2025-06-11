# validate date input in the format YYYY-MM-DD
from datetime import datetime

def input_date(date):
    while True:
        try:
            date_str = input(date)
            return datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            print("❌ Invalid format. Please use YYYY-MM-DD.") 
