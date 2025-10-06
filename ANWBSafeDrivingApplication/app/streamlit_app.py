import streamlit as st
import requests
import os
import sys
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[
        logging.FileHandler("streamlit_app.log", mode="w"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger(__name__)

# Add the pages directory to the system path to allow imports
sys.path.append(os.path.join(os.path.dirname(__file__), "pages"))

base_url = "http://127.0.0.1:3630"


# Mock switch_page function to avoid MyPy errors
def switch_page(page: str):
    st.session_state["current_page"] = page


st.set_page_config(initial_sidebar_state="collapsed")


def show_terms_and_conditions():
    """
    Display the terms and conditions.
    """
    st.markdown(
        """
    <style>
        .terms {
            font-size: 8px;
        }
    </style>
    <div class="terms">
        <h4>Welcome to Straat-O-Sfeer</h4>
        <p><strong>Terms and Conditions</strong></p>
        <p><strong>Effective Date: 18 June 2024</strong></p>
        <p>Welcome to Straat-O-Sfeer Limited App (straat-o-sfeer). By using
        this App, you agree to the following summarised terms and conditions:
        </p>
        <ol>
            <li><strong>Acceptance of Terms:</strong> By using the App, you agree to
            be bound by these Terms. If you do not agree, do not use the App.</li>
            <li><strong>Changes to Terms:</strong> We may modify these Terms at any
            time. Continued use of the App means you accept the new Terms.</li>
            <li><strong>Use of the App:</strong></li>
            <ul>
                <li><strong>Eligibility:</strong> You must be 18+ years old.</li>
                <li><strong>License:</strong> You have a limited, non-exclusive,
                non-transferable, revocable license for personal, non-commercial
                use.</li>
                <li><strong>Prohibited Conduct:</strong> Do not use the App for
                illegal activities, distribute content without permission, use
                automated systems to access the App, or compromise security.</li>
            </ul>
            <li><strong>Intellectual Property:</strong> All content and features of
            the App are owned by Straat-O-Sfeer Law Limited and are protected by
            intellectual property laws.</li>
            <li><strong>Privacy Policy:</strong> Your use of the App is subject to
            our Privacy Policy. By using the App, you consent to our data
            practices.</li>
            <li><strong>Use of AI:</strong> The App uses artificial intelligence to
            provide certain features and functionalities. By using the App, you
            agree to the use of AI as described in our Privacy Policy. Specifically,
            we use AI to analyse various data inputs and create model outputs for
            street risk categories. This helps to identify and categorise different
            levels of street safety risks based on collected data.</li>
            <li><strong>Disclaimer of Warranties:</strong> The App is provided "as
            is" without warranties of any kind. Use the App at your own risk.</li>
            <li><strong>Limitation of Liability:</strong> Straat-O-Sfeer Limited is
            not liable for any damages arising from your use of the App.</li>
            <li><strong>Indemnification:</strong> You agree to indemnify
            Straat-O-Sfeer Limited from any claims or damages resulting from your
            use of the App or violation of these Terms.</li>
            <li><strong>Right to Be Anonymised:</strong> You have the right to request the
            anonymisation of your personal data. This means that we will remove or
            alter any personal identifiers so that the data can no longer be
            associated with you.</li>
            <li><strong>User Data Requests:</strong> You have the right to request access
            to the personal data we hold about you. You can request the correction,
            deletion, or anonymisation of your data, and we will comply in accordance
            with our Privacy Policy and applicable laws.</li>
            <li><strong>Right to Data Deletion:</strong> You have the right to request the
            deletion of your personal data. Upon receiving such a request, we will
            delete your data from our records, except where we are required to retain
            it for legal reasons.</li>
            <li><strong>Governing Law:</strong> These Terms are governed by the laws
            of the European Union's AI Act. Any disputes will be resolved under the
            jurisdiction of the courts of the European Union.</li>
            <li><strong>Contact Information:</strong> For questions, contact us at:</li>
            <ul>
                <li>Address: Monseigneur Hopmansstraat 2, 4817 JS Breda</li>
                <li>Phone: 076 533 2203</li>
                <li>Email: agmapplication@buas.nl</li>
            </ul>
        </ol>
        <p>By using the App, you acknowledge that you have read, understood,
        and agree to these Terms and Conditions.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button("I Accept"):
            st.session_state["accepted_terms"] = True
            st.experimental_rerun()

    with col2:
        if st.button("Disagree"):
            st.warning(
                """Unable to proceed, tool can only be used after agreeing
                with the terms."""
            )
            st.stop()

st.title("Welcome to Straat-O-Sfeer")

def log_in(username, password):
    """
    Log in a user.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        dict: The response from the server.
    """
    payload = {"username": username, "password": password}
    try:
        response = requests.post(f"{base_url}/log-in", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return {"status": "error", "message": "Request failed"}


def sign_up(first_name, last_name, email, password):
    """
    Sign up a new user.

    Args:
        first_name (str): The first name.
        last_name (str): The last name.
        email (str): The email.
        password (str): The password.

    Returns:
        dict: The response from the server.
    """
    payload = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
    }
    try:
        response = requests.post(f"{base_url}/sign-up", json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
        return {"status": "error", "message": "Request failed"}


def log_out():
    """
    Log out or delete the current user.
    """
    st.session_state["logged_in"] = False


# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "accepted_terms" not in st.session_state:
    st.session_state["accepted_terms"] = False

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "main"

# Check if the user should be redirected to the Route page
if st.session_state["current_page"] == "Route":
    st.switch_page("pages/Route.py")

if not st.session_state["accepted_terms"]:
    show_terms_and_conditions()

if st.session_state["accepted_terms"] and not st.session_state["logged_in"]:
    tab1, tab2, tab3 = st.tabs(["Signup", "Log-in", "Guest"])

    with tab1:
        st.header("Create new account")
        first_name = st.text_input("First Name", key="signup_first_name")
        last_name = st.text_input("Last Name", key="signup_last_name")
        email = st.text_input("Email", key="signup_email")
        password = st.text_input("Password", key="signup_password",
                                 type="password")

        if st.button("Create account"):
            result = sign_up(first_name, last_name, email, password)
            if result["status"] == "success":
                st.success(result["message"])
                st.session_state["logged_in"] = True
                st.session_state["user_name"] = result["user_name"]
                st.session_state["current_page"] = "Route"
                st.experimental_rerun()
            else:
                st.error(result["message"])

    with tab2:
        st.header("Login to existing account")
        username = st.text_input("Username", key="login_username")
        password = st.text_input("Password", key="login_password",
                                 type="password")

        if st.button("Log In"):
            result = log_in(username, password)
            if result["status"] == "success":
                st.session_state["logged_in"] = True
                st.session_state["user_name"] = result["user_name"]
                st.success("Logged in!")
                st.session_state["current_page"] = "Route"
                st.experimental_rerun()
            else:
                st.error(result["message"])

    with tab3:
        st.header("Guest login")
        if st.button("Continue as Guest"):
            st.session_state["logged_in"] = True
            st.session_state["user_name"] = "Guest"
            st.success("Logged in as Guest!")
            st.session_state["current_page"] = "Route"
            st.experimental_rerun()

elif st.session_state["logged_in"]:
    st.write(f"Logged in as {st.session_state['user_name']}!")
    if st.button("Log Out"):
        log_out()
        st.success("Logged out successfully.")
        st.experimental_rerun()

    if st.button("Delete User"):
        st.success("User deleted successfully.")
        log_out()
        st.experimental_rerun()
