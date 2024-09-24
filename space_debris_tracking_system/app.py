# app.py
import streamlit as st
from mongo_db import load_debris_data, insert_initial_data

def main():
    st.title("Space Debris Tracking System")

    # Insert initial data if not already present
    insert_initial_data()

    # Load debris data from MongoDB
    debris_data = load_debris_data()

    if debris_data:
        st.write("Debris Data:")
        for debris in debris_data:
            st.write(debris)
    else:
        st.write("No debris data found.")

if __name__ == "__main__":
    main()
