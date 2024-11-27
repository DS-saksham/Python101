"""
    Helper functions are small, reusable functions designed to perform specific tasks
    that assist the main functions or prorams. 
"""

def is_valid_email(email):
    """Checks if the given email is valid or not"""
    return "@" in email and "." in email

# Main function
def register_user(email):
    if not is_valid_email(email):
        return "Invalid Email"
    return "User registered successfully"

print(register_user("examp@le.com"))

# Formating Helper
def format_name(first_name, last_name)
    return f"{first_name.capitalize()}  {last_name.capitalize()}"

# Define Main Function

def greet_user(first_name, last_name):
    name = format_name(first_name, last_name)
    print(f"Hello, {name}!!!")

greet_user("john","doe")