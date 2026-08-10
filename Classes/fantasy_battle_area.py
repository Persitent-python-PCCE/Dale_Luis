import random as r

class Character:
    def __init__(self, name, health,attack,defense,speed):
        self.name=name
        self.health=health
        self.attack=attack
        self.defense=defense
        self.speed=speed

    def take_damage(self,amount):
        dmg=max(1,amount-self.defense)
        self.health-=dmg
        if not target.is_alive():
            print(f"{target.name} is defeated!")
        return dmg
    
    def is_alive(self):
        return self.health>0
    
    def attacks(self,target):
        raw=self.attack
        target.take_damage(raw)

class Warrior(Character):
    def __init__(self, name, health, attack, defense, speed):
        self.rage=0
        self.hlth=health
        super().__init__(name, health, attack, defense, speed)
        
        
    def attacks(self,target):
        if(self.hlth!=self.health):
            self.rage+=1
            self.hlth=self.health
            if self.rage==5:
                rage_atk=self.attack+self.rage
                print(f"{self.name} (Warrior) uses rage! Deals {rage_atk} damage.")
                target.take_damage(rage_atk)
        elif self.health<(self.health*0.30):
            berserk=self.attack*2
            print(f"{self.name} (Warrior) enters Beserk Mode! Attack power increased")
            print(f"{self.name} (Warrior) strikes with double power! Deals {berserk} damage.")
            target.take_damage(berserk)
        else:
                print(f"{self.name} (Warrior) swings sword! Deals {self.attack} damage.")
                target.take_damage(self.attack)
    
class Mage(Character):
    def __init__(self, name, health, attack, defense, speed):
        self.mana=100
        super().__init__(name, health, attack, defense, speed)
        
    def attacks(self,target):
        if self.mana>40:
            mana_atk=self.attack*1.5
            self.mana-=40
            self.health-=8
            print(f"{self.name} (Mage) casts Fireball! Deals {mana_atk} damage but loses 8 health.")
            target.take_damage(mana_atk)
        else:
            print(f"{self.name} (Mage) swings his staff! Deals {self.attack-17} damage.")
            target.take_damage(self.attack-17)
    
class Archer(Character):
    def __init__(self, name, health, attack, defense, speed):
        self.critical_chance=0.30
        super().__init__(name, health, attack, defense, speed)
        
    def attacks(self,target):
        ran=r.random()
        if ran<self.critical_chance:
            crit_dmg=self.attack*2
            print(f"{self.name} (Archer) lands a Critical Hit! Deals {crit_dmg} damage.")
            target.take_damage(crit_dmg)
        else:
            print(f"{self.name} (Archer) shoots an arrow! Deals {self.attack} damage.")
            target.take_damage(self.attack)

Thor = Warrior("Warrior",130,22,12,6)
Gandalf=Mage("Mage",90,30,5,8)
Alex=Archer("Archer",100,24,7,12)

fighters = [Thor, Gandalf, Alex]

while sum(f.is_alive() for f in fighters) > 1:
    
    fighters.sort(key=lambda f: f.speed, reverse=True)

    for fighter in fighters:
        
        if not fighter.is_alive():
            continue

        targets = [f for f in fighters if f != fighter and f.is_alive()]

        if not targets:
            break
        
        target = r.choice(targets)
        fighter.attacks(target)
        
        if sum(f.is_alive() for f in fighters) == 1:
            break

winner = [f for f in fighters if f.is_alive()][0]

print(f"{winner.name} wins the battle!")