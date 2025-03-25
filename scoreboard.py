def scoreboard ():
    players = []
    scores = []
    
    print("Are you new to the game?")
    new = input("Yes or No: "):
         if new == "Yes":
            name = input("What is your name? ")
            players.append(name)
            score = 0
            scores.append(score)
            print("Welcome to the game, ", name)
        else:
            print("Welcome back!")