# 1

x = True
mylist = []
while x:
	userlist = input("Please enter your favorite game(Enter 'Game Over!' to stop):")
	print("The game entered was: " +str(userlist))
	if userlist == "Game Over!":
		print("The input was Game Over!. Exiting...")
		x = False
	else:
		mylist.append(userlist)
		continue
print("Game list: " , mylist)


#2

for x in mylist:
	print(x)

#3
y = True
bandlist = []
while y:
	userlist2 = input("Enter your favorite bands until they enter 'The shows over' ")
	print("The Band entered was: " +str(userlist2))
	if userlist2 == "The shows over":
		print("The input was 'The shows over' ...Exiting...")
		y = False
	else:
		bandlist.append(userlist2)
		continue
	print(" Band list: " , bandlist)

#4	
myfavtuple = ("MK","KISS")

#5

gcounter = 0

bcounter = 0

for x in myfavtuple:
    for y in mylist:
        if x in y:
            gcounter += 1
    for z in bandlist:
        if x in z:
            bcounter += 1

if gcounter >= 1 and bcounter < 1:
    print("Thats a great game")

if gcounter < 1 and bcounter >= 1:
    print("I love that band")

if gcounter >= 1 and bcounter >= 1:
    print("Thats the perfect combo!")

#6

favorite_games_set = {"Legend of Zelda", "God of War", "Super Smash Bros Ultimate"}

#7

print("My favorite games are: ", favorite_games_set)

#8
total_set = list(favorite_games_set) + mylist

#9

print("Our best games in no particular order would be : ", total_set)