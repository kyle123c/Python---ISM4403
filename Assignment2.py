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
	userlist2 = input("Enter your favorite bands until they enter 'The show is over' ")
	print("The Band entered was: " +str(userlist2))
	if userlist2 == "The show is over":
		print("The input was 'The show is over' ...Exiting...")
		y = False
	else:
		bandlist.append(userlist2)
		continue
	gametuple = ("MK",)			
	bandtuple = ("Kiss",)
	gamebandtuple = gametuple + bandtuple
	print(gamebandtuple)					#4
	'''
		for x in mylist:
		if x in gametuple:
			print("That is a great a game")
		if x in bandtuple:
			print("Thats is my favorite band!")
		if x in mylist + bandlist:
			print("That is the perfect combination!")	


'''

