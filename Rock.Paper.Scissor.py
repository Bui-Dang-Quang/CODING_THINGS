import random


def RPS():
    count = 0
    gamecount = 1
    Bpoint = 0
    Upoint = 0

    for i in range(0, 5):
        count = count + 1
        print("\nTAKE THE ROUND",count)
        options = ["Rock", "Paper", "Scissor"]
        bot = random.choice(options)
        user = input("Make your decision: ")

        while user not in options:
            user = input("Make your decision PROPERLY: ")

        if user == "Rock" and bot == "Paper":
            print("Bot:", bot)
            print("User:", user)
            print("Bot wins")
            Bpoint = Bpoint + 1
        elif user == "Rock" and bot == "Scissor":
            print("Bot:", bot)
            print("User:", user)
            print("User wins")
            Upoint = Upoint + 1
        elif user == "Paper" and bot == "Rock":
            print("Bot:", bot)
            print("User:", user)
            print("User wins")
            Upoint = Upoint + 1
        elif user == "Paper" and bot == "Scissor":
            print("Bot:", bot)
            print("User:", user)
            print("Bot wins")
            Bpoint = Bpoint + 1
        elif user == "Scissor" and bot == "Rock":
            print("Bot:", bot)
            print("User:", user)
            print("Bot wins")
            Bpoint = Bpoint + 1
        elif user == "Scissor" and bot == "Paper":
            print("Bot:", bot)
            print("User:", user)
            print("User wins")
            Upoint = Upoint + 1
        else:
            print("Bot:", bot)
            print("User:", user)
            print("DRAW")

    print("\nFINAL RESULT:")
    if Bpoint > Upoint:
        print("- Bot's point:",Bpoint)
        print("- User's point:",Upoint)
        print("BOT WIN THE PRIZE")
    elif Bpoint < Upoint:
        print("- Bot's point:",Bpoint)
        print("- User's point:",Upoint)
        print("USER WIN THE PRIZE")
    else:
        print("- Bot's point:",Bpoint)
        print("- User's point:",Upoint)
        print("BOTH WIN THE PRIZE")
        gamecount = gamecount + 1
        print("\nGame",gamecount,",START!!!!!")
        RPS()
        
RPS()