def name_counter():
    while True:
        first_name = input("Please enter your first name: ")
        last_name = input("Please enter your last name name: ")
        firstname_count = len(first_name)
        lastname_count = len(last_name)
        if lastname_count < 2 or firstname_count < 2:
            print("Not enough letters")
        else:
            print(f"Your first name is {firstname_count} letters long and your last name is {lastname_count} letters long")
            break

name_counter()