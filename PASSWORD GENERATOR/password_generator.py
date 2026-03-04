import random
import string
import sys

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_special):
    """Generate a random password of specified length with selected character types."""
    character_pool = ""
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation
    
    if not character_pool:
        print("Error: Select at least one character type.")
        return None
    
    password = random.choices(character_pool, k=length)
    return ''.join(password)

def check_password_strength(password):
    """Evaluate and return the strength of the password."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    
    score = sum([has_upper, has_lower, has_digit, has_special])
    
    if length >= 12 and score == 4:
        return "Strong"
    elif length >= 8 and score >= 3:
        return "Medium"
    else:
        return "Weak"

def copy_to_clipboard(text):
    """Copy text to clipboard using platform-specific command."""
    try:
        if sys.platform == "win32":
            import subprocess
            subprocess.run(['cmd.exe', '/c', 'echo ' + text + ' | clip'], 
                         capture_output=True, check=True)
        elif sys.platform == "darwin":
            import subprocess
            subprocess.run(['pbcopy'], input=text.encode(), check=True)
        else:
            import subprocess
            subprocess.run(['xclip', '-selection', 'c'], input=text.encode(), check=True)
        return True
    except Exception:
        return False

def main():
    """Main function to run the password generator."""
    print("=" * 40)
    print("      PASSWORD GENERATOR APPLICATION")
    print("=" * 40)
    print()
    
    # Get password length
    try:
        length = int(input("Enter password length (8-128): "))
        if length < 8 or length > 128:
            print("Error: Password length must be between 8 and 128 characters.")
            return
    except ValueError:
        print("Error: Please enter a valid number.")
        return
    
    # Character type options
    print("\nSelect character types to include:")
    use_uppercase = input("  Include uppercase letters (A-Z)? (y/n): ").lower() == 'y'
    use_lowercase = input("  Include lowercase letters (a-z)? (y/n): ").lower() == 'y'
    use_digits = input("  Include digits (0-9)? (y/n): ").lower() == 'y'
    use_special = input("  Include special characters (!@#$%^&*)? (y/n): ").lower() == 'y'
    
    # Generate password
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    
    if password:
        # Display results
        print("\n" + "-" * 40)
        print(f"Generated Password: {password}")
        print(f"Password Strength:  {check_password_strength(password)}")
        print("-" * 40)
        
        # Copy to clipboard option
        copy_option = input("\nCopy password to clipboard? (y/n): ").lower()
        if copy_option == 'y':
            if copy_to_clipboard(password):
                print("Password copied to clipboard!")
            else:
                print("Could not copy to clipboard. Please select and copy manually.")
    
    print("\nThank you for using Password Generator!")

if __name__ == "__main__":
    main()

