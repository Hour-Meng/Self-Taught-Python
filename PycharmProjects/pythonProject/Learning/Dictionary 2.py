
Capital = {
    "Cambodia": "Phnom Penh",
    "USA": "Washington",
    "Russia": "Moscow"
}

def get_capital(user_input):
    # Convert the user input to lowercase for case-insensitive matching
    user_input_lower = user_input.lower()

    # Check if the lowercase input matches any country name
    for country in Capital:
        if user_input_lower == country.lower():
            return Capital[country]

    # If no match is found, provide an appropriate message
    return "Sorry, I don't have information about the capital of " + user_input

# Get user input
User = input("What's your country?: ")

# Call the function and print the result
print(get_capital(User))
