"""
CodTech Cybersecurity Internship
Project 3: Password Strength Checker
Description: A tool to analyze password complexity and provide security feedback.
Author: [Your Name]
"""

import re

def analyze_password_strength(password):
    """
    Analyzes the strength of a given password based on length, 
    casing, numbers, and special characters.
    Returns a dictionary containing the score, strength rating, and feedback.
    """
    # Initialize scoring and feedback tracking
    score = 0
    feedback = []
    
    # 1. Length Check
    password_length = len(password)
    if password_length >= 12:
        score += 2
    elif password_length >= 8:
        score += 1
        feedback.append("👉 Increase password length to 12 or more characters for better security.")
    else:
        feedback.append("❌ Critical: Password is too short! It must be at least 8 characters.")

    # 2. Uppercase Character Check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("👉 Add at least one uppercase letter (A-Z).")

    # 3. Lowercase Character Check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("👉 Add at least one lowercase letter (a-z).")

    # 4. Number Check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("👉 Include at least one numerical digit (0-9).")

    # 5. Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_+-]", password):
        score += 1
    else:
        feedback.append("👉 Include at least one special character (e.g., !, @, #, $, %, etc.).")

    # Determine overall strength category based on score (Max score possible = 6)
    if score >= 5:
        strength = "VERY STRONG 💪"
    elif score == 4:
        strength = "STRONG 👍"
    elif score == 3:
        strength = "MEDIUM ⚠️"
    else:
        strength = "WEAK ❌"

    return {
        "score": score,
        "strength": strength,
        "feedback": feedback
    }

def main():
    """
    Interactive command-line interface for the Password Strength Checker.
    """
    print("=" * 50)
    print("      CODTECH CYBERSECURITY: PASSWORD CHECKER      ")
    print("=" * 50)
    
    while True:
        # User input prompt
        user_password = input("\nEnter a password to test (or type 'exit' to quit): ").strip()
        
        if user_password.lower() == 'exit':
            print("\nExiting program. Stay secure!")
            print("=" * 50)
            break
            
        if not user_password:
            print("⚠️ Input cannot be empty. Please enter a valid password.")
            continue
            
        # Run analysis
        results = analyze_password_strength(user_password)
        
        # Display Results Dashboard
        print("\n" + "-" * 40)
        print(f" PASSWORD ANALYSIS RESULTS")
        print("-" * 40)
        print(f"🔹 Strength Rating : {results['strength']}")
        print(f"🔹 Metric Score   : {results['score']} / 6")
        print("-" * 40)
        
        # Display feedback if any criteria are missed
        if results['feedback']:
            print("💡 Suggestions to improve your password:")
            for tip in results['feedback']:
                print(f" {tip}")
        else:
            print("🎉 Excellent! Your password satisfies all standard safety parameters.")
        print("-" * 40)

if __name__ == "__main__":
    main()