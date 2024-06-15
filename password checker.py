import re
from zxcvbn import zxcvbn  

def check_password_strength(password):
    score = 0
    messages = []

    if len(password) >= 12:
        score += 2
        messages.append("Good length (12 or more characters).")
    elif len(password) >= 8:
        score += 1
        messages.append("Moderate length (8-11 characters).")
    else:
        messages.append("Password too short (less than 8 characters).")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 2
        messages.append("Contains both upper and lower case letters.")
    elif re.search(r'[A-Z]', password) or re.search(r'[a-z]', password):
        score += 1
        messages.append("Contains either upper or lower case letters.")

    if re.search(r'\d', password):
        score += 2
        messages.append("Contains digits.")
    else:
        messages.append("No digits found.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 2
        messages.append("Contains special characters.")
    else:
        messages.append("No special characters found.")

    common_patterns = ["123", "password", "qwerty", "abc", "letmein"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score -= 2
        messages.append("Contains common patterns or dictionary words.")
    else:
        score += 1
        messages.append("No common patterns or dictionary words.")

    zxcvbn_result = zxcvbn(password)
    zxcvbn_score = zxcvbn_result['score']
    if zxcvbn_score == 4:
        score += 2
        messages.append("zxcvbn analysis: Very strong password.")
    elif zxcvbn_score == 3:
        score += 1
        messages.append("zxcvbn analysis: Strong password.")
    elif zxcvbn_score == 2:
        messages.append("zxcvbn analysis: Fair password.")
    else:
        messages.append("zxcvbn analysis: Weak password.")

    if score >= 8:
        strength = "Very Strong"
    elif score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, messages

def main():
    print("Password Strength Checker")
    print("=========================")
    password = input("Enter a password to check its strength: ")
    strength, messages = check_password_strength(password)
    print(f"\nPassword Strength: {strength}")
    print("Details:")
    for message in messages:
        print(f"- {message}")

if __name__ == "__main__":
    main()
