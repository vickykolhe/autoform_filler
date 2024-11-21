import sqlite3

# Connect to the database
conn = sqlite3.connect("forms.db")
c = conn.cursor()

# Create a table for form data if it doesn't exist
c.execute(
    """CREATE TABLE IF NOT EXISTS form_data
             (form_name TEXT, field_name TEXT, field_value TEXT, aadhaar TEXT)"""
)


def save_to_db(form_name, field_name, field_value, aadhaar):
    """
    Save the form data into the database, linked to the Aadhaar key.
    If the entry already exists (same form, field, and aadhaar), update it.
    """
    # Check if the entry already exists
    c.execute(
        "SELECT * FROM form_data WHERE form_name = ? AND field_name = ? AND aadhaar = ?",
        (form_name, field_name, aadhaar),
    )
    existing_entry = c.fetchone()

    if existing_entry:
        # Update the existing entry
        c.execute(
            "UPDATE form_data SET field_value = ? WHERE form_name = ? AND field_name = ? AND aadhaar = ?",
            (field_value, form_name, field_name, aadhaar),
        )
    else:
        # Insert new entry if it doesn't exist
        c.execute(
            "INSERT INTO form_data (form_name, field_name, field_value, aadhaar) VALUES (?, ?, ?, ?)",
            (form_name, field_name, field_value, aadhaar),
        )

    # Commit the changes to the database
    conn.commit()


def fetch_form_data(aadhaar):
    """
    Retrieve all form data for a specific Aadhaar key.
    """
    c.execute(
        "SELECT form_name, field_name, field_value FROM form_data WHERE aadhaar = ?",
        (aadhaar,),
    )
    rows = c.fetchall()
    if rows:
        form_data = {}
        for row in rows:
            form_name, field_name, field_value = row
            if form_name not in form_data:
                form_data[form_name] = {}
            form_data[form_name][field_name] = field_value
        return form_data
    else:
        print(f"No data found for Aadhaar: {aadhaar}")
        return None


# Function to view the data in the database
def view_database():
    c.execute("SELECT * FROM form_data")
    rows = c.fetchall()

    # Display the rows
    if rows:
        print("Form Data:")
        for row in rows:
            print(
                f"Form Name: {row[0]}, Field Name: {row[1]}, Field Value: {row[2]}, Aadhaar: {row[3]}"
            )
    else:
        print("No data found.")


# Close the connection at the end
def close_connection():
    conn.close()


# Example usage to view database and fetch form data
if __name__ == "__main__":
    view_database()  # View the current data
    # Example of fetching form data by Aadhaar key
    aadhaar_to_fetch = "1234"  # Replace with actual Aadhaar last 4 digits
    form_data = fetch_form_data(aadhaar_to_fetch)
    if form_data:
        print(f"Form data for Aadhaar {aadhaar_to_fetch}: {form_data}")
    close_connection()  # Ensure the database connection is closed after use
