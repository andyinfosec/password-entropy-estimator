import string, math

def handle_input():
    user_input = input(f"Enter a password or type 'q' to quit: ")
    if user_input == 'q':
        quit()
    if not user_input.strip():
        print("Password cannot be empty")
        return
    while True:
        password = user_input
        calculate_entropy(password)
        break

def calculate_entropy(password):
    upper_case = any(c.isupper() for c in password) # Checking the password for character types
    lower_case = any(c.islower() for c in password)
    special = any(c in string.punctuation for c in password)
    digits = any(c.isdigit() for c in password)
    space = False
    if any(c == " " for c in password):
        space = True
    
    characters = [upper_case, lower_case, special, digits, space] # If type is found, value is true. This can be used to calculate R

    R = 0 # R is character pool

    if characters[0] == True: # adds number of characters in set to R if present in password. Maximum is 95
        R += 26
    if characters[1] == True:
        R += 26
    if characters[2] == True:
        R += 32
    if characters[3] == True:
        R += 10
    if characters[4] == True:
        R += 1

    L = len(password)

    E = L * math.log2(R) # Formula to calculate entropy in bits

    entropy = (round(E,2))
    print(f"{entropy} bits of entropy")

    feedback(entropy)
    return entropy
    
def feedback(entropy):
    if entropy <= 50:
        print("Weak")
    elif 50 <  entropy <= 60:
        print("Moderate")
    elif 60 < entropy <= 80 :
        print("Good")
    elif entropy > 80:
        print("Very good")
    
def run():
    while True:
        handle_input()
run()
