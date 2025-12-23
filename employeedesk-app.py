import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.title("EmployeeDesk")

try:
    uri = st.secrets["MONGODB_URI"]
    client = MongoClient(uri, server_api=ServerApi('1'))
    client.admin.command("ping")

    st.success("Connected to MongoDB Atlas successfully!")

except Exception as e:
    st.error(f"MongoDB connection failed: {e}")
