def name_counter():
    while True:
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name: ")
        firstname_count = len(first_name)
        lastname_count = len(last_name)
        if lastname_count < 2 or firstname_count < 2:
            print("One or both of your names don't contain enough letters")
        else:
            print(f"Your first name is {firstname_count} letters long and your last name is {lastname_count} letters long")
        break

name_counter()