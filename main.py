from models import create_event, add_guest, view_guest_list, rsvp_summary, events_no_guests, search_guest_by_email

def menu():
    while True:
        print("""
📋 Welcome to DataSense Event Planner!
1. Create New Event
2. Add Guest to Event
3. View Guest List
4. Show RSVP Summary
5. Show Events with No Guests
6. Search Guest by Email
7. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_event()
        elif choice == "2":
            add_guest()
        elif choice == "3":
            view_guest_list()
        elif choice == "4":
            rsvp_summary()
        elif choice == "5":
            events_no_guests()
        elif choice == "6":
            search_guest_by_email()
        elif choice == "7":
            print("👋 Exiting. Bye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
