import psycopg2
from urllib.parse import quote

# Database connection parameters
PG_PORT = "5432"
PG_DB = "test"  # Your database name
PG_USER = "postgres"
PG_PASSWORD_RAW = "Shivani@12345"
PG_PASSWORD = quote(PG_PASSWORD_RAW)
PG_HOST = "localhost"

# Create a connection string
PG_CONNECTION_STRING = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"

# ✅ Show connection string (mask password)
print("Connection String:", PG_CONNECTION_STRING.replace(PG_PASSWORD, "******"))

# ✅ Try to connect once when DB.py runs to show message
try:
    test_connection = psycopg2.connect(PG_CONNECTION_STRING)
    print("✅ Connected to the database successfully!")  # ← You want this here
    test_connection.close()
except Exception as e:
    print("❌ Failed to connect to the database:", e)

# ✅ Function to execute a query
def execute_query(query, values=None, fetch=False):
    try:
        connection = psycopg2.connect(PG_CONNECTION_STRING)
        cursor = connection.cursor()
        cursor.execute(query, values)

        if fetch:
            result = cursor.fetchall()
        else:
            result = None
            connection.commit()

        cursor.close()
        connection.close()
        return result

    except Exception as e:
        print("❌ Database error during query:", e)
        return None
