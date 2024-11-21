# import sqlite3

# # Connect to the database
# conn = sqlite3.connect("forms.db")
# c = conn.cursor()

# # Create a table for form data if it doesn't exist
# c.execute(
#     """CREATE TABLE IF NOT EXISTS form_data
#              (form_name TEXT, field_name TEXT, field_value TEXT)"""
# )


# def save_to_db(form_name, field_name, field_value):
#     c.execute(
#         "INSERT INTO form_data (form_name, field_name, field_value) VALUES (?, ?, ?)",
#         (form_name, field_name, field_value),
#     )
#     conn.commit()


# # Function to view the data
# def view_database():
#     c.execute("SELECT * FROM form_data")
#     rows = c.fetchall()

#     # Display the rows
#     if rows:
#         print("Form Data:")
#         for row in rows:
#             print(f"Form Name: {row[0]}, Field Name: {row[1]}, Field Value: {row[2]}")
#     else:
#         print("No data found.")


# # Close the connection at the end
# def close_connection():
#     conn.close()


# # Example usage to view database
# if __name__ == "__main__":
#     view_database()  # View the current data
#     close_connection()  # Ensure the database connection is closed after use

# database.py

import sqlite3

# Connect to the database
conn = sqlite3.connect("forms.db")
c = conn.cursor()

# Create a table for form data if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS form_data
             (user_id TEXT, form_name TEXT, field_name TEXT, field_value TEXT)"""
)


def save_to_db(user_id, form_name, field_name, field_value):
    c.execute(
        "INSERT INTO form_data (user_id, form_name, field_name, field_value) VALUES (?, ?, ?, ?)",
        (user_id, form_name, field_name, field_value),
    )
    conn.commit()


def get_user_data(user_id, form_name):
    """Retrieve user data for a specific form."""
    c.execute(
        "SELECT field_name, field_value FROM form_data WHERE user_id = ? AND form_name = ?",
        (user_id, form_name),
    )
    return dict(c.fetchall())


# Function to view the data# Function to view the data
def view_database():
    c.execute("SELECT * FROM form_data")
    rows = c.fetchall()

    # Display the rows
    if rows:
        print("Form Data:")
        for row in rows:
            print(
                f"User ID: {row[0]}, Form Name: {row[1]}, Field Name: {row[2]}, Field Value: {row[3]}"
            )
    else:
        print("No data found.")


# Close the connection at the end
def close_connection():
    conn.close()


# Example usage to view database
if __name__ == "__main__":
    view_database()  # View the current data
    close_connection()  # Ensure the database connection is closed after use
