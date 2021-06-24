#My code so far.

import random #import libraries

#Hero class

class Hero: #Defining class Hero
	def __init__(self,name,level,weaponname,life,damage,attack):
		self.name = name
		self.level = level
		self.weaponname = weaponname
		self.life = 100
		self.damage = damage
		self.attack = 0

#Function for attack
def AttackPoints(self):
	self.attack = random.randrange(0,10)
	return self.attack

#Function for Remaining life and Damage
def imHit(self,hit):
	self.life = max(self.life - hit,0)
	self.damage = self.damage + str(hit)
	print(self.name,"Screams - I'm hit!")
	print("Life = ",self.life)

#Villian Class | Defining class using inherit Hero class
class Villian(Hero):
	def __init__(self,name,level,weaponname,life,damage,attack):
		self.name = name
		self.level = level
		self.weaponname = weaponname
		self.life = 100
		self.damage = damage
		self.attack = 0

def FinalForm(self,name): #Define method for Perticular Villian class
	print("This isn't even my final form",name,"!")

#Creation of objects

Hero1 = Hero('Goku','50','Kamahameha!', 100,'0', '0') #Creation of Hero object
Villian1 = Villian('Frieza','50','Death Beam!',100,'0','0')#Creation of Villian object

#Starting of the game
#Start battle between Hero and Villian

while True:
	Hero1.imHit(Villian1.AttackPoints())
	Villian1.imHit(Hero1.AttackPoints())

	if(Hero1.life==0):
		print(Hero1.name,"is dead")
		break

	if Villian1.life==0:
		Villian1.FinalForm(Hero1.name)
		break





	'''
	while(Hero1.life!=0 and Villian1.life!=0):
	Hero1.imHit(Villian1.AttackPoints())
	Villian1.imHit(Hero1.AttackPoints())

	if(Hero1.life==0):
		print(Hero1.name,"is dead")

else:
	Villian1.FinalForm(Hero1.name)
	'''