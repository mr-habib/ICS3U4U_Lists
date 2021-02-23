# Firstname, L
# mm/dd/yyyy
# Descriptive module title

# Enter the contents of the list here


user_response = input("Come up with a good prompt: ")

# Use strip and lower to ensure that no matter how the user types in done (Eg. "  DonE") it will finish
# Note, you don't have to do that, but you can if you want. I will only use good input :)
while user_response.strip().lower() != 'done':
  # Process the response assuming the user did not enter 'done'
  
  
  user_response = input("Same prompt as above: ")

