# You are building a social media preview feature that displays shortened versions of long posts. When users write long messages, you need to show a preview with a limited number of characters followed by "..." (ellipsis) to indicate there's more content.Here's how it works:

# You have a text message that might be very long
# You have a maximum character limit for the preview
# If the message is longer than the maximum limit, you cut it off at that limit and add "..." at the end
# If the message is equal to or shorter than the limit, display the full message without adding "..."
# Example 1: Message = "Python is an amazing programming language", Max length = 20
# Output: "Python is an amazing..."Example 2: Message = "Hello World", Max length = 20
# Output: "Hello World" (no ellipsis needed)You need to create a program that:

# Takes a text message as input
# Takes the maximum preview length as input
# Displays the truncated message with "..." if it exceeds the limit, or the full message if it doesn't
# Input Format:

# First line: Text message (string)
# Second line: Maximum preview length (integer)
# Output Format:

# Print the truncated message with "..." if it's too long, otherwise print the full message

message = input()
max_length = int(input())

if len(message) > max_length:
    print(message[:max_length] + "...")
else:
    print(message)
