# 1. importing extensions
import streamlit as st

# 2. creating home title
st.title("Welcome to :red[PizzaZone] :pizza: !", text_alignment = "center")

# 3. creating subheading
st.subheader("Your one-stop destination for delicious pizzas! :pizza:", text_alignment = "center")

# 4. adding hero image
st.image("images/hero.jpg")
st.divider()

column1, column2 = st.columns(2, border = True)

with column1:
    st.header("🍕 Hungry?")
    st.subheader("Explore our menu and satisfy your cravings!")
    if st.button("Explore Menu", use_container_width = True):
        st.switch_page("pages/menu.py")

with column2:
    st.header("✨ Need help?")
    st.subheader("if you need help, chat with our AI assistant")
    if st.button("Chat with AI✨", use_container_width = True):
        st.switch_page("pages/chatbot.py")