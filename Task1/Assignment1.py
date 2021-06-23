'''
1.	Create a variable and assign your favorite movie to it. Print this value out to the screen. 
2.	Create a variable and assign it the number of times you have seen your favorite movie. Print this value out to the screen. 
3.	Display the datatype of each of the previous variables.
4.	Print to the screen the name of the movie and the number of times watched in one line using concatenation and casting.
5.	Check to see if the number of times watched is greater than 10 and display a message stating that you are a true fan (use your own verbiage).
6.	Prompt the user to input a movie they like and store this in a new variable. Print this value out to the screen. 
7.	Prompt the user to input the number of times they watched the movie they entered and store this in a new variable. Print this value out to the screen. 
8.	If they watched the movie less than 5 times, print a message stating that they seemed to like the movie, but they aren’t a hardcore fan (use your own verbiage). If they watched the movie more than 5 times, but less then 10, print a message saying that they are almost an “ultra fan” (use your own verbiage). If they watched the movie more than 10 times, print out a message that they are the “ultimate fan” (use your own verbiage). 
9.	Add the number of times you watched your favorite movie to the number of times the user watched their favorite movie and output the number to the screen with an appropriate message of the total number of times you both watched your favorite movies. 
10.	If the user has watched their favorite movie more than your favorite movie, output a message stating that they are winning. If the inverse is true then output a message stating that you are winning. If they are equal, then output an appropriate message. 
'''
# Number 1
var1 = "The Wolf of Wallstreet"
print(var1)

# Number 2
var2 = 69
print(var2)


# Number 3
print(type(var1))
print(type(var2))

# Number 4
print("I've watched", var1 , var2, "times")

# Number 5 
x = 10  
if x < var2:
	print ("I'm a true fan boiiiiii!!!")

# Number 6
user_input = input("Whats your favorite movie?")
print("The movie entered is: " + user_input)

# Number 7
user_input2 = input("How many times have you watched your favorite movie?")
print("The number of times is : " + user_input2)

# Number 8
if int(user_input2) < 5:
	print("You seemed to like the movie, but your not a hardcore fan ")
elif 10 > int(user_input2) > 5:
	print("Your almost an ultra fan! ")
else: 
	print("Your the Ultimate Fan")	
	print (user_input2)	

# Number 9
usermovie = int(input("Soooo how many times you watched this movie again?: "))
var3 = var2 + usermovie 
print ("We both watched a total of: " , var3)

# Number 10
if int(usermovie) > var2:
	print ("The user has won")
elif int(usermovie) < var2:
	print ("I'm Winning")
else:
	print ("Its a Draw")	
