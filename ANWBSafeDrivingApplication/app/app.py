# Backend logic
from flask import Flask, request, jsonify
from flask_cors import CORS
import hashlib
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=[logging.FileHandler("app.log", mode="w"),
              logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app)

# Hardcoded users (initial)
hardcoded_users = {
    "user": hashlib.sha256("1".encode()).hexdigest(),
    "user2@example.com": hashlib.sha256("password2".encode()).hexdigest(),
    "user3@example.com": hashlib.sha256("password3".encode()).hexdigest(),
}


def hash_password(password):
    """
    Hashes a password using SHA-256.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def validate_login_data(data):
    """
    Validates the login data.

    Args:
        data (dict): The login data.

    Returns:
        tuple: A tuple containing the username and an error message (if any).
    """
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        logger.warning("Missing username or password")
        return None, "Username and password are required"

    return username, None


def authenticate_user(username, password):
    """
    Authenticates the user.

    Args:
        username (str): The username.
        password (str): The password.

    Returns:
        tuple: A tuple containing the status and response message.
    """
    hashed_password = hash_password(password)
    if (
        username in hardcoded_users
        and hardcoded_users[username] == hashed_password
    ):
        logger.info(f"User {username} logged in successfully")
        return "success", username
    else:
        logger.error("Invalid username or password")
        return "error", "Invalid username or password"


@app.route("/log-in", methods=["POST"])
def log_in():
    """
    Handles the user login request.

    Expects a JSON payload with 'username' and 'password'.

    Returns:
        JSON response indicating success or failure.
    """
    data = request.json
    username, error = validate_login_data(data)
    if error:
        return jsonify(status="error", message=error), 400

    status, response = authenticate_user(username, data["password"])
    if status == "success":
        return jsonify(status="success", user_name=response)
    else:
        return jsonify(status="error", message=response), 401


@app.route("/sign-up", methods=["POST"])
def sign_up():
    """
    Handles the user sign-up request.

    Expects a JSON payload with 'first_name', 'last_name', 'email',
    and 'password'.

    Returns:
        JSON response indicating success or failure.
    """
    data = request.json
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    password = data.get("password")

    if not first_name or not last_name or not email or not password:
        logger.warning("Missing fields in sign-up data")
        return jsonify(status="error", message="All fields are required"), 400

    if email in hardcoded_users:
        logger.info("User already exists")
        return jsonify(status="error", message="User already exists"), 409

    hashed_password = hash_password(password)
    hardcoded_users[email] = hashed_password
    logger.info(f"User {email} registered successfully")
    return jsonify(status="success", message="User registered successfully")


if __name__ == "__main__":
    logger.info("Starting the Flask app")
    app.run(debug=True, port=3630)
