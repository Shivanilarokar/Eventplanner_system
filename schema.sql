CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    event_name VARCHAR(100),
    event_date DATE,
    location VARCHAR(100)
);

CREATE TABLE guests (
    guest_id SERIAL PRIMARY KEY,
    event_id INT REFERENCES events(event_id),
    name VARCHAR(100),
    email VARCHAR(100),
    rsvp_status VARCHAR(10),
    UNIQUE (event_id, email)
);
