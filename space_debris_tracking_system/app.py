import streamlit as st
import pymongo
from bson.json_util import dumps
import json

# MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['spacedebris']
collection = db['debris']

def load_debris_data():
    return list(collection.find({}))

def display_debris(debris_data):
    st.title("Space Debris Tracking System")
    
    if debris_data:
        st.write("### Current Space Debris:")
        for debris in debris_data:
            st.write(f"**Name:** {debris['name']}")
            st.write(f"**Size:** {debris['size']} m")
            st.write(f"**Mass:** {debris['mass']} kg")
            st.write(f"**Current Orbit:** {debris['currentOrbit']}")
            st.write(f"**Last Updated:** {debris['lastUpdated']}")
            st.write("---")
    else:
        st.write("No debris data available.")

def main():
    debris_data = load_debris_data()
    display_debris(debris_data)

if __name__ == "__main__":
    main()
