#Adventure Game
#User name is called RECRUIT ZERO -- Recruit Zero(user) goal is to become a Silver Soldier
#recruit will collect gold coins and the resource is their power points
#User will fail game  if power points are below -25 even if they get to level 10

import random


class Adventure:
    def __init__(self, recruit, goldCoins, powerUpPoints):
        self.recruit = recruit
        self.pos = 0
        self.goldCoins =  goldCoins 
        self.powerUpPoints = powerUpPoints
   
    def __str__(self):
        #ent = enter key 
        ent = "----------------------------------------------------\n"
        ent = ent + "Level: " + str(self.pos) + "\n"
        ent = ent + "Golden Coins: " + str(self.goldCoins) + "\n"
        ent = ent + "Power Points: " + str(self.powerUpPoints) + "\n"
        return ent


class Enemy:
    def __init__(self, name, pos, enemyIntro, enemyAttack):
        self.name = name
        self.pos = pos
        self.enemyIntro = enemyIntro
        self.enemyAttack = enemyAttack
    

#adventure game main loop 
def playGame(recruit, gameEnemy, posLength):
    print("\nSTART GAME")
    for i in range(1, posLength+1): 
        input("\nPress <ENTER> to walk forward.\n") 
        #Press <ENTER> to have RECRUIT ZERO move forward
        recruit.pos = i 
        print("RECRUIT ZERO you are at LEVEL " + str(recruit.pos))
        for enemy in gameEnemy:
            if recruit.pos == enemy.pos: 
                recruit.powerUpPoints -= enemy.enemyAttack 
                print("You got attacked by " + enemy.name + " and lost " + str(enemy.enemyAttack) + " " + " power points!")
                break
        else: 
            collect = random.randint(10, 60)
            recruit.goldCoins = recruit.goldCoins + collect
            print("The gods have given you " + str(collect) + " " + "Golden Coins!")
        # If the recruit has failed its mission
        if recruit.powerUpPoints <= -25: 
            print("\nYour enemies have severely weakened you! You have failed your goal ")
            print("of becoming a Silver Soldier.")
            break
    else:
        print("\nYou have completed the mission successfully!")
        print("RECRUIT ZERO, welcome to the League of the Silver Soldiers!")
        

#enemy name list and introduction list
enemyList = ["Prince Evil Eye", "Vampire Bats!", "Mistress Khan"]
enemyIntroList = [" the Prince of darkness will attempt to destroy you!",
                  " These black flying creatures will not make your journey easy.",
                  " her hypnotic eyes will steal your power if your gaze is too long."]


def GameIntro():
    print("Somewhere on a planet far far away in the Galaxy of the Unknown....")
    input("Press <Enter> to continue.\n")
    print("Welcome to the Vorex Training grounds RECRUIT ZERO! I am the Grand Commander and")
    print("I will be your guide for today's event.")
    input("Press <Enter> to continue.\n")
    print("It is your goal RECRUIT ZERO to reach LEVEL 12 to become a")
    print("Silver Soldier, but to reach this goal you must " )
    print("first complete this task that will test your strength and mental toughness.")
    print("You may find a gift along the way; a blessing from the gods but, don't forget")
    print("about the danger that lurks in the shadows.")
    print("Your POWER can't get to a negative 25 or below!")
    print("Your MISSION awaits you...\n")
    input("Press <Enter> to continue\n")
    
    print('BEFORE YOU GO!\n')
    print('Let me warn you of the things that lurk in the shadows:')
    print(enemyList[0] + enemyIntroList[0])
    print(enemyList[1] + enemyIntroList[1])
    print(enemyList[2] + enemyIntroList[2])
    input("Press <Enter> to continue\n")
    

def main():
    GameIntro()
    posLength = 10
    recruit = Adventure("RECRUIT ZERO", 0, 100)
    #30%-60% chance of enemies 
    nEnemy = random.randint(int(0.3 * posLength), int(0.6 * posLength)) 
    
    gameEnemy = []
    
    for i in range(nEnemy):
        eName, eIntro = random.choice(enemyList), random.choice(enemyIntroList)
        ePos, eAttack = random.randint(1, posLength), random.randint(20, 60)
        gameEnemy.append(Enemy(eName, ePos, eIntro, eAttack))
    
    #play game and print final results 
    playGame(recruit, gameEnemy, posLength) 
    print("\n\nYour Final Results:") 
    print(recruit)
 

if __name__ == '__main__':
    main()
