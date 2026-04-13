# TODO: 1 enter message 2 save the encrypted message in a file 3 read the encrypted message from the file 4 decrypt the message and print it


import json
import os
from encryption import encrypt_pass, decrypt_pass

FILE = "storage.json"


def load_data(master_pass):
    if not os.path.exists(FILE):
        return {}

    with open(FILE, "r") as f:
        encrypted = f.read()

    if not encrypted:
        return {}

    try:
        decreapted = decrypt_pass(encrypted, master_pass)
        return json.loads(decreapted)
    except Exception as e:
        print("Error decrypting data. Check your master password.")
        return None


def save_data(data, master_pass):
        encrypted = encrypt_pass(json.dumps(data), master_pass)
        with open(FILE, "w") as f:
            f.write(encrypted)


def add_entry(data):
    service = input("Enter service name: ")
    username = input("Enter username: ")
    password = input("Enter password: ")

    if service in data:
        print("Service already exists. Use update to change the password.")
        return
    else:
        data[service] = {"username": username, "password": password}
        print(f"Entry for {service} added.")



def view_entries(data):
    if not data:
        print("No entries found")
        return

    for service,credentials in data.items():
        print(f"Service: {service}")
        print(f"Username: {credentials['username']}")
        print(f"Password: {credentials['password']}")
        print("-" * 20)


def search_entries(data):
    service = input("Enter service name to search: ")
    if service in data:
        credentials = data[service]
        print(f"Service: {service}")
        print(f"Username: {credentials['username']}")
        print(f"Password: {credentials['password']}")
    else:
        print("Service not found.")
