import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://admin-dev:<db_password>@employeedesk-cluster.gbjyes6.mongodb.net/db_employeedesk?appName=employeedesk-cluster"

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Connected successfully!")

    db = client["db_employeedesk"]

    db.employees.insert_one({
        "employee_id": "EMP001",
        "name": "First Employee",
        "department": "IT"
    })

    print("Database and collection created!")

except Exception as e:
    print(e)
