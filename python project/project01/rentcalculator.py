# Rent Calculator 
# A simple tool to calculate how much rent each roommate should pay

def welcome_message():
    print(" Welcome to the Rent Calculator!")
    print("Let's figure out how much rent each person should pay.\n")


def get_user_inputs():
    try:
        total_rent = float(input("Enter the total rent amount ($): "))
        num_people = int(input("How many people are sharing the rent? "))

        if total_rent < 0 or num_people <= 0:
            print("Please enter positive numbers only.")
            return get_user_inputs()

        return total_rent, num_people
    except ValueError:
        print(" Oops! That doesn't look like a number. Try again.")
        return get_user_inputs()


def calculate_rent_per_person(total_rent, num_people):
    return round(total_rent / num_people, 2)


def show_result(per_person_rent):
    print(f"\n💰 Each person should pay: ${per_person_rent}")
    print("Thank you for using the Rent Calculator! ")


def main():
    welcome_message()
    total_rent, num_people = get_user_inputs()
    per_person_rent = calculate_rent_per_person(total_rent, num_people)
    show_result(per_person_rent)


if __name__ == "__main__":
    main()
