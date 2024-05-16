print("What is your name")
name = input()
print("It is nice to meet you " + name)

ready = False
while ready == False:
	print("Are you ready to play?")
	choice = input()
	if choice == "yes":
		print("Okay we will start")
		ready = True
	else:
		print("Just tell me when you are ready")
Doorstext = ("You opened the door and walked through it and there was ")
Doors = ["a way to escape." , "a bottomless pit." , "a room that contains tearsure." , "a big red dragon."]
alive = False
while alive == False:
	print("You are in a room with 4 doors on each side. Which door do you want to walk through? (door 1,2,3, or 4)")
	choice = input()
	if choice == "1" or "door 1":
		print( Doorstext + Doors + "You run out of the dungeon.")
		alive = True
	elif choice == "2" or "door 2":
		print( Doorstext + Doors + "You didn't notice the bottomless pit when you walked in the room and now you will be falling to your death forever"
	elif choice == "3" or "door 3":
		print( Doorstext + Doors + "	
	else:
		print("You have died. Do you want to play again?"
		
		

	
	
