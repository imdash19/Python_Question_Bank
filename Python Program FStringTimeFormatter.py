# Reads hour, minute, and second components and formats them as a standardized time string (HH:MM:SS) using f-string syntax. Modern approach to time formatting.

hour = int(input())
minute = int(input())
second = int(input())

print(f"{hour:02d}:{minute:02d}:{second:02d}")