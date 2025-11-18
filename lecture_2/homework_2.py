def generate_profile(age):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


print("Hello!Welcome to the program")
user_name = input("Please enter your full name: ")
birth_year_str = input("Please enter your birth year: ")
birth_year = int(birth_year_str)
if birth_year > 2025 or birth_year < 1900:
    print("Invalid birth year.")
    exit()
else:
    current_age = 2025 - birth_year

hobbies = []
while True:
    hobby = input("Enter a favorite hobby or type 'stop' to finish:")
    if hobby == "stop":
        break
    else:
        hobbies.append(hobby)
life_stage = generate_profile(current_age)
user_profile = {"name": user_name, "age": current_age,
                "stage": life_stage, "hobbies": hobbies}
print("Profile Summary:M")
print(f"Name: {user_profile['name']}")
print(f"Age: {user_profile['age']}")
print(f"Life Stage: {user_profile['stage']}")
if not hobbies:
    print("You didn't mention any hobbies.")
else:
    print(f"Favorite Hobbies({len(user_profile['hobbies'])})")
    for hobby in user_profile["hobbies"]:
        print(f"-{hobby}")
