#My code so far.

import random #import libraries

#Hero class

class Hero: #Defining class Hero
def __init__(self,name,level,weaponname): #Initializing attributes
self.name = name
self.level = level
self.weaponname = weaponname
self.life = 100
self.damage = 0  

def AttackPoints(self) : #Function for attack
self.attack = random.randrange(0,10)
return self.attack

def imHit(self,dmg): #Function for Remaining life and Damage
self.life = max(self.life - dmg,0)
self.damage = self.damage + dmg
print(self.name,"screams - I'm hit!")
print("Life = ",self.life)

#Villian Class
class Villian(Hero): #Defining class using inherit Hero class
def __init__(self,name,level,weaponname): #Initializing attributes
self.name = name
self.level = level
self.weaponname = weaponname
self.life = 100
self.damage = 0

def FinalForm(self,name): #Define method for Perticular Villian class
print("This isn't even my final form",name,"!")

#Creation of objects

Hero1 = Hero('IronMan',2,"Ak47") #Creation of Hero object
Villian1 = Villian('Thanos',2,"Top")     #Creation of Villian object

#Starting of the game

while(Hero1.life!=0 and Villian1.life!=0): #Start battle between Hero and Villian
Hero1.imHit(Villian1.AttackPoints())
Villian1.imHit(Hero1.AttackPoints())

if(Hero1.life==0): #if Hero died
print(Hero1.name,"is dead")
else: #if Villian died
Villian1.FinalForm(Hero1.name)