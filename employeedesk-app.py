import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.title("EmployeeDesk – Step 1: Employee Creation")

# MongoDB connection
uri = st.secrets["MONGODB_URI"]
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["db_employeedesk"]

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
