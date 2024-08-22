# task 1
# place = input("Choose a place: forest or cave? ")

# if place = "forest":
#     action = input("climb a tree or cross a river?")
#     if action = "climb a tree":
#         print("You found a bird's nest!")
#     else action = "cross a river":
#         print("You found a boat!")
# elif place = "cave":
#     print("You find a hidden treasure!")

#task 1 FIXED CODE
# task 2 add if user chooses "cave" ask if they want to use "light a torch" or "procceed in the dark"
# task 3 add a pass in ending for if user inputs any wrong combination at anytime 

place = input("Choose a place: forest or cave? ")


if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    action = input(" light a torch or procceed in the dark?")
    if action == "light a torch":
     print("You find a hidden treasure!")
    elif action == "procceed in the dark":
     print("Be very cautious!")
    else: 
       print("oops wrong option")
       pass

    


