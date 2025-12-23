import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime

st.title("Employee Attendance 🚀")

# MongoDB connection
uri = st.secrets["MONGODB_URI"]
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["db_employeedesk"]

# -------------------- Step 1: Add New Employee --------------------
st.subheader("Add New Employee")

employee_id = st.text_input("Employee ID")
name = st.text_input("Employee Name")
department = st.text_input("Department")

if st.button("Save Employee"):
    if employee_id and name and department:
        if db.employees.count_documents({"employee_id": employee_id}) == 0:
            db.employees.insert_one({
                "employee_id": employee_id,
                "name": name,
                "department": department
            })
            st.success("Employee saved successfully!")
        else:
            st.warning("Employee ID already exists.")
    else:
        st.error("Please fill all fields.")

# -------------------- Step 3: Attendance --------------------
st.subheader("Record Attendance")

# Fetch employee list
employee_list = list(db.employees.find({}, {"_id": 0, "employee_id": 1, "name": 1}))

# Create dropdown for employees
employee_options = [f"{emp['employee_id']} - {emp['name']}" for emp in employee_list]
selected_employee = st.selectbox("Select Employee", ["--Select--"] + employee_options)

attendance_status = st.selectbox("Attendance Status", ["Present", "Absent", "Leave"])

if st.button("Save Attendance"):
    if selected_employee != "--Select--":
        emp_id = selected_employee.split(" - ")[0]  # Extract employee_id
        db.attendance.insert_one({
            "employee_id": emp_id,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "status": attendance_status
        })
        st.success(f"Attendance for {selected_employee} saved successfully!")
    else:
        st.error("Please select an employee.")
