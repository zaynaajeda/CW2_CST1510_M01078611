import streamlit as st

#Webpage title and icon
st.set_page_config(page_title="Login/Register", page_icon="🔐", layout="centered")

#Initialising session state variables
#Initialise users dictionary
if "users" not in st.session_state:
    st.session_state.users = {}

#Initialise login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

#Initialise username
if "username" not in st.session_state:
    st.session_state.username = ""

st.title("Welcome")

# If already logged in, go straight to dashboard
if st.session_state.logged_in:
    #Inform user they are already logged in
    st.success(f"Already logged in as **{st.session_state.username}**.")
    #Button to go to dashboard
    if st.button("Go to dashboard"):
        # Use the official navigation API to switch pages
        st.switch_page("pages/1_Dashboard.py")
    #Stop further execution of the script
    st.stop()

# Tabs for Login and Register
tab_login, tab_register = st.tabs(["Login", "Register"])

#Login Tab
with tab_login:
    #Subheading
    st.subheader("Login to your account")

    #Prompt for username and password
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    #Login button
    if st.button("Login"):
        #Get users dictionary from session state
        users = st.session_state.users
        #Check if username exists
        if login_username in users:
            #Check if password matches
            if users[login_username] == login_password:
                #Set session state 
                st.session_state.logged_in = True
                st.session_state.username = login_username

                #Success message for login
                st.success(f"Logged in as **{login_username}**.")

                if st.button("Go to dashboard"):
                    st.switch_page("pages/1_Dashboard.py")

            else:
                st.error("Incorrect password.")
        else:
            st.error("Invalid username.")

#Register Tab
with tab_register:
    #Subheading
    st.subheader("Create a new account")

    #Prompt for new username and password
    new_username = st.text_input("Choose a username", key="register_username")
    new_password = st.text_input("Choose a password", type="password", key="register_password")
    confirm_password = st.text_input("Confirm password", type="password", key="register_confirm")

    #Create account button
    if st.button("Create account"):
        #Input validation
        if not new_username or not new_password:
            #Incomplete fields
            st.warning("Please fill in all fields.")

        #Password confirmation
        elif new_password != confirm_password:
            #Password mismatch
            st.error("Passwords do not match. Please try again.")

        #Verify if username already exists
        elif new_username in st.session_state.users:
            #Username taken
            st.error("Username already exists. Choose a different one.")
        
        else:
            #Add new user to users dictionary
            st.session_state.users[new_username] = new_password
            st.success("Account created!")
            st.info("Go to Login tab to sign in.")