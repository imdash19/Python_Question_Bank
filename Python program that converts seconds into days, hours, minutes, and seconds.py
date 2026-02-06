# Write a Python program that converts seconds into days, hours, minutes, and seconds.

def convert_seconds():
    total_seconds = int(input("Enter total seconds: "))

    if total_seconds < 0:
        print("Please enter a non-negative number of seconds.")
        return

    days = total_seconds // (24 * 3600)
    remaining_seconds = total_seconds % (24 * 3600)

    hours = remaining_seconds // 3600
    remaining_seconds %= 3600

    minutes = remaining_seconds // 60
    seconds = remaining_seconds % 60

    print("\nConverted Time:")
    print(f"Days    : {days}")
    print(f"Hours   : {hours}")
    print(f"Minutes : {minutes}")
    print(f"Seconds : {seconds}")

convert_seconds()