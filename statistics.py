# Library file: statistics.py

def calculate_statistics(numbers):
    total = 0
    count = 0

    for num in numbers:
        if num > 0:
            total += num
            count += 1

    average = total / count if count > 0 else 0

    return count, total, average

# Main program: main.py