import sqlite3


# Establish the connection
conn = sqlite3.connect('portal_pooya.db')

# Create a cursor to interact with the database
cursor = conn.cursor()


# Create the table if it doesn't exist
create_table_query = '''
    CREATE TABLE IF NOT EXISTS student_info (
        national_code INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT ,
        email TEXT,
        mobile TEXT ,
        gender TEXT ,
        category TEXT,
        entry_year TEXT,
        uername TEXT,
        password TEXT
    )
'''
cursor.execute(create_table_query)



# Select all rows from the table
select_query = '''
    SELECT * FROM student_info
'''

cursor.execute(select_query)

# Fetch all rows
rows = cursor.fetchall()

# Print the rows
for row in rows:
    print(row)


# # Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()