import random
print(" _     _            _    _            _    \n| |   | |          | |  (_)          | |   \n| |__ | | __ _  ___| | ___  __ _  ___| | __\n| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /\n| |_) | | (_| | (__|   <| | (_| | (__|   < \n|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\ \n                       _/ |                \n                      |__/                 ")

while True:
    yy=input("To play blackjack enter y else n:")
    if yy=="n":
        print("Okie!! Have a good day")
        break
    card1,card2=random.randint(1,10),random.randint(1,10)
    compcard1,compcard2=random.randint(1,10),random.randint(1,10)
    lime=[card1,card2]
    licomp=[compcard1,compcard2]
    print("your hand is:",lime)
    print("Computers hand is:",licomp[0])
    answer=input("Hit or Pass?")
    if answer=="Hit":
        card3=random.randint(1,10)
        compcard3=random.randint(1,10)
        sum=card1+card2+card3
        compsum=compcard1+compcard2+compcard3
        lime.append(card3)
        licomp.append(compcard3)
        if sum>21:
            print("you lose",lime)
        elif compsum>21:
            print("You win!! The computers cards were:",licomp)
        else:
            if sum>compsum:
                print("You win! as your cards are :",lime,"and comps cards are :",licomp)
            elif compsum==sum:
                print("draw")
            else:
                print("You lose as your cards were:",lime,"and the computers cards were",licomp)
    else:
        x=random.randint(1,2)
        if x==1:    #its gonna hit
            compcard3=random.randint(1,10)
            compsum=compcard1+compcard2+compcard3
            licomp.append(compcard3)
            sum=card1+card2
            if compsum>21:
                print("You win!! as the computers cards were:",licomp,"and yours were",lime)
            elif compsum>sum:
                print("You lose!! as the computers cards were:",licomp,"and yours were",lime)
            else:
                print("You win!! as the computers cards were:",licomp,"and yours were:",lime)
        else:       #its gonna pass
            sum=card1+card2
            compsum=compcard1+compcard2
            if sum>compsum:
                print("You win!! as your cards were ",lime,"and computeres cards were:",licomp)
            else:
                print("You lose!! as your cards were ",lime,"and computeres cards were:",licomp)
    licomp=list()
    lime=list()
                 
                            