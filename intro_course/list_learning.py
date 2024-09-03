import os
file_path = 'sports03.txt'

def read_sports(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return [line.strip() for line in file.readlines()]
    return []

def write_sports(file_path, sports_list):
    with open(file_path, 'w') as file:
        for sport in sports_list:
            file.write(f"{sport}\n")

repeat = "yes"
while repeat == "yes":
    sports = read_sports(file_path)
    new_sport = input("Enter your favourite sport: ").capitalize().strip()
    if new_sport:
        if new_sport in sports:
            print(f"You have already entered {new_sport}")
        else:
            sports.append(new_sport)
            print("Updated sports list:", sports)
    else:
        print("No sports added")
    write_sports(file_path, sports)
    print("Sports list:")
    for i, sport in enumerate(sports):
        print(f"Sport {i+1}: {sport}")
    repeat = input("Do you want to add more sports? (yes/no): ").strip().lower()
print("Thank you!")

# Suggested Improvements:
