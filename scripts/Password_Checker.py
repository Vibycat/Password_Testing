import random
import string
import re
import math

# Brute force speed estimates based on known attack rates
# Values are in attempts per second (approximate estimates based on modern hardware)
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

import random

def insult_password(score):
    """Returns a random insult based on password strength."""
    insults = {
        1: [
            "Your password is basically a speedrun for hackers.",
            "Even a potato could crack this.",
            "I think my cat just guessed your password.",
            "This is less secure than a sticky note on your monitor.",
            "Are you trying to get hacked for sport?",
            "This password is one Google search away from being exposed.",
            "I've seen better security on a luggage lock."
        ],
        2: [
            "This is marginally better than leaving the field blank.",
            "You might as well use 'password123'.",
            "Hackers will send you a thank-you note.",
            "This is the digital equivalent of locking your front door but leaving all the windows open.",
            "Slightly less terrible, but still a hacker’s dream.",
            "Your password is one lucky guess away from disaster.",
            "Honestly, a toddler could guess this."
        ],
        3: [
            "Mildly better, but still trash.",
            "Did you think adding a number would help?",
            "This is what we call 'hacker bait'.",
            "You're at the level where an intern hacker would break in just for practice.",
            "A dictionary attack would eat this for breakfast.",
            "Your password is like a house with a 'No Burglars Allowed' sign.",
            "Might as well hand out your login info on business cards."
        ],
        4: [
            "Not bad, but still kind of meh.",
            "A decent attempt, but don’t get cocky.",
            "You're on the right path, but still in hacker snack territory.",
            "This might stop a lazy hacker, but not a determined one.",
            "Security level: toddler-proof.",
            "You added some complexity, but not enough to impress anyone.",
            "Try again, and this time, pretend you care."
        ],
        10: [
            "Hacker-proof. Well played.",
            "This password could outlive the universe.",
            "You're basically a cybersecurity god.",
            "Congratulations, even quantum computers will struggle with this.",
            "This is so secure, I’m afraid to even look at it.",
            "Your password is so strong that even you might forget it.",
            "Even the NSA would be impressed."
        ]
    }
    return random.choice(insults.get(score, ["You're doing... okay."]))


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
            print(insult_password(score))

            print(" Estimated Crack Time with Brute Force:")
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
