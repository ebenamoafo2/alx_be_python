# Ask the user for the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# While loop for rows
while row < size:
    # For loop for columns
    for _ in range(size):
        print("*", end="")
    print()  # Move to the next line
    row += 1
