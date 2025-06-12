import streamlit as st
from businesslogic import (
    create_event,
    add_guest_to_event,
    view_guest_list,
    rsvp_summary,
    events_with_no_guests,
    search_guest_by_email
)

# Streamlit Page Config
st.set_page_config(page_title="📋 DataSense Event Planner", layout="centered")
st.title("📋 Welcome to DataSense Event Planner")

# Menu options
menu_options = [
    "Create New Event",
    "Add Guest to Event",
    "View Guest List",
    "Show RSVP Summary",
    "Show Events with No Guests",
    "Search Guest by Email",
]

# Sidebar Navigation
choice = st.sidebar.radio("Navigation", menu_options)

# Mapping functions to UI
if choice == "Create New Event":
    st.subheader("➕ Create New Event")
    create_event()

elif choice == "Add Guest to Event":
    st.subheader("👥 Add Guest to Event")
    add_guest_to_event()

elif choice == "View Guest List":
    st.subheader("📜 View Guest List")
    view_guest_list()

elif choice == "Show RSVP Summary":
    st.subheader("📊 RSVP Summary")
    rsvp_summary()

elif choice == "Show Events with No Guests":
    st.subheader("🚫 Events with No Guests")
    events_with_no_guests()

elif choice == "Search Guest by Email":
    st.subheader("🔍 Search Guest by Email")
    search_guest_by_email()

# Footer
st.markdown("---")
st.caption("Crafted with ❤️ by Shivani using Streamlit")
