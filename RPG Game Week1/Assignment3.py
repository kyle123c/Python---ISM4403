import random 

# Hero class | attributes
class Hero:
    def __init__(self, name, level, weaponname, life, damage, attack):  # Initializing attributes
        self.name = name
        self.level = level
        self.weaponname = weaponname
        self.life = 100
        self.damage = 0
        self.attack=0

    def AttackPoints(self):  # Function for attack
        self.attack = random.randrange(1, 40)
        return self.attack

    def imHit(self, hit):  # Function for Remaining life and Damage
        self.life = max(self.life - hit, 0)
        self.damage = self.damage + hit
        print(self.name, "Screams - I'm hit!")
        print("Life = ", self.life)


# Villian Class
class Villian(Hero):  # Defining class using inherit Hero class
    def __init__(self, name, level, weaponname, life, damage, attack):  # Initializing attributes
        super().__init__(name,level,weaponname, life, damage, attack)

    def FinalForm(self, name):  # Define method for Particular Villian class
        print("This isn't even my final form", name, "!")


# Starting of the game
battle_number = 0
hero_wins=0
villain_wins=0

# Creation of objects
while True:
    Hero1 = Hero('Goku',50,'Kamahameha!',100,'0','0')  # Creation of Hero object
    Villian1 = Villian('Frieza',55,'Death Beam!',100,'0','0')  # Creation of Villian object
   
    round_number = 0
    battle_number += 1
    total_damage=[]
    hero_attack_val=[]
    villan_attack_val=[]
    
    while Hero1.life != 0 and Villian1.life != 0:  # Start battle between Hero and Villian
        round_number += 1
        
        # user chooses how to proceed
        print("ROUND : ", round_number)
        print("Who will attack?")
        print("1.", Hero1.name)
        print("2.", Villian1.name)
        print("choice : ", end=" ")
        choice: int = int(input())
        print("")
        
        if choice == 2:
            Hero1.imHit(Villian1.AttackPoints())
            total_damage.append(Villian1.attack)
        elif choice == 1:
            Villian1.imHit(Hero1.AttackPoints())
            total_damage.append(Hero1.attack)
        else:
            print("WRONG CHOICE! TRY AGAIN!!\n")
        hero_attack_val.append(Hero1.attack)
        villan_attack_val.append(Villian1.attack)

    if Hero1.life == 0:  # if Hero died
        print(Hero1.name, "is dead")
        villain_wins+=1
    else:  # if Villian died
        Villian1.FinalForm(Hero1.name)
        hero_wins+=1