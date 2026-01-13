import random

class PerfectGuessGame:

    def __init__(self):
        self.generate_random_number = random.randint(1,100)
        self.attempts = 0
        

        
    def get_user_guess(self):
      while True:   
        try:
            user_guess = int(input("Enter the users choice : "))
            self.attempts +=1
            return user_guess
           
        except ValueError:
          print("Please enter a valid integer")
      
              
    def check_guess(self,user_guess):
         if user_guess > self.generate_random_number :
            return "high"

         elif user_guess < self.generate_random_number :
            return "low"

         else:
            return "correct"
         
    def reset_game(self):
       self.generate_random_number = random.randint(1, 100)
       self.attempts = 0    

            
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

        # Replay decision
        play_again = input("\nPlay again? (yes/no): ").lower()
        if play_again == "yes":
            self.reset_game()
        else:
            print("\nThanks for playing! 👋")
            break              
             

game = PerfectGuessGame()
game.play()









   

            




