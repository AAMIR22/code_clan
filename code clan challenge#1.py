#A quick note
# In this challenge, used datetime modules to work with dates & exception handling
# Defined a function
# We used the strptime from datetime to convert the string in to a date time object
# datetime.now() to get the current date
# Then calculated the difference and adjust it for negative years,months or dates
# Additionally, added a birthday wishes for the same dates

from datetime import datetime


def calculate_exact_age():
    try:
        current_date = datetime.now()
        print(f"Current Date & Time: {current_date} ")
        birth_date = input("Enter your birth date (YYYY-MM-DD): ")
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

        age_years = current_date.year - birth_date.year
        age_months = current_date.month - birth_date.month
        age_days = current_date.day - birth_date.day
        if age_years < 0:
            raise ValueError
        if age_years == 0:
            if age_months < 0:
                raise ValueError
            if age_months == 0:
                if age_days < 0:
                    raise ValueError
                if age_days == 0:
                    print("Happy Birthday!!")
        if current_date.month < birth_date.month:
            age_years -= 1
            age_months += 11
        elif current_date.month == birth_date.month:
            if current_date.day < birth_date.day:
                age_years -= 1
                age_months += 11
                age_days += 30



        print(f"You are {age_years} years, {age_months} months, and {age_days} days old.")
    except ValueError:
        print("Invalid input. Please enter the correct date. Check the format YYYY-MM-DD or check entered date is before the current date")


# Calling function
calculate_exact_age()