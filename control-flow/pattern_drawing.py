# Ask the user for the size of the pattern
pattern = int(input('Enter the size of the pattern: '))

# Use a for loop to print each row
for _ in range(pattern):
    print('*' * pattern)