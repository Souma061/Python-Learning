import json
from pathlib import Path
from encryption import encrypt_pass, decrypt_pass

FILE = Path(__file__).resolve().parent / "storage.json"


def load_data(master_pass):
    if not FILE.exists():
        return {}

    with open(FILE, "r", encoding="utf-8") as f:
        encrypted = f.read()

    if not encrypted:
        return {}

    try:
        decrypted = decrypt_pass(encrypted, master_pass)
        return json.loads(decrypted)
    except Exception:
        return None


def save_data(data, master_pass):
    encrypted = encrypt_pass(json.dumps(data), master_pass)
    with open(FILE, "w", encoding="utf-8") as f:
        f.write(encrypted)


def set_entry(data, service, username, password):
    service = service.strip()
    username = username.strip()
    password = password.strip()

    if not service or not username or not password:
        raise ValueError("Service, username, and password are required.")

    data[service] = {"username": username, "password": password}


def get_entry(data, service):
    return data.get(service.strip())


def list_entries(data, search_term=""):
    search_term = search_term.strip().lower()
    entries = []

    for service, credentials in sorted(data.items()):
        if search_term and search_term not in service.lower():
            continue
        entries.append((service, credentials["username"], credentials["password"]))

    return entries


def delete_entry(data, service):
    return data.pop(service, None) is not None
