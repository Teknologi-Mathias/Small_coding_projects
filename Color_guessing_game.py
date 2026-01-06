global score # Global, så den ikke bliver sat til 0 hvis den er i en funktion der bliver kaldt. 
score = 0

def color_chosen():
    import random
    color_list = ("red", "blue", "green")
    return random.choice(color_list) # random.choice ved valg af item i tupple. 

def game_start():
    global color # color sat til global så de andre funktioner kan benytte, og i game_start så den opdaterer ved hvert kald af funktion. 
    color = color_chosen()
    game()

def game():
    guess = str(input("Guess; red, green or blue?: "))
    global score # Her er score sat i funktion, så den kan kalde på score udenfor funktionen, men også tillæge ved rigtigt gæt. 

    if guess.lower() == color:
        score += 1 # Tillægger score fordi man gættede korrekt
        print("Congrats, you've guessed correct!")
        game_repeat()
    
    elif guess not in ["red", "green", "blue"]
        print("Invalid color")
        return game()

    else: 
        print("You've guessed wrong! Try again")
        print(" ")
        return game()


def game_repeat():
    print(" ")
    print(f"Your current score is {score} (+1)")
    answer = str(input("Do you want to play again? Y/N: "))

    if answer.lower() == "yes" or answer.lower() == "y":
        game_start()
    
    elif answer.lower() == "n" or answer.lower() == "no":
        print(" ")
        game_end()

    elif answer == "":
        print("Yes or no?")
        return game_repeat()
    
    else:
        print("No Y/N is the expression for quitting")
        game_end()

def game_end(): 
    print("You've chosen to end the game")
    print(" ")
    print(f"Your final score were {score}")    # tillæg funktion, hvor mange gange personen har gættet den rigtige farve ved afslutning af spillet. 


game_start()
