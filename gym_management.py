import mysql.connector
import streamlit as st
from datetime import datetime

# Function to connect to the MySQL database
def get_connection():
    return mysql.connector.connect(
        host="your_host",       # Replace with your MySQL host
        user="your_username",            # Replace with your MySQL username
        password="Your_password",# Replace with your MySQL password
        database="gym_management"#Use your Database name
    )

# Function to view all members
def view_members():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    cursor.close()
    conn.close()

    if members:
        for member in members:
            st.write(f"**ID**: {member[0]} | **Name**: {member[1]} | **Contact**: {member[2]} | **Email**: {member[3]}")
    else:
        st.write("No members found.")

# Function to add a new member
def add_member_to_db(name, contact, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (name, contact, email) VALUES (%s, %s, %s)", (name, contact, email))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("Member added successfully!")

# Function to delete a member
def delete_member(member_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE member_id = %s", (member_id,))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("Member deleted successfully!")

# Function to display all attendance records
def see_attendance():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    attendance = cursor.fetchall()
    cursor.close()
    conn.close()

    if attendance:
        for record in attendance:
            st.write(f"**Member ID**: {record[0]} | **Trainer ID**: {record[1]} | **Date**: {record[2]}")
    else:
        st.write("No attendance records found.")

# Function to record attendance
def record_attendance(member_id, trainer_id, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO attendance (member_id, trainer_id, date) VALUES (%s, %s, %s)", (member_id, trainer_id, date))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("Attendance recorded successfully!")

# Function to add a trainer
# Function to add a trainer
def add_trainer_to_db(name, specialization, contact, email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trainers (name, specialization, contact, email) VALUES (%s, %s, %s, %s)", (name, specialization, contact, email))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("Trainer added successfully!")


# Function to display all trainers
def see_trainers():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trainers")
    trainers = cursor.fetchall()
    cursor.close()
    conn.close()

    if trainers:
        for trainer in trainers:
            st.write(f"**Trainer ID**: {trainer[0]} | **Name**: {trainer[1]} | **Specialization**: {trainer[2]} | **Contact**: {trainer[3]}")
    else:
        st.write("No trainers found.")

# Function to delete a trainer
def delete_trainer(trainer_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trainers WHERE trainer_id = %s", (trainer_id,))
    conn.commit()
    cursor.close()
    conn.close()
    st.success("Trainer deleted successfully!")

# Streamlit app main function
# Streamlit app main function
def main():
    st.set_page_config(page_title="Gym Management System", page_icon="🏋️‍♀️", layout="wide")

    # App Title and Description
    st.title("Gym Management System")
    st.write("""
    Welcome to the Gym Management System! Manage your gym members, trainers, and attendance with ease. 
    Choose an option from the sidebar to get started.
    """)

    # Sidebar for navigation
    menu = ["View Members", "Add Member", "Delete Member", "View Attendance", "Record Attendance", "View Trainers", "Add Trainer", "Delete Trainer"]
    choice = st.sidebar.selectbox("Select an Option", menu)

    # View Members
    if choice == "View Members":
        st.subheader("Members List")
        view_members()

    # Add Member
    elif choice == "Add Member":
        st.subheader("Add New Member")
        name = st.text_input("Member Name")
        contact = st.text_input("Contact Number")
        email = st.text_input("Email Address")
        if st.button("Add Member"):
            if name and contact and email:
                add_member_to_db(name, contact, email)
            else:
                st.warning("Please fill in all fields.")

    # Delete Member
    elif choice == "Delete Member":
        st.subheader("Delete Member")
        member_id = st.number_input("Enter Member ID", min_value=1)
        if st.button("Delete Member"):
            delete_member(member_id)

    # View Attendance
    elif choice == "View Attendance":
        st.subheader("Attendance Records")
        see_attendance()

    # Record Attendance
    elif choice == "Record Attendance":
        st.subheader("Record Attendance")
        member_id = st.number_input("Enter Member ID", min_value=1)
        trainer_id = st.number_input("Enter Trainer ID", min_value=1)
        date = st.date_input("Select Date", min_value=datetime.today())
        if st.button("Record Attendance"):
            record_attendance(member_id, trainer_id, date)

    # View Trainers
    elif choice == "View Trainers":
        st.subheader("Trainers List")
        see_trainers()

    # Add Trainer
    # Add Trainer
    elif choice == "Add Trainer":
        st.subheader("Add New Trainer")
        name = st.text_input("Trainer Name")
        specialization = st.text_input("Trainer's Specialization")
        contact = st.text_input("Contact Number")
        email = st.text_input("Email Address")
        if st.button("Add Trainer"):
            if name and specialization and contact and email:
                add_trainer_to_db(name, specialization, contact, email)
            else:
                st.warning("Please fill in all fields.")


    # Delete Trainer
    elif choice == "Delete Trainer":
        st.subheader("Delete Trainer")
        trainer_id = st.number_input("Enter Trainer ID", min_value=1)
        if st.button("Delete Trainer"):
            delete_trainer(trainer_id)

if __name__ == '__main__':
    main()
