# Function to calculate the sum of a list of numbers
def add(addends: list[float]) -> float:
    # Initialize sum to 0
    sum = 0
    # Iterate through each number in the list and add it to the sum
    for addend in addends:
        sum = sum + addend

    # Return the final sum
    return sum


# Function to describe what the 'add' function does
def describe_add() -> str:
    return 'Returns the sum of all of the numbers passed to it.'


# Main block: only runs if the script is executed directly (not imported)
if __name__ == '__main__':
    import sys  # Import sys to access command-line arguments

    # Print the description of the 'add' function
    print(describe_add())

    # Check if any command-line arguments were provided (besides the script name)
    if len(sys.argv) > 1:
        # Convert command-line arguments (excluding the script name) to floats
        addends = [float(arg) for arg in sys.argv[1:]]
        # Print the result of adding the numbers
        print(add(addends))
