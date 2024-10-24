import streamlit as st
import requests

# Title of the web app
st.title("User Information Form")

# Input fields for the user to enter their details
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=120)
location = st.text_input("Enter your location:")
occupation = st.text_input("Enter your occupation:")

# When the user clicks "Submit", fetch data from FastAPI
if st.button("Submit"):
    # Make a GET request to FastAPI
    response = requests.get(
        "http://127.0.0.1:8000/user-info", 
        params={"name": name, "age": age, "location": location, "occupation": occupation}
    )
    
    # Display the data returned from the FastAPI
    if response.status_code == 200:
        data = response.json()
        st.write(f"Name: {data['name']}")
        st.write(f"Age: {data['age']}")
        st.write(f"Location: {data['location']}")
        st.write(f"Occupation: {data['occupation']}")
    else:
        st.write("Error fetching data from API")
