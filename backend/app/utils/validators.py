import re


def is_valid_tc(tc):
    return tc.isdigit() and len(tc) == 11


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


def is_valid_password(password):
    return len(password) >= 6