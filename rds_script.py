import mysql.connector

# Connect to RDS
conn = mysql.connector.connect(
    host="studentdb.ctuwqgkgatmu.us-east-1.rds.amazonaws.com",  # Replace with your RDS endpoint
    user="admin",              # Your RDS username
    password="Tejaswini123",  # Your RDS password
    database="University"      # The database you created
)

cursor = conn.cursor()

# Insert Data
cursor.execute("INSERT INTO Students VALUES (2, 'Jane Smith', 22, 'Mathematics')")
conn.commit()  # Save changes

# Fetch Data
cursor.execute("SELECT * FROM Students")
for row in cursor.fetchall():
    print(row)  # Display all rows

# Close connection
cursor.close()
conn.close()
