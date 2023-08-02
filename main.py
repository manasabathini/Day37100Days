print("🌟Star Wars Name Generator🌟")



fName= input("Enter your first name: ")

lName= input("Enter your last name: ")

mMname = input("Enter your mother's maiden name: ")

cityBorn = input("Enter the city where you were born: ")

name = f"{fName.strip()[:3].title()}{lName.strip()[:3].lower()} {mMname.strip()[:2].title()}{cityBorn.strip()[-3:].lower()}"

print(f"Your Star Wars name is  {name}")