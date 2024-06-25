import random
#create the dictionary for everything to operate
#creating the intro statement first
print("Welcome to the rock paper scissors game by Me, Mohammed aka Moh AKA Blackwing, lets get it")
moveon = input("Please press enter to continue: ")
def game():
    Tries = 0
    while Tries < 3:
        #create the list for rock paper and scissors
        gameoption = ["ROCK", "PAPER", "SCISSORS"]
        userchoice = input("Pick your element niggaaa: " + str(gameoption))
        computerchoice = random.choice(gameoption)
        print("COMPUTER CHOSE: " + computerchoice)
        #This was my long ass version that i had to check ai for when it wasnt working but it turned out the code wasnt the problem but rather saying "random.choices" instead of "random.choice" ffs
        if userchoice == "ROCK" and computerchoice == "ROCK":
            print("ROCK V ROCK, I HEAR VOICES IN THE AIR, GET IT??, NAHH FUCK YOU THEN, ITS A DRAW.")
            
        elif userchoice == "ROCK" and computerchoice == "PAPER":
            print("ITS CRAZZY THAT A BIG ASS ROCK GOT BEATEN BY A PAPER LOL")
            
        elif userchoice == "ROCK" and computerchoice == "SCISSORS":
            print("YAYYYY DWAYNE JOHNSON WINS😁")
            
        elif userchoice == "PAPER" and computerchoice == "ROCK":
            print("YOOOO YOU BEAT THE FINAL BOSS, PAPER WINS")
            
        elif userchoice == "PAPER" and computerchoice == "PAPER":
            print("A MOTHERFUCKING DRAW???!! BOOOOOOOOOO ")
            
        elif userchoice == "PAPER" and computerchoice == "SCISSORS":
            print("SCISSORS JUST COOKED YOUR LAME AHHH")
            
        elif userchoice == "SCISSORS" and computerchoice == "ROCK":
            print("DWAYNE JOHNSON JUST KNOCKED YOUR ASS OUT LOL")
            
        elif userchoice == "SCISSORS" and computerchoice == "PAPER":
            print("YOOO YOU CUT THAT BUM ASS PAPER UPPP CUHH")
            
        elif userchoice == "SCISSORS" and computerchoice == "SCISSORS":
            print("Y'ALL SCISSORING UP MORE THAN THE LESBIANS LOL")
        Tries += 1
#AI version
        """if userchoice == computerchoice:
            print("It's a tie")
        elif (userchoice == "ROCK" and computerchoice == "SCISSORS") or (userchoice == "PAPER" and computerchoice == "ROCK") or (userchoice == "SCISSORS" and computerchoice == "PAPER"):
            print("You Win")
        else:
            print("Computer wins")"""
game()
print("©mohtech")