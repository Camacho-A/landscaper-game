money = 0
hasScissors = False
hasPushLawnMower = False
hasBatteryPoweredLawnMower = False
hasLandscapingTeam = False

print("Lets play Landscaper! To win you must own a landscaping team and have $1000 or more. Good luck!")

while ((money < 1000) or (hasLandscapingTeam == False)):
    # must be OR to have both true to end the game   

    print("--- Make a selection from the options below --- :")
    user_choice = input(
        "[1] Save money & cut the lawn with your teeth [2] Buy a set of scissors for $5 [3] Cut the lawn with your set of scissors [4] Buy a push lawnmower for $25 [5] Cut the lawn with push lawnmower [6] Buy a battery-powered lawnmower for $250 [7] Cut the lawn with your battery-powered lawnmower [8] Hire a team of landscapers for $500 [9] Have your landscaping team cut the lawn [10] Check Money ")


    if (user_choice == "1"):
        money += 1

        print(
            f"You just cut the lawn with your teeth and earned $1! Total money is: ${money}\n")


    if (user_choice == "2"):
        # check to see if your have the listed tool. 
        if (hasScissors == True):
            print("You already own scissors.\n")
        # check if player has enough money
        elif (money >= 5):
            money -= 5             # subtract tool cost
            hasScissors = True     # user has x tool now
            print("WooHoo! You bought a pair of scissors. Now you have a tool you can cut lawns with a little faster.\n")
        else:
            print("You do not have enough money. Cut more lawns with your teeth to earn some money!\n")


    if (user_choice == "3"):
        # check to see if your have the listed tool.
        if (hasScissors == True):
            money += 5
            print(
                f"Sweet! You just cut the lawn with your scissors and just earned $5! Total money is: ${money}\n")
        else:
            print("Bummer! You have not purchased a set of scissors yet. Buy your first set of scissors to make more money!\n")


    if (user_choice == "4"):
        # check to see if your have the listed tool.
        if (hasPushLawnMower == True):
            print("You already own a push lawnmower. Get working!\n")
        # check if player has enough money
        elif (money >= 25):
            money -= 25
            hasPushLawnMower = True
            print("Sweet! You purchased a push lawnmower. Now you can cut lawns even faster.\n")
        else:
            print("Sorry, you do not have enough money. Cut more lawns with your teeth or the tools you do own.\n")


    if (user_choice == "5"):
      # check to see if your have the listed tool.
        if (hasPushLawnMower == True):
            money += 50
            print(
                f"Hooray! You just cut the lawn with the push lawnmower and earned $50! Total money is: ${money}\n")
        else:
            print("Sorry, you do not have a push lawnmower yet. Buy one first!\n")


    if (user_choice == "6"):
       # check to see if your have the listed tool.
        if (hasBatteryPoweredLawnMower == True):
            print("You already own a battery-powered lawnmower.\n")
                    # check if player has enough money
        elif (money >= 250):
            money -= 250
            hasBatteryPoweredLawnMower = True
            print(
                "Woohoo! You purchased a battery-powered lawnmower! Now you can cut lawns with it.\n")
        else:
            print(
                "Sorry, you do not have enough money. Cut more lawns with your teeth or the tools you do own.\n")
            
            
    if (user_choice == "7"):
              # check to see if your have the listed tool.
        if (hasBatteryPoweredLawnMower == True):
            money += 100
            print(
                f"Hooray! You just cut the lawn with your battery-powered lawnmower and earned $100! Total money is: ${money}\n")
        else:
            print("Sorry, you do not have a battery-powered lawnmower yet. Buy one first!\n")
           
            
    if (user_choice == "8"):       
        if (hasLandscapingTeam == True):
            print("You already hired a landscaping team.\n")
        elif (money >= 500):
            money -= 500
            hasLandscapingTeam = True
            print(
                "You purchased a landscaping team! Now put them to work.\n")
        else:
            print("Sorry, you do not have enough money. Cut more lawns with your teeth or the tools you do own\n")
            
            
    if (user_choice == "9"):
              # check to see if your have the listed tool.
        if (hasLandscapingTeam == True):
            money += 250
            print(
                f"Hooray! You just used your landscaping team to cut the lawn and earned $250! Total money is: ${money}\n")
        else:
            print("Sorry, you have not hired a landscaping team. Hire them first!\n")


    if (user_choice == "10"):
        print(f"Total money is: ${money}")
        
print(
    f"Congratulations! You've won the game with your landscaping team with a total of ${money}.")
