from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in 'YYYY-MM-DD HH:MM:SS' format."""
    current_date = datetime.now()  # Get the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculate and display the future date after adding a specified number of days."""
    # Prompt the user to enter the number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print the future date in 'YYYY-MM-DD' format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Display current date and time
    display_current_datetime()
    
    # Calculate future date
    calculate_future_date()

if __name__ == "__main__":
    main()
