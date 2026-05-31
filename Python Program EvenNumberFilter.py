# Reads space-separated integers and filters only the even numbers, creating a list of even integers. The program validates each number against the evenness condition during processing.

numbers = list(map(int, input().split()))

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
