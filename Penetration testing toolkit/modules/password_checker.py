import re


def check_password_strength(password):

    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append('Password should be at least 8 characters')

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        remarks.append('Add uppercase letters')

    if re.search(r'[a-z]', password):
        score += 1
    else:
        remarks.append('Add lowercase letters')

    if re.search(r'[0-9]', password):
        score += 1
    else:
        remarks.append('Add numbers')

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        remarks.append('Add special characters')

    if score <= 2:
        strength = 'Weak'
    elif score <= 4:
        strength = 'Medium'
    else:
        strength = 'Strong'

    return {
        'strength': strength,
        'score': score,
        'remarks': remarks
    }