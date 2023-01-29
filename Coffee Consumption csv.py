import csv

# Create a list to store the data
coffee_consumption = []

# Function to add data to the list
def add_data(day, kilograms):
    coffee_consumption.append([day, kilograms])

# Function to save data to a file
def save_data_to_file(file_name):
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for i in range(0, len(coffee_consumption), 7):
            writer.writerow(coffee_consumption[i:i+7])

# Add data for each day
add_data("Monday", 2.5)
add_data("Tuesday", 2.6)
add_data("Wednesday", 2.7)
add_data("Thursday", 2.8)
add_data("Friday", 2.9)
add_data("Saturday", 3.0)
add_data("Sunday", 3.1)

# Save data to a file
save_data_to_file("coffee_consumption.csv")

# =============Example with 2D Array=========================
# This program creates a 2D list coffee_data containing
# the number of kilograms of coffee used by the local cafe
# on each day of the week. Then, it opens a file called
# "coffee_data.csv" in write mode using the open() function.
# Then it creates a CSV writer object and uses a for loop to
# write each row of the coffee_data list to the file.
# Finally, it prints a message to confirm that the data has been
# saved to the file. The file can be opened in excel and it will
# show the data in the form of a table.
import csv

# Create a 2D list to represent the data
coffee_data = [
    ["Monday", 5, 4, 3, 6, 8, 4, 7],
    ["Tuesday", 6, 8, 5, 3, 7, 4, 6],
    ["Wednesday", 4, 5, 8, 7, 6, 5, 3],
    ["Thursday", 2, 4, 6, 8, 5, 7, 4],
    ["Friday", 7, 8, 5, 4, 6, 3, 5],
    ["Saturday", 5, 6, 7, 4, 5, 8, 4],
    ["Sunday", 8, 7, 6, 5, 4, 3, 2]
]

# Open a file for writing
with open("coffee_data.csv", "w") as csv_file:
    # Create a CSV writer
    csv_writer = csv.writer(csv_file)

    # Write the data to the file
    for row in coffee_data:
        csv_writer.writerow(row)

# Print message to confirm data has been saved
print("Coffee data has been saved to coffee_data.csv.")
