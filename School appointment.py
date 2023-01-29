import csv


def get_appointments():
    # Read appointments from file
    appointments = []
    with open('appointments.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            appointments.append(row)
    return appointments


def save_appointments(appointments):
    # Write appointments to file
    with open('appointments.csv', 'w') as f:
        writer = csv.writer(f)
        for appointment in appointments:
            writer.writerow(appointment)


def allocate_appointment(parent_name, parent_preferences, appointments):
    # Try to allocate one of the preferred appointment times
    for preference in parent_preferences:
        for appointment in appointments:
            if preference[0] == appointment[0] and preference[1] == appointment[1] and appointment[2] == '':
                appointment[2] = parent_name
                return True

    # If preferred times are not available, allocate an alternative appointment
    for appointment in appointments:
        if appointment[2] == '':
            appointment[2] = parent_name
            return True

    # If no appointment is available
    return False


def display_timetable(appointments):
    # Display a timetable of appointments for each evening
    for appointment in appointments:
        print(f"{appointment[0]} {appointment[1]}: {appointment[2]}")


def display_appointment(parent_name, appointments):
    # Display details of individual appointments for parents
    for appointment in appointments:
        if appointment[2] == parent_name:
            print(f"{appointment[0]} {appointment[1]}")


# Main program
appointments = get_appointments()

# Example input of parent's details and appointment preferences
parent_name = input("Enter parent name: ")
preference_1 = input("Enter first preference (day time): ")
preference_2 = input("Enter second preference (day time): ")
parent_preferences = [preference_1, preference_2]

# Allocate appointment
if allocate_appointment(parent_name, parent_preferences, appointments):
    print("Appointment allocated.")
else:
    print("No appointment available.")

# Save appointments
save_appointments(appointments)

# Display timetable
display_timetable(appointments)

# Display individual appointment
display_appointment(parent_name, appointments)
