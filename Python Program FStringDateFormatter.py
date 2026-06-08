# Reads year, month, and day components and formats them as a standardized date string (YYYY-MM-DD) using f-string syntax. Modern approach to date formatting.

year = int(input())
month = int(input())
day = int(input())

print(f"{year:04d}-{month:02d}-{day:02d}")