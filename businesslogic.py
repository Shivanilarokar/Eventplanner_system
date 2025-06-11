
from DB import execute_query
# create a new event
def create_event():
    event_name = input("Enter event name: ")
    event_date = input("Enter event date (YYYY-MM-DD): ")
    location = input("Enter event location: ")

    query = "INSERT INTO events (event_name, event_date, location) VALUES (%s, %s, %s)"
    values = (event_name, event_date, location) 
    execute_query(query, values)
    print("Event created successfully!")

# add a guest to an event
def add_guest_to_event():
    event_id = input("Enter event ID: ")
    Guest_name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    rsvp_status = input("Enter RSVP status (yes/no/Maybe): ").capitalize()

    query = "INSERT INTO guests (event_id, name, email, rsvp_status) VALUES (%s, %s, %s, %s)"
    values = (event_id, Guest_name, email, rsvp_status)
    execute_query(query, values)
    print("Guests added successfully!")


# view guest list for an event
def view_guest_list():
    event_id = input("Enter event ID to view guest list: ")

    query = "SELECT * FROM guests WHERE event_id = %s"
    values = (event_id,)
    results = execute_query(query, values, fetch=True)

    if results:
        print(f"Guest list for event ID {event_id}:")
        for row in results:
            print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, RSVP Status: {row[3]}")
    else:
        print("No guests found for this event.")

# Show RSVP summery 
def rsvp_summary():
    event_id = input("Enter event ID to view RSVP summary: ")

    query = """
    SELECT rsvp_status, COUNT(*) FROM guests 
    WHERE event_id = %s 
    GROUP BY rsvp_status
    """
    values = (event_id,)
    results = execute_query(query, values, fetch=True)

    if results:
        print(f"RSVP summary for event ID {event_id}:")
        for row in results:
            print(f"RSVP Status: {row[0]}, Count: {row[1]}")
    else:
        print("No RSVP data found for this event.")

# events with no guests
def events_with_no_guests():
    query = """
    SELECT e.event_id, e.event_name, e.event_date, e.location 
    FROM events e 
    LEFT JOIN guests g ON e.event_id = g.event_id 
    WHERE g.guest_id IS NULL
    """
    results = execute_query(query, fetch=True)

    if results:
        print("Events with no guests")
        for row in results:
            print(f"Event ID: {row[0]}, Name: {row[1]}, Date: {row[2]}, Location: {row[3]}")
    else:
        print("All events have guests.")

# search guest by email
def search_guest_by_email():
    email = input("Enter guest email to search: ")

    query = """SELECT g.name, e.event_name, g.rsvp_status
    FROM guests g JOIN events e ON g.event_id = e.event_id
    WHERE g.email = %s;"""
    values = (email,)
    results = execute_query(query, values, fetch=True)

    if results:
        print(f"Guest details for email {email}:")
        for row in results:
            print(f"ID: {row[0]}, Event ID: {row[1]}, Name: {row[2]}, RSVP Status: {row[3]}")
    else:
        print("No guest found with this email.") 

    
