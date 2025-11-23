import json
from datetime import datetime

DB = "books.json"

def load_data():
    try:
        with open(DB, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(items):
    with open(DB, "w") as f:
        json.dump(items, f, indent=4)


def add_book():
    all_books = load_data()

    b_id = input("Book ID: ").strip()
    title = input("Book Title: ").strip()
    writer = input("Author: ").strip()

    new_book = {
        "id": b_id,
        "title": title,
        "author": writer,
        "issued": False,
        "issuer": "",
        "issue_date": ""
    }

    all_books.append(new_book)
    save_data(all_books)
    print("✔ Book added.\n")


def show_books():
    data = load_data()

    if not data:
        print("No books found.\n")
        return

    for b in data:
        print("\nID:", b["id"])
        print("Title:", b["title"])
        print("Author:", b["author"])
        print("Issued:", b["issued"])
        if b["issued"]:
            print("Issuer:", b["issuer"])
            print("Issued On:", b["issue_date"])
        print("-" * 40)


def issue_book():
    data = load_data()
    bid = input("Enter Book ID to Issue: ").strip()

    for b in data:
        if b["id"] == bid:

            if b["issued"]:
                print("Book already issued.\n")
                return

            name = input("Enter issuer name: ").strip()
            b["issued"] = True
            b["issuer"] = name
            b["issue_date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            save_data(data)
            print("✔ Book Issued.\n")
            return

    print("Book ID not found.\n")


def return_book():
    data = load_data()
    bid = input("Enter Book ID to Return: ").strip()

    for b in data:
        if b["id"] == bid:

            if not b["issued"]:
                print("Book was not issued.\n")
                return

            d1 = datetime.strptime(b["issue_date"], "%Y-%m-%d %H:%M:%S")
            d2 = datetime.now()

            total_days = (d2 - d1).days
            overdue = total_days - 7
            fine = overdue * 50 if overdue > 0 else 0

            b["issued"] = False
            b["issuer"] = ""
            b["issue_date"] = ""

            save_data(data)

            print("✔ Book Returned.")
            print("Days kept:", total_days)
            print("Fine:", fine, "/-\n")
            return

    print("Book ID not found.\n")