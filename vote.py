# Initialize vote counts
options = {
    'Option 1': 0,
    'Option 2': 0,
    'Option 3': 0
}

# Function to display voting options
def display_options():
    print("Voting Options:")
    for key, value in options.items():
        print(f"{key}: {value}")

# Function to vote for an option
def vote(option):
    if option in options:
        options[option] += 1
        print(f"You voted for {option}!")
    else:
        print("Invalid option. Please vote again.")

# Main program loop
while True:
    display_options()
    print("\nEnter the option you want to vote for (or 'done' to exit): ")
    choice = input().strip()

    if choice.lower() == 'done':
        break
    else:
        vote(choice)

# Display final results
print("\nFinal Voting Results:")
for key, value in options.items():
    print(f"{key}: {value}")

