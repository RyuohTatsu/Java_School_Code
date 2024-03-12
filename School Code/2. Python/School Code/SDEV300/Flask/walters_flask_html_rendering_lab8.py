"""
This program runs a website.

Key Features:
- User Registration: Users can create new accounts by providing a username
and password that meet certain complexity requirements.
- User Login: Registered users can log in to their accounts using their credentials.
- User Logout: Users can log out of their accounts securely.
- Access Control: Certain pages, such as the title page, body, and references,
are protected and can only be accessed by logged-in users.
- Flash Messages: Informative messages are displayed to users based on their actions,
such as successful login, registration, or errors encountered.

Dependencies:
- Flask: A micro web framework written in Python.
- Passlib: A password hashing library for Python, used for securely storing user passwords.

Usage Instructions:
1. Run the program using Python.
2. Access the website using a web browser.
3. Register a new account or log in with existing credentials.
4. Navigate through the different pages, including the protected ones.
5. Log out securely when done using the website.

Developer: Brian Walters SDEV300/6380
Developed: February 28, 2024
"""
import os
import logging
from datetime import datetime
from passlib.hash import sha256_crypt
from flask_login import login_required, LoginManager, UserMixin, login_user, logout_user
from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

CHAR_SETS = {
    'UPPER_ALPHA': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'LOWER_ALPHA': 'abcdefghijklmnopqrstuvwxyz',
    'DIGITS': '0123456789',
    'SPECIAL': r'^!\$%&/()=?{[]}+~#-_.:,;<>|\\'
}

common_passwords = set()

class User(UserMixin):
    """
    Represents a user object.

    Attributes:
        id (str): The unique identifier for the user.
    """
    def __init__(self, user_id):
        """
        Initializes a User object.

        Args:
            user_id (str): The unique identifier for the user.
        """
        self.id = user_id

@login_manager.user_loader
def load_user(user_id):
    """
    Load a user object from the database or any other storage mechanism.

    This function is required by Flask-Login to load a user object based on its
    user ID. It should return the user object corresponding to the provided user ID.

    Args:
        user_id (str): The unique identifier for the user.

    Returns:
        User: The user object corresponding to the provided user ID.
    """
    # Load the user from the database or any other storage mechanism
    return User(user_id)

def get_current_date():
    """Get the current date."""
    return datetime.now().strftime('%d %b %Y')

def get_current_time():
    """Get the current time."""
    return datetime.now().strftime('%H:%M')

@app.context_processor
def inject_current_date():
    """Inject the current date into all templates."""
    return {"current_date": get_current_date()}

@app.context_processor
def inject_current_time():
    """Inject the current time into all templates."""
    return {"current_time": get_current_time()}

def get_existing_usernames():
    """
    Retrieve existing usernames from the user credentials file.

    Returns:
        list: A list of existing usernames.
    """
    existing_usernames = []
    try:
        filepath = os.path.join(os.getcwd(), 'Flask', 'user_credentials.txt')
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                if ',' in line:  # Add a check for comma in the line
                    username, _ = line.strip().split(',', 1)
                    existing_usernames.append(username)
                else:
                    # Log or handle the case where the line format is unexpected
                    print(f"Error: Unexpected line format in user_credentials.txt: {line}")
    except FileNotFoundError:
        print("Error: File 'user_credentials.txt' not found.")
    return existing_usernames

@app.context_processor
def inject_username():
    """Inject the current user into all templates."""
    # Retrieve the username from the session (this might vary depending on your implementation)
    username = session.get('username')
    # Return a dictionary with the username variable
    return {'username': username}

def load_common_passwords():
    """Load common passwords from file into a set."""
    try:
        filepath = os.path.join(os.getcwd(), 'Flask', 'CommonPassword.txt')
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                common_passwords.add(line.strip())
    except FileNotFoundError:
        print("Error: File 'CommonPassword.txt' not found.")

# Load common passwords on application startup
load_common_passwords()

def is_common_password(password):
    """Checks if the provided password is common."""
    return password in common_passwords

