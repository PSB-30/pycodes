import streamlit as st

# Streamlit app function
def email_splitter_app():
    st.title("Email Splitter")

    # Manage state of the email input field using session_state
    if 'email' not in st.session_state:
        st.session_state.email = ""  # Initialize email field if not set

    # User input for email
    email = st.text_input("Enter your email address:", value=st.session_state.email)

    # Button to trigger the split action
    if st.button("Split Email"):
        if email:
            check_1 = email.count("@")
            if check_1 != 1:
                st.error("Not a valid email address")
            else:
                # Split the email into username and domain
                email_splitter = email.split("@")
                username = email_splitter[0]
                domain = email_splitter[1]
                # Display the result
                st.success(f'Hello, your username is "{username}" and domain is "{domain}".')
        else:
            st.warning("Please enter an email address.")

    # Button to clear the email input field
    if st.button("Clear"):
        st.session_state.email = ""  # Clear the email field
        st.experimental_rerun()  # Re-run the app to refresh the input

# Run the app
if __name__ == "__main__":
    email_splitter_app()
