import psycopg2
from DB import execute_query
from utils import (
    get_valid_date,
    get_non_empty_input,
    get_valid_email,
    get_valid_rsvp,
    get_valid_int
)

# 🔹 Create a new event
def create_event():
    name = get_non_empty_input("Event name: ")
    date = get_valid_date()
    location = get_non_empty_input("Location: ")

    query = "INSERT INTO events (event_name, event_date, location) VALUES (%s, %s, %s)"
    execute_query(query, (name, date, location))
    print("✅ Event created successfully!")

# 🔹 Show all events
def show_all_events():
    events = execute_query("SELECT event_id, event_name, event_date, location FROM events", fetch=True)
    if not events:
        print("❌ No events found.")
        return False

    print("\n📅 Available Events:")
    for e in events:
        print(f"ID: {e[0]}, Name: {e[1]}, Date: {e[2]}, Location: {e[3]}")
    return True

# 🔹 Add guest to an event
def add_guest_to_event():
    if not show_all_events():
        return

    event_id = get_valid_int("Enter event ID: ")
    name = get_non_empty_input("Guest name: ")
    email = get_valid_email()
    rsvp = get_valid_rsvp()

    query = "INSERT INTO guests (event_id, name, email, rsvp_status) VALUES (%s, %s, %s, %s)"
    try:
        execute_query(query, (event_id, name, email, rsvp))
        print("✅ Guest added successfully!")
    except psycopg2.errors.UniqueViolation:
        print("⚠️ Guest with this email already exists for this event.")
    except Exception as e:
        print("❌ Error adding guest:", e)

# 🔹 View guest list
def view_guest_list():
    if not show_all_events():
        return

    event_id = get_valid_int("Enter event ID to view guests: ")
    query = "SELECT * FROM guests WHERE event_id = %s"
    guests = execute_query(query, (event_id,), fetch=True)

    if guests:
        print(f"\n👥 Guest list for event ID {event_id}:")
        for g in guests:
            print(f"Name: {g[2]}, Email: {g[3]}, RSVP: {g[4]}")
    else:
        print("No guests found for this event.")

# 🔹 Show RSVP summary
def rsvp_summary():
    event_id = get_valid_int("Enter event ID for RSVP summary: ")
    query = """SELECT rsvp_status, COUNT(*) FROM guests 
               WHERE event_id = %s GROUP BY rsvp_status"""
    results = execute_query(query, (event_id,), fetch=True)

    if results:
        print(f"\n📊 RSVP Summary for Event ID {event_id}:")
        for r in results:
            print(f"{r[0]}: {r[1]}")
    else:
        print("No RSVP data found.")

# 🔹 Events with no guests
def events_with_no_guests():
    query = """
    SELECT e.event_id, e.event_name, e.event_date, e.location
    FROM events e LEFT JOIN guests g ON e.event_id = g.event_id
    WHERE g.guest_id IS NULL
    """
    results = execute_query(query, fetch=True)

    if results:
        print("\n🛑 Events with no guests:")
        for e in results:
            print(f"ID: {e[0]}, Name: {e[1]}, Date: {e[2]}, Location: {e[3]}")
    else:
        print("🎉 All events have guests.")

# 🔹 Search guest by email
def search_guest_by_email():
    email = get_valid_email()
    query = """
    SELECT g.name, e.event_name, g.rsvp_status
    FROM guests g JOIN events e ON g.event_id = e.event_id
    WHERE g.email = %s
    """
    results = execute_query(query, (email,), fetch=True)

    if results:
        print(f"\n🔍 Guest details for {email}:")
        for r in results:
            print(f"Name: {r[0]}, Event: {r[1]}, RSVP: {r[2]}")
    else:
        print("No guest found with this email.")