def check_password_complexity(password):
    """
    Checks if the provided password meets minimum complexity requirements.

    This function checks if the password contains characters from each of the
    defined character sets (upper-case letters, lower-case letters, digits, and
    special characters).

    Args:
        password (str): The password to check.

    Returns:
        bool: True if the password meets complexity requirements, False otherwise.
    """
    return all(any(char in password for char in value) for key, value in CHAR_SETS.items())

def read_user_credentials():
    """
    Reads user credentials from the 'user_credentials.txt' file.

    This function reads the user credentials file located in the 'Flask' directory
    and returns a dictionary with usernames as keys and their hashed passwords as
    values.

    Returns:
        dict: A dictionary containing username-hashed password pairs.
    """
    users = {}
    try:
        filepath = os.path.join(os.getcwd(), 'Flask', 'user_credentials.txt')
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                username, stored_hashed_password = line.strip().split(',', 1)
                users[username] = stored_hashed_password
    except FileNotFoundError:
        print("Error: File 'user_credentials.txt' not found.")
    return users

def write_user_credentials(username, hashed_password):
    """Write new user credentials to the text file."""
    try:
        filepath = os.path.join(os.getcwd(), 'Flask', 'user_credentials.txt')
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"{username},{hashed_password}")
    except FileNotFoundError:
        print("Error: File 'user_credentials.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while writing user credentials.")

def update_user_credentials(username, hashed_password):
    """
    Update the hashed password for a given username in the user credentials file.

    Args:
        username (str): The username for which the password needs to be updated.
        hashed_password (str): The new hashed password.
    """
    try:
        filepath = os.path.join(os.getcwd(), 'Flask', 'user_credentials.txt')
        # Open the file in read mode
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Open the file again in write mode
        with open(filepath, 'w', encoding='utf-8') as file:
            # Iterate through each line in the file
            for line in lines:
                # Check if the current line contains the target username
                if line.startswith(username + ','):
                    # If the username matches, update the password
                    file.write(f"{username},{hashed_password}\n")
                else:
                    # If not, write the line as it is
                    file.write(line)
    except FileNotFoundError:
        print("Error: File 'user_credentials.txt' not found.")
    except PermissionError:
        print("Error: Permission denied while updating user credentials.")

def log_failed_login_attempt(username, ip_address):
    """
    Logs failed login attempts.

    Args:
        username (str): The username attempted to log in.
        ip_address (str): The IP address from which the login attempt originated.
    """
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    try:
        filepath = os.path.join(os.getcwd(), 'Flask', 'logger.txt')
        with open(filepath, 'a', encoding='utf-8') as file:
            file.write(f"{username},{ip_address}\n")
        logging.basicConfig(filename=filepath, level=logging.INFO, format=log_format)
        logging.info("Failed login attempt for username: %s, from IP: %s", username, ip_address)
    except PermissionError:
        # Log the error if logging fails
        logging.error("Error: Permission denied while writing login attempt.")

def hash_password(password):
    """Hashes the password using SHA-256."""
    return sha256_crypt.hash(password)

