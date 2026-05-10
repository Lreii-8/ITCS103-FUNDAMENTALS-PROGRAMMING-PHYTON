while True:

    print("\n===== DREAMS FILE MANAGER =====")
    print("1. Read inspiring messages")
    print("2. Add a new inspiring message")
    print("3. Rewrite the entire file")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # READ FILE
    if choice == "1":

        file = open("dreams.txt", "r")
        content = file.read()
        file.close()

        print("\n--- Inspiring Messages ---")
        print(content)

    # APPEND FILE
    elif choice == "2":

        message = input("\nEnter your new inspiring line: ")

        file = open("dreams.txt", "a")
        file.write("\n" + message)
        file.close()

        print("\nYour inspiration has been added!")

    # OVERWRITE FILE
    elif choice == "3":

        print("\nWarning: This will overwrite the file.")
        confirm = input("Type YES to continue: ")

        if confirm == "YES":

            new_message = input("\nWrite your new set of inspiring messages:\n")

            file = open("dreams.txt", "w")
            file.write(new_message)
            file.close()

            print("\nFile has been overwritten.")

        else:
            print("\nOperation cancelled.")

    # EXIT
    elif choice == "4":

        print("\nProgram ended.")
        break

    else:
        print("\nInvalid choice. Try again.")