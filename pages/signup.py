# 1. importing extensions
import streamlit as st

# 2. 
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = None
if "user_email" not in st.session_state:
    st.session_state.user_email = None
if "user_phone" not in st.session_state:
    st.session_state.user_phone = None
if "user_street" not in st.session_state:
    st.session_state.user_street = None
if "user_apartment" not in st.session_state:
    st.session_state.user_apartment = None 
if "user_password" not in st.session_state:
    st.session_state.user_password = None

# 2. creating title
st.title("Create Your Account 📝")

# 3. creating subheading
st.subheader("Join us and enjoy delicious pizzas! 🍕")

# 4. creating personal form
form = st.form("signup_form")
with form:
    st.header("Personal Information")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
    with col2:
        phone = st.text_input("Phone Number")
        password = st.text_input("Password", type="password")
    
    st.header("Address Information")
    col3, col4 = st.columns([3,1])
    with col3:
        street = st.text_input("Street Address")
    with col4:
        apartment = st.text_input("Apartment No.")
    
    if st.form_submit_button("Create Account", use_container_width = True):
        if not name or not email or not phone or not password or not street:
            st.error("Please fill in all required fields.")
        else:
            st.session_state.logged_in = True
            st.session_state.user_name = name
            st.session_state.user_email = email
            st.session_state.user_phone = phone
            st.session_state.user_street = street
            st.session_state.user_apartment = apartment
            st.session_state.user_password = password
            st.success("Account created successfully! 🎉")

st.divider()

st.subheader("Already have an account?")
if st.button("Sign in", use_container_width = True):
    st.switch_page("pages/signin.py")



    

    









# st.header("Personal Information")
#     name = st.text_input("Full Name")
#     email = st.text_input("Email Address")
#     password = st.text_input("Password", type="password")
#     confirm_password = st.text_input("Confirm Password", type="password")
#     submit_personal = st.form_submit_button("Next")