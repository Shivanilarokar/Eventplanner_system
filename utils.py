from datetime import datetime
import re

def get_valid_date(prompt="Date (YYYY-MM-DD): "):
    while True:
        d = input(prompt)
        try:
            datetime.strptime(d, "%Y-%m-%d")
            return d
        except: print("❌ Format must be YYYY-MM-DD.")

def get_non_empty_input(prompt="Enter value: "):
    while True:
        val = input(prompt).strip()
        if val: return val
        print("❌ Cannot be empty.")

def get_valid_email(prompt="Enter email: "):
    while True:
        e = input(prompt).strip()
        if re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', e): return e
        print("❌ Invalid email.")

def get_valid_rsvp(prompt="RSVP (Yes/No/Maybe): "):
    while True:
        r = input(prompt).capitalize()
        if r in {"Yes", "No", "Maybe"}: return r
        print("❌ Choose Yes / No / Maybe.")

def get_valid_int(prompt="Enter number: "):
    while True:
        n = input(prompt)
        if n.isdigit(): return int(n)
        print("❌ Only digits allowed.")
