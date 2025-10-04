# explore_datetime.py

from datetime import datetime, timedelta

# Part 1: Display the Current Date and Time
def display_current_datetime():
    current_date = datetime.now()  # get current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print("Current date and time:", formatted_date)

# Part 2: Calculate a Future Date
def calculate_future_date(days: int):
    today = datetime.today().date()
    future_date = today + timedelta(days=days)
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Run the script
if __name__ == "__main__":
    # Part 1
    display_current_datetime()

    # Part 2
    try:
        days = int(input("Enter the number of days to add to the current date: "))
        calculate_future_date(days)
    except ValueError:
        print("Please enter a valid integer.")
