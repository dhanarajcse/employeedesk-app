import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.title("EmployeeDesk Portal")

# ✅ Read MongoDB URI from Streamlit Secrets
uri = st.secrets["MONGODB_URI"]

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    st.success("Connected to MongoDB successfully!")

    db = client["db_employeedesk"]

    # Insert sample employee only once
    if db.employees.count_documents({"employee_id": "EMP001"}) == 0:
        db.employees.insert_one({
            "employee_id": "EMP001",
            "name": "First Employee",
            "department": "IT"
        })
        st.success("Employee record created!")
    else:
        st.info("Employee record already exists.")

except Exception as e:
    st.error(f"Error: {e}")
