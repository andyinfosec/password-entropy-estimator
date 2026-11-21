## Password Entropy Estimator
A Python-based tool that estimates the theoretical entropy of a password based on its length and character composition.

## Overview
Password Entropy Estimator calculates the theoretical entropy of a password in bits. It identifies the character sets used within the password and estimates the number of possible combinations that could be generated from those character sets.
The project was developed to explore password security, information theory and the mathematical principles behind password entropy.

## Features
- Detects lowercase letters, uppercase letters, digits and special characters.
- Identifies spaces within passwords.
- Calculates password length.
- Determines the size of the available character pool.
- Estimates theoretical password entropy in bits.
- Provides an indicative measure of password strength.

## How It Works
The estimator uses the following formula:
`E = L * log_2(R)`
Where:
- E = Estimated entropy in bits.
- L = Password length.
- R = Size of the character pool.

The character pool represents the total number of possible characters available based on the character classes detected.
For example, if a password contains lowercase letters, uppercase letters and digits, the character pool is:

`R = 26 + 26 + 10 = 62`

For a randomly generated password of 12 characters:

`E = 12 * log_2(62)`

This produces an estimated entropy of approximately 71.45 bits.

## Requirements
- Python 3.x
- Python standard library `math`

No third-party dependencies are required.

## Installation
1. Clone the repository:

`git clone https://github.com/andyinfosec/password-entropy-estimator.git`

2. Navigate into the project directory:

`cd password-entropy-estimator`

3. Run the program:

`python3 password_entropy_estimator.py`

## Limitations
This tool calculates theoretical entropy rather than measuring the actual security or guessability of a password.
The calculation assumes that:
 - Every character is selected independently.
 - Every character in the detected pool has an equal probability of being selected.
- The password is generated randomly rather than chosen by a human.
Human-created passwords often contain predictable patterns, common words, repeated characters or substitutions. These characteristics can significantly reduce the effective entropy of a password.

Consequently, the estimated entropy may overstate the actual resistance of a human-created password to guessing attacks.
This tool should be treated as an educational estimator, not a definitive password security assessment.

## Disclaimer
This project is intended for educational purposes and to demonstrate an understanding of Python programming and password entropy. It is not intended to replace dedicated password security auditing tools.
