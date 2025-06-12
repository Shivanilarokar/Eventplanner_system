# 📋 DataSense EventPlanner — Event & Guest Manager CLI App

**DataSense EventPlanner** is a command-line application built with Python and PostgreSQL to help individuals or small teams seamlessly plan events, manage guest lists, and track RSVPs — all from a simple and intuitive menu interface.

---

## 🌟 Why I Built This

Event planning can be messy — tracking who’s coming, which events have low engagement, or simply organizing multiple guest lists quickly becomes chaotic in spreadsheets.

This project was my way to:

- Learn **how databases work in real projects**
- Use Python to build real-world integration & automation.
- Understand **how business logic is separated** from UI

---

## 💼 What Problem It Solves

Event planners, HR teams, college clubs, or anyone managing small events need quick answers:

- How many people RSVP’ “Yes”?
- Which event has no guests?
- Who is attending Event X?
- Events with no guest
- guest list


This tool gives you that — instantly — through a simple CLI app powered by Python and PostgreSQL.

---

## 🚀 Key Features

✅ **Create New Events**  
Provide event name, date, and location. Dates are validated in `YYYY-MM-DD` format.

✅ **Add Guests with RSVP**  
Add guest name, email, and RSVP status (`Yes`, `No`, `Maybe`) — with validation and duplicate email check per event.

✅ **View Guest List per Event**  
See who is attending any event, with full details.

✅ **RSVP Summary**  
Get a quick breakdown of how many people RSVP’d “Yes”, “No”, or “Maybe”.

✅ **Find Events with No Guests**  
Spot underperforming or forgotten events quickly.

✅ **Search Guest by Email**  
Find out which events a guest is attending and their RSVP status.

---

## 🧠 How It Works

1. App starts with a **menu-driven CLI interface** (in `main.py`)
2. All logic like event creation, RSVP summary, and guest insertion is handled in `businesslogic.py`
3. Inputs (like date, email, status) are validated through utility functions in `utils.py`
4. PostgreSQL handles data storage and is accessed via `db.py` using `psycopg2`

Everything is modular and maintainable — making the system easy to extend in the future.

---

## 🔍 Input Validations

✅ **Dates**: Checked for format `YYYY-MM-DD`  
✅ **Emails**: Regex-based email format validation  
✅ **RSVP Options**: Only accepts `Yes`, `No`, or `Maybe`  
✅ **Text Fields**: Empty strings are rejected  
✅ **Event IDs**: Must be numeric  
✅ **Duplicate Guest Entries**: Blocked using unique `(event_id, email)` combo

All handled gracefully with meaningful CLI error messages and re-prompts.

---

## 🛠️ Tools & Libraries

- **Python 3.10+**
- **PostgreSQL**
- `psycopg2` – PostgreSQL adapter for Python
- **CLI interface** with user-friendly prompts and validations

---

## 🎯 What I Learned

- How to build an **end-to-end functional CLI app** with a real database
- Writing **clean, readable, and reusable** functions
- Handling **database constraints and exceptions**
- Real-time validation of user input

---

## 💬 Feedback & Contributions

I’d love to hear your thoughts!  
Feel free to raise issues, suggest features, or fork the project.

