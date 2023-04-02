# Import the ASCII art and social media account data
from art import logo, vs
from game_data import data
import random
# Import the function for clearing the console screen
from replit import clear

# Get the total number of social media accounts
total = len(data)
# Initialize a variable to track if the user has lost the game
lose = False

# Start the game loop
# The loop continues until the user loses
while(not lose):
  # Display the ASCII art
  print(logo)
  
  # Select the first social media account at random
  rand1 = random.randint(0,total)
  # Get the data for the selected account
  name1 = data[rand1]["name"]
  followers1 = data[rand1]["follower_count"]
  description1 = data[rand1]["description"]
  country1 = data[rand1]["country"]
  # Display the data for the first account
  print(f"Compare A: {name1}, {description1} from {country1}.")
  
  # Display the VS ASCII art
  print(vs)
  
  # Select the second social media account at random
  rand2 = random.randint(0,total)
  # Get the data for the selected account
  name2 = data[rand2]["name"]
  followers2 = data[rand2]["follower_count"]
  description2 = data[rand2]["description"]
  country2 = data[rand2]["country"]
  # Display the data for the second account
  print(f"Against B: {name2}, {description2} from {country2}.")
  
  # Determine which account has more followers
  correct = 'A' if (followers1 > followers2) else 'B'
  
  # Ask the user to guess which account has more followers
  ans = input("Who has more followers? Type 'A' or 'B':")
  # Display the correct answer
  print(correct)
  
  # If the user's guess is correct, update the random index for the next round
  if(ans == correct):
    if(correct == 'B'):
      rand1 = rand2
  # If the user's guess is incorrect, exit the game loop
  else:
    lose = True
  
  # Clear the console screen for the next round
  clear()