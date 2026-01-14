# Perfect Guess Game using Object-Oriented Programming (OOP)
# The game generates a random number and asks the user to guess it
import random

# This class handles the complete Perfect Guess game logic
class PerfectGuessGame:

    # Constructor: initializes the random number and attempt counter
    def __init__(self):
        self.generate_random_number = random.randint(1,100)
        self.attempts = 0
        
    # Safely takes user input and returns a valid integer guess   
    def get_user_guess(self):
      while True:   
        try:
            user_guess = int(input("Enter the users choice : "))
            self.attempts +=1
            return user_guess
           
        except ValueError:
          print("Please enter a valid integer")
      
    # Compares the user's guess with the generated number and returns the result          
    def check_guess(self,user_guess):
         if user_guess > self.generate_random_number :
            return "high"

         elif user_guess < self.generate_random_number :
            return "low"

         else:
            return "correct"
    # Resets the game by generating a new number and resetting attempts     
    def reset_game(self):
       self.generate_random_number = random.randint(1, 100)
       self.attempts = 0    

    # Controls the complete game flow: guessing, checking results, replay, and reset         
    def play(self):
     while True:
        # Guessing loop
        while True:
            guess = self.get_user_guess()
            result = self.check_guess(guess)

            if result == "high":
                print("Too high")

            elif result == "low":
                print("Too low")

            else:
                print(f"Perfect guess in {self.attempts} attempts!")
                break

       # Ask the user if they want to play again
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again == "yes":
            self.reset_game()
        else:
            print("\nThanks for playing! 👋")
            break              
             
# Create game object and start the game
game = PerfectGuessGame()
game.play()









   

            




