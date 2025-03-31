import streamlit as st
from pymongo import MongoClient

def get_database():
    mongo_uri = st.secrets["connections"]["MONGODB_URI"]
    client = MongoClient(mongo_uri)
    return client["lost_found_db"]
