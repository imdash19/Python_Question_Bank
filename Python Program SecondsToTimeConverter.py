# Reads an integer representing seconds and converts it to a formatted time string (HH:MM:SS). Handles large second values correctly with proper hour calculation.

seconds = int(input())

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{hours:02d}:{minutes:02d}:{secs:02d}")