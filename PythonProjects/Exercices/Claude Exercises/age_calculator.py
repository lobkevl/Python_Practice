birth_year = int(input("Enter your birth year: "))
current_year = 2026
age = current_year - birth_year

if age < 13:
    print("You are a baby or child! 👶")
elif age < 18:
    print("You are a teenager! 🧑")
else:
    print("You are an adult! 👨")
