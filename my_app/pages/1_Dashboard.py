import streamlit as st
import sys
import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(ROOT_DIR)

#Import database connection function
from app.data.db import connect_database

#Import incident management functions
from app.data.incidents import (
    get_all_incidents,
    insert_incident,
    update_incident,
    delete_incident)

#Webpage title and icon
st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

#Ensure session state variables are initialised
if "logged_in" not in st.session_state:
    #Initialise login status
    st.session_state.logged_in = False

if "username" not in st.session_state:
    #Initialise username
    st.session_state.username = ""

# Check if user is logged in
if not st.session_state.logged_in:
    st.error("You must be logged in to view the dashboard.")

    #Button to go back to login/register page
    if st.button("Go to Login/Register page"):
        #Use the official navigation API to switch pages
        st.switch_page("Home.py")
        st.stop()

    #Stop further execution of the script
    st.stop()

# Dashboard content for logged-in users
st.title("Dashboard")

#Sidebar for domain selection
with st.sidebar:
    #Domain selection dropdown
    domain = st.selectbox("Choose a Domain", ["-- Select a Domain --", "Cyber Security", "Data Science", "IT Operations"], key="select_domain")

    #Line separator
    st.divider()

    if st.button("Log out"):
        # Clear session state variables related to login
        st.session_state.logged_in = False
        st.session_state.username = ""

        #Inform user of successful logout
        st.info("Logged out successfully.")

        # Redirect immediately to the login/register page
        st.switch_page("Home.py")

        #Stop further execution of the script
        st.stop()

#Verify if domain is selected
if domain == "-- Select a Domain --":
    #Display warning message
    st.warning("Please select a domain from the sidebar to continue.")
    #Stop whole execution of script
    st.stop()

else:
    #Verify if domain is Cyber Security
    if domain == "Cyber Security":
        st.markdown("Welcome to **Cyber Security** Dashboard!")


# #Connect to intelligence database
# conn = connect_database("DATA/intelligence.db")

# #Fetch all incidents from database
# incidents = get_all_incidents()

# #Display incidents in a table
# st.dataframe(incidents, use_container_width=True)

# conn.commit()
