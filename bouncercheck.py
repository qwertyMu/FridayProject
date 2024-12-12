def bouncer_check(people):
    for person in people:
        name, age, is_drunk = person
        print(f"Hello, " + name " ! Welcome to the bar.")

        if age < 18:
            print("Sorry, you are underage. You cannot enter.")
        elif is_drunk:
            print("Sorry, you seem drunk. You cannot enter.")
        else:
            print("You are good to go. Welcome inside!")

        print("-")

# List of people to be checked (name, age, is_drunk)
people_list = [
    ("Alice", 25, False),
    ("Bob", 17, False),
    ("Charlie", 30, True),
    ("Daisy", 19, False)
]

# Run the bouncer check
bouncer_check(people_list)