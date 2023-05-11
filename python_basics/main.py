def addNums(a, b):
    return a + b

def substracNums(a, b):
    return a - b

# q: write simple unit test for both functions using assert statement
# a:
def test_addNums():
    assert addNums(2, 3) == 5

def test_substractNums():
    assert substracNums(3, 2) == 1

print("My small python assert tests passed")

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

import random

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

def generate_password():
    upercase_letter1, upercase_letter2=chr(random.randint(65,90)), chr(random.randint(65,90))
    lowercase_letter1, lowercase_letter2=chr(random.randint(97,122)), chr(random.randint(97,122))
    digit1, digit2=chr(random.randint(48,57)), chr(random.randint(48,57))
    punctuation_sign1, punctuation_sign2=chr(random.randint(33,47)), chr(random.randint(33,47))
    password = upercase_letter1 + upercase_letter2 + lowercase_letter1 + lowercase_letter2 + digit1 + digit2 + punctuation_sign1 + punctuation_sign2
    encoded_password = shuffle(password)
    return encoded_password

print("Randomly generated password: " + generate_password())