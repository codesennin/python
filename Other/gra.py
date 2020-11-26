from typing import List
import math

#########################################################################################

class Equipment:
    name: str
    type: int # 1=weapon; 2=armor; 3=shield
    damage: int
    armor: int

    def __init__(self, name: str, type: int, stat: int):
        self.name = name
        self.type = type
        if type == 1:
            self.damage = stat
            self.armor = 0
        if type in [2, 3]:
           self.damage = 0
           self.armor = stat

#########################################################################################

class Player:
    nickname: str
    level: int
    experience: int
    statistics: List[int] # 0=strength, 1=vitality, 2=agility, 3=intelligence
    equipment: List[Equipment] # 3 slots=> 0=weapon, 1=armor, 2=shield
    backpack: List[Equipment] # 4 slots
    skillpoints: int
    gold: int

    def __init__(self, nickname: str):
        self.nickname = nickname
        self.level = 1
        self.experience = 0
        self.statistics = [10, 10, 10, 10]
        self.equipment = [Equipment("Miecz", 1, 10), Equipment("Zbroja", 2, 15), Equipment("Tarcza", 3, 8)]
        self.backpack = []
        self.skillpoints = 0
        self.gold = 10

    def getPlayerHp(self):
        return self.statistics[1] * 100

    def getPlayerDamage(self):
        return self.statistics[0] * 10 + self.equipment[0].damage

    def addToBackpack(self, item: Equipment):
        if len(self.backpack) != 4:
            self.backpack.append(item)
        else:
            print("Backpack is full.")

    def sellItem(self, slot: int):
        temp = self.backpack[slot]
        self.backpack.pop(slot)
        if temp.type == 1:
            self.gold += temp.damage
        if temp.type in [2, 3]:
            self.gold += temp.armor

    def addSkillPoint(self, stat: int):
        if self.skillpoints > 0:
            self.statistics[stat] += 1
            self.skillpoints -= 1
        else:
            print("You don't have free skillpoints.")

    def buySkillpoint(self, stat: int):
        if self.gold > 10:
            self.statistics[stat] += 1
            self.gold -= 10
        else:
            print("You don't have enough gold.")

#########################################################################################

class Enemy:
    name: str
    level: int
    statistics: List[int]

    def __init__(self, name: str, player: Player, difficulty: int): # 1=easy 2=normal 3=hard
        self.name = name
        self.statistics = []
        if difficulty == 1:
            if player.level == 1:
                self.level = 1
            else:
                self.level = player.level - 1
            for stat in player.statistics:
                self.statistics.append(int(math.floor(stat*0.8)))
        elif difficulty == 2:
            if player.level == 1:
                self.level = 1
            else:
                self.level = player.level
            for stat in player.statistics:
                self.statistics.append(stat)
        elif difficulty == 3:
            self.level = player.level + 1
            for stat in player.statistics:
                self.statistics.append(int(math.floor(stat*1.2)))

    def getEnemyHp(self):
        return self.statistics[1] * 100

    def getEnemyDamage(self):
        return self.statistics[0] * 10

#########################################################################################

def fight(Player, Enemy):
    playerHp = Player.getPlayerHp()
    playerDamage = Player.getPlayerDamage()
    enemyHp = Enemy.getEnemyHp()
    enemyDamage = Enemy.getEnemyDamage()
    print("Player: ", str(playerHp), "HP, Enemy: ", str(enemyHp), "HP", sep="")
    while(playerHp > 0 or enemyHp > 0):
        print("Player is attacking.")
        enemyHp -= playerDamage
        print("Player: ", str(playerHp), "HP, Enemy: ", str(enemyHp), "HP", sep="")
        if enemyHp <= 0:
            print("You won.")
            break
        print("Enemy is attacking.")
        playerHp -= enemyDamage
        print("Player: ", str(playerHp), "HP, Enemy: ", str(enemyHp), "HP", sep="")
        if playerHp <= 0:
            print("You died.")
            break

#########################################################################################
##################################    TEST    SPACE    ##################################
#########################################################################################

gracz = Player("SwirPaleta")
wrog = Enemy("Wilk", gracz, 3)

fight(gracz, wrog)
