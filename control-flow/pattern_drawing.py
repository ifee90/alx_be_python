# Ask the user to input the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Use a while loop to go through each row
while row < size:
    # Use a for loop to print asterisks in each column
    for column in range(size):
        print("*", end="")
    print()  # Move to the next line after each row
    row += 1
