import os
import random
import string
import re
import math

# Folder containing the insult text files
INSULT_FOLDER = "src"

# Brute force speed estimates based on known attack rates
BRUTE_FORCE_SPEEDS = {
    "Basic GPU (100M/s)": 1e8,    # Low-end GPU rig
    "Advanced GPU (10B/s)": 1e10,  # Advanced GPU rig
    "Supercomputer (100T/s)": 1e14 # High-end supercomputers or botnets
}

def test_password_strength(password):
    """Evaluates the strength of a password and returns a score from 1-10."""
    score = 0
    char_pool = 0

    # Character Pool Size
    if any(c.islower() for c in password):
        char_pool += 26
    if any(c.isupper() for c in password):
        char_pool += 26
    if any(c.isdigit() for c in password):
        char_pool += 10
    if any(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~" for c in password):
        char_pool += 30  # Special characters

    # Length Check
    length = len(password)
    if length >= 8:
        score += 2
    if length >= 12:
        score += 3
    if length >= 16:
        score += 2

    # Character Variety
    if char_pool >= 36:
        score += 2
    if char_pool >= 62:
        score += 3
    if char_pool >= 92:
        score += 3

    # Check for common passwords
    common_passwords = ["password", "123456", "qwerty", "admin", "abc123", "letmein", "monkey", "123456789"]
    if password.lower() in common_passwords or re.match(r"^[a-zA-Z]+$", password):
        score = max(1, score - 5)

    return min(10, max(1, score)), char_pool

def estimate_crack_time(password_length, char_pool):
    """Estimates the time to crack a password using brute force at different speeds."""
    total_combinations = char_pool ** password_length
    time_estimates = {}

    for name, speed in BRUTE_FORCE_SPEEDS.items():
        seconds = total_combinations / speed
        if seconds < 60:
            time_estimates[name] = f"{seconds:.2f} seconds"
        elif seconds < 3600:
            time_estimates[name] = f"{seconds / 60:.2f} minutes"
        elif seconds < 86400:
            time_estimates[name] = f"{seconds / 3600:.2f} hours"
        elif seconds < 31557600:
            time_estimates[name] = f"{seconds / 86400:.2f} days"
        elif seconds < 3155760000:
            time_estimates[name] = f"{seconds / 31557600:.2f} years"
        else:
            time_estimates[name] = f"{seconds / 31557600000:.2f} centuries"

    return time_estimates

def get_random_insult(score):
    """Reads a random insult from the appropriate file based on score."""
    filename = os.path.join(INSULT_FOLDER, f"Level_{score}_Insults.txt")

    if not os.path.exists(filename):
        return "No insults available for this level. Consider being more creative with your passwords!"

    with open(filename, "r", encoding="utf-8") as file:
        insults = file.readlines()

    return random.choice(insults).strip() if insults else "Somehow, this insult file is empty. That's an insult in itself."

def generate_password(strength):
    """Generates a password based on the desired strength (1-10)."""
    length_map = {1: 6, 2: 8, 3: 10, 4: 12, 5: 14, 6: 16, 7: 18, 8: 20, 9: 22, 10: 24}
    length = length_map.get(strength, 12)

    chars = string.ascii_letters + string.digits
    if strength >= 5:
        chars += "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
    
    return ''.join(random.choice(chars) for _ in range(length))

def main_menu():
    while True:
        print("\n--- Password Strength Tester ---")
        print("1. Test a password")
        print("2. Generate a new password")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            user_password = input("\nEnter a password to test: ")
            score, char_pool = test_password_strength(user_password)
            crack_times = estimate_crack_time(len(user_password), char_pool)

            print(f" Password Strength Score: {score}/10")
            print(get_random_insult(score))  # Get insult from correct file

            print("\n Estimated Crack Time with Brute Force:")
            for method, time in crack_times.items():
                print(f"  {method}: {time}")

        elif choice == "2":
            desired_strength = int(input("Select a strength level (1-10): "))
            new_password = generate_password(desired_strength)
            print(f"\nHere is your new password: {new_password}")

        elif choice == "3":
            print("Exiting... Stay secure!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
