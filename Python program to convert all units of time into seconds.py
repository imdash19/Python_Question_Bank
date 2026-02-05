# Write a Python program to convert all units of time into seconds.

def convert_time_to_seconds():
    seconds = float(input("Enter seconds: "))
    minutes = float(input("Enter minutes: "))
    hours = float(input("Enter hours: "))
    days = float(input("Enter days: "))
    weeks = float(input("Enter weeks: "))
    months = float(input("Enter months (30 days): "))
    years = float(input("Enter years (365 days): "))

    total_seconds = (
        seconds +
        minutes * 60 +
        hours * 3600 +
        days * 86400 +
        weeks * 604800 +
        months * 2592000 +
        years * 31536000
    )

    print("\nTotal time in seconds =", total_seconds)

convert_time_to_seconds()