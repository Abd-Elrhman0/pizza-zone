# 1. inporting extensions
import streamlit as st

# 2. creating pages
home_page = st.Page(
    page = "pages/home.py",
    title = "Home page",
    icon = "🏠",
    default = True
)

chatbot_page = st.Page(
    page = "pages/chatbot.py",
    title = "talk with AI",
    icon = "✨"
)

menu_page = st.Page(
    page = "pages/menu.py",
    title = "Menu",
    icon = "📋"
)

signin_page = st.Page(
    page = "pages/signin.py",
    title = "Sign in",
    icon = "🔑"
)

signup_page = st.Page(
    page = "pages/signup.py",
    title = "Sign up",
    icon = "📝"
)

# 3. cteating navbar
navbar = st.navigation(
    pages = [
        home_page,
        signup_page,
        signin_page,
        menu_page,
        chatbot_page,
    ],
    position = 'top'
)
navbar.run()