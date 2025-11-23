import library

while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    ch = input("Enter choice: ").strip()

    if ch == "1":
        library.add_book()

    elif ch == "2":
        library.show_books()

    elif ch == "3":
        library.issue_book()

    elif ch == "4":
        library.return_book()

    elif ch == "5":
        print("Bye!")
        break

    else:
        print("Invalid choice.\n")