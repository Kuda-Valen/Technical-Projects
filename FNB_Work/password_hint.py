"""
    == Secure Password Hint tool ==

    Users often forget thier passwords. Create a script that helps
    users by showing a secure hint.
    1. Ask the user to input thier secret password
    2. Use .strip() to clean up any spaces they might have typed at the start or end
    3. Grab the very first letter and the very last letter of the password using string indexing
    4. Print a hint using an f-string that forces the letters itno uppercase so they stand out
"""

def password_hint(password):
    first_letter = password[0]
    last_letter = password[-1]
    return first_letter, last_letter

password = "Kudakwashe09191 "
new_password = password.strip()

print(f"Password: {password}")
print(f"New Password: {new_password}")
print(f"Your password hint: Starts with {password_hint(new_password)[0]} and ends with {password_hint(new_password)[1]}")