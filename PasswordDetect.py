'''
Strong Password Detection Using Regex
'''
import re

strength = 0


def user_name():
    user_name = raw_input("Enter your Name : ")
    return user_name


def ask_password():
    strength = 0
    password = raw_input("Enter Password : ")
    return password,strength


def pass_len_check(text, strength):
    p1 = re.compile(r'(\w){8}')
    r1 = p1.search(text)

    if (r1 == None):
        print("Password must contain at least 8 characters ")
    else:
        strength += 1
    return strength


def pass_case_digit_check(text,strength):
    p2 = re.compile(r'[a-z]+')
    r2 = p2.search(text)

    p3 = re.compile(r'[A-Z]+')
    r3 = p3.search(text)

    p4 = re.compile(r'[0-9]')
    r4 = p4.search(text)

    if (r2 == None):
        print "Password must contain atleast one lower case letter"
    else:
        strength += 1

    if (r3 == None):
        print "Password must contain atleast one upper case letter"
    else:
        strength += 1

    if (r4 == None):
        print "Password must contain atleast one digit"
    else:
        strength += 1

    return strength
user_name()
while strength < 4:
    y, strength = ask_password()
    strength = pass_len_check(y, strength)
    strength = pass_case_digit_check(y, strength)

print "Your Password is Strong"