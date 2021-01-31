
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
