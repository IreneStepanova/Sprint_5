import random

COHORT = 49


def generate_email():
    digits = random.randint(100, 999)
    email = f"test_testov_{COHORT}_{digits}@yandex.ru"
    print(f"  Email: {email}")
    return email


def generate_password():
    password = f"Test{random.randint(1000, 9999)}!"
    print(f"  Password: {password}")
    return password


def generate_name():
    name = f"Testov{random.randint(10, 99)}"
    print(f"  Name: {name}")
    return name


def generate_short_password():
    password = f"Sh{random.randint(10, 99)}"
    print(f"  Short password: {password}")
    return password