@app.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration requests.

    This route handles GET and POST requests for the registration page.
    - On GET, it renders the 'register.html' template.
    - On POST, it validates the username, password, and password confirmation,
      and if valid, stores the new user credentials and redirects to the login page.
      Otherwise, displays error messages.
    """
    if request.method == 'POST':
        # Extract username, password, and confirm password from the form data
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Remove leading and trailing whitespace
        username = username.strip()
        password = password.strip()
        confirm_password = confirm_password.strip()

        # Validate username
        if not username:
            flash('Please enter a username.', 'error')
        elif len(username) < 3:
            flash('Username must be at least 3 characters long.', 'error')
        elif username in get_existing_usernames():
            flash('Username already exists. Please choose a different one.', 'error')
        else:
            # Validate password
            if not password:
                flash('Please enter a password.', 'error')
            elif len(password) < 8:
                flash('Password must be at least 8 characters long.', 'error')
            elif not check_password_complexity(password):
                flash("Invalid password format. Please make sure your password contains at least\
                    one uppercase letter, one lowercase letter, one digit, and one special\
                    character.", 'error')
            elif password != confirm_password:
                flash('New password and confirm password do not match. Please try again.', 'error')
            elif is_common_password(password):
                flash("This password is too common. Please choose a different one.", 'error')
            else:
                try:
                    # If validation passes, register the user
                    hashed_password = hash_password(password)
                    write_user_credentials(username, hashed_password)
                    flash('Registration successful! Please log in.', 'success')
                    return redirect(url_for('login'))
                except ValueError as ve:
                    flash(f"Password complexity error: {str(ve)}", 'error')
        # Render the template after handling errors
        return render_template('register.html')

    # Render the template for GET requests
    return render_template('register.html')

@app.route('/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    """
    Handles user password change requests.

    This route handles GET and POST requests for the change password page.
    - On GET, it renders the 'change_password.html' template.
    - On POST, it validates the current password, new password, and password confirmation,
      and if valid, updates the user's password, logs the user out, and redirects to the login page.
      Otherwise, displays error messages.
    """
    if request.method == 'POST':
        # Extract current password, new password, and confirm password from the form data
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        # Retrieve the current username from the session
        username = session.get('username')

        # Remove leading and trailing whitespace
        current_password = current_password.strip()
        new_password = new_password.strip()
        confirm_password = confirm_password.strip()

        # Validate current password
        if not sha256_crypt.verify(current_password, session['hashed_password']):
            flash('Invalid current password. Please try again.', 'error')
            return render_template('change_password.html')

        # Validate new password
        if not new_password:
            flash('Please enter a new password.', 'error')
        elif len(new_password) < 8:
            flash('New password must be at least 8 characters long.', 'error')
        if not check_password_complexity(new_password):
            flash("Invalid password format. Please make sure your new password contains\
                at least one uppercase letter, one lowercase letter, one digit, and one special\
                character.", 'error')
        elif new_password != confirm_password:
            flash('New password and confirm password do not match. Please try again.', 'error')
        elif is_common_password(new_password):
            flash("This password is too common. Please choose a different one.", 'error')
        else:
            # Wrap password change logic in a try-except block to handle potential errors
            try:
                # If validation passes, update the user's password
                if check_password_complexity(new_password):
                    hashed_password = hash_password(new_password)
                    update_user_credentials(username, hashed_password)
                    flash('Password updated successfully!', 'success')
                    # Log out the user
                    session.pop('username', None)
                    return redirect(url_for('login'))
            except ValueError as ve:
                flash(f"Password complexity error: {str(ve)}", 'error')
    return render_template('change_password.html')

@app.route('/', methods=['GET', 'POST'])
def login():
    """
    Handles user login requests.

    This route handles GET and POST requests for the login page.
    - On GET, it renders the 'login.html' template.
    - On POST, it validates the username and password, and if valid,
    redirects the user to the title page. Otherwise, displays error messages.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Remove leading and trailing whitespace
        password = password.strip()
        users = read_user_credentials()
        if username in users:
            stored_hashed_password = users[username]
            if sha256_crypt.verify(password, stored_hashed_password):
                user = User(username)
                session['username'] = username
                session['hashed_password'] = stored_hashed_password
                login_user(user)
                # Check if the "Change Password after Login" checkbox is checked
                if 'change_password' in request.form:
                    return redirect(url_for('change_password'))
                return redirect(url_for('title_page'))
            else:
                # Log failed login attempt
                log_failed_login_attempt(username, request.remote_addr)
                flash('Invalid password. Please try again.', 'error')
        else:
            flash('User is not registered. Please register first.', 'error')
            # Log failed login attempt
            log_failed_login_attempt(username, request.remote_addr)
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Handle user logout."""
    logout_user()
    flash('You have been successfully logged out.', 'success')
    return redirect(url_for('login'))

@app.route('/title_page')
@login_required
def title_page():
    """Opens Title Page."""
    return render_template('title_page.html')

@app.route('/body')
@login_required
def body():
    """Render the Body page."""
    return render_template('body.html')

@app.route('/references')
@login_required
def references():
    """Render the References page."""
    return render_template('references.html')

if __name__ == '__main__':
    app.run(debug=True)
