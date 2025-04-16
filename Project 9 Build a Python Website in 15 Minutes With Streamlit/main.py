import streamlit as st

# Set up the sidebar with navigation options
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "About", "Contact Us"))

# Display content based on the selected page
if page == "Home":
    st.title("Welcome to My Simple Website")
    st.write("""
        This is a simple website created using Streamlit. 
        Navigate through the sections using the sidebar.
    """)

elif page == "About":
    st.title("About Us")
    st.write("""
        We are a team of passionate developers building cool web apps with Streamlit. 
        This website serves as a demonstration of basic navigation and web design using Streamlit.
    """)

elif page == "Contact Us":
    st.title("Contact Us")
    st.write("""
        Feel free to get in touch with us. You can reach out via the following methods:
        
        - Email: example@example.com
        - Phone: +1 (123) 456-7890
    """)

