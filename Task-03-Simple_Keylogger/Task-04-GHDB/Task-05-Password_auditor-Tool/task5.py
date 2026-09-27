import re

print("==== Password Auditor Tool ===")
password = input("Enter the password: ")
score = 0
if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
    if re.search(r"[0-9]", password):
        score += 1
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            score += 1
            common_patterns = ["123", "password", "admin", "qwerty"]
            weak_pattern = False
            for pattern in common_patterns:
                if pattern in password.lower():
                    weak_pattern = True
                    print("\nSecurity Report:")
                    if weak_pattern:
                        print("Weak Pattern Detected")
                        if score == 5 and not weak_pattern:
                            print("Security Score: Excellent")
                        elif score >= 3:
                            print("Security Score: Medium")
                        else:
                            print("Security Score: Weak")