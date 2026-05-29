import random
logo =("""

 / ___|_   _  ___  ___ ___  |_   _| |__   ___ 
| |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ 
| |_| | |_| |  __/\__ \__ \   | | | | | |  __/ 
 \____|\__,_|\___||___/___/   |_| |_| |_|\___|
      

| \ | |_   _ _ __ ___ | |__   ___ _ __        
|  \| | | | | '_ ` _ \| '_ \ / _ \ '__|       
| |\  | |_| | | | | | | |_) |  __/ |          
|_| \_|\__,_|_| |_| |_|_.__/ \___|_|   """)


print(logo)
print("Let me think of a number between 1 to 50.\n")
level = input("Choose level of difficulty... Type 'easy' or 'hard': ")

chances = 0

if level == "easy":
    chances = 10
elif level == "hard":
    chances = 5

end_Program = False
random_number = random.randint(1, 50)

while not end_Program:
    print(f"\nYou have {chances} attempts remaining to guess the number!")
    your_guess = int(input("Make a guess: "))

    if your_guess == random_number:
        print("🎉 You guessed it right! Good job!")
        end_Program = True

    elif your_guess < random_number:
        print("Your guess is too low.")
        chances -= 1

    else:
        print("Your guess is too high.")
        chances -= 1

    if chances == 0 and not end_Program:
        print("\n❌ You ran out of attempts!")
        print(f"The correct number was: {random_number}")
        end_Program = True
