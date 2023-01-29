# Import the datetime module to handle date and time
import datetime

# Create a list to store the appointments
appointments = []

# Function to check if a specific time slot is available
def check_availability(day, time):
    for appointment in appointments:
        if appointment[0] == day and appointment[1] == time:
            return False
    return True

# Function to get an alternative time slot
def get_alternative(day):
    for i in range(1, 10):
        if check_availability(day, i):
            return i
    return None

# Function to make an appointment
def make_appointment(parent_name, child_name, day1, time1, day2, time2):
    # Check if the first preferred time slot is available
    if check_availability(day1, time1):
        appointments.append([day1, time1, parent_name, child_name])
        print("Appointment confirmed for " + parent_name + " with " + child_name + " on " + day1 + " at " + str(time1) + ":00 pm.")
    # If not, check if the second preferred time slot is available
    elif check_availability(day2, time2):
        appointments.append([day2, time2, parent_name, child_name])
        print("Appointment confirmed for " + parent_name + " with " + child_name + " on " + day2 + " at " + str(time2) + ":00 pm.")
    # If both preferred slots are unavailable, offer an alternative time
    else:
        alternative_day = None
        alternative_time = None
        if get_alternative(day1) != None:
            alternative_day = day1
            alternative_time = get_alternative(day1)
        elif get_alternative(day2) != None:
            alternative_day = day2
            alternative_time = get_alternative(day2)
        # If there are no available alternative slots, inform the parent
        if alternative_day == None:
            print("Sorry, all slots are fully booked. Please try again later.")
        else:
            appointments.append([alternative_day, alternative_time, parent_name, child_name])
            print("Appointment confirmed for " + parent_name + " with " + child_name + " on " + alternative_day + " at " + str(alternative_time) + ":00 pm.")

# Example usage of the function
make_appointment("John Smith", "Mary Smith", "Monday", 5, "Tuesday", 7)
make_appointment("Jane Doe", "John Doe", "Monday", 5, "Tuesday", 7)
