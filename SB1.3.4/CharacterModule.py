#---------------------------------------------------This section is for importing existing python modules----------------------------------------------------------#
import time
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------This section find and storing the current location of the program so that it can reference other files & modules in it's directory-----------------#
from Swordbrook import game
import MonsterModule as Monst
import CharacterFileEditingAndIO as FE
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------------This section defines the mechanics for the main menu. It is called first before the game instance method is called---------------------------#
class Character(game):
    
#---#This block contains a currently unneeded
    # |#def __init__():#(self, name, health, attack, defense):
    # |    #self.name = name
    # |    #self.health = health
    # |    #self.attack = attack
    # |    #self.defense = defense
    # |
    # |#def __str__(self):
    # |#    return(f'{self.name} - Health: {self.health} | Attack: {self.attack} | Defense: {self.defense}')

    def makeNewCharacter(self, characterName):
        makeNewCharacterloop = 0
        
        while ((makeNewCharacterloop in range(10)) and self.makingACharacter == True):
            print ("New character's name will be: " + characterName + "\n")
            time.sleep(2)
            userResponse1 = (str(input("Is this name alright? yes/no or \"back\" to return to previous step." + "\n"))).lower()
            
            if (userResponse1 == 'y' or userResponse1 == 'yes'):
                print("Making a New Character!")
                newDataRowEntry = [characterName,'0','0','0']
                self.df.loc[len(self.df)] = newDataRowEntry
                FE.characterFileManager.Write(self,self.df,self.CharacterFile)
                indexOfCharacterName = self.df.index[self.df['Name'] == characterName].tolist()
                self.activeCharDF.loc[len(self.activeCharDF)] = [characterName,indexOfCharacterName]
                #print(indexOfCharacterName)!")#COMMENT ME AFTER DEBUG!
                #print(self.activeCharDF)!")#COMMENT ME AFTER DEBUG!
                self.makingACharacter = False
                return
            
            elif (userResponse1 == 'n' or userResponse1 == 'no'):
                nameAltering = True
                nameAlteringLoop = 0
                
                while ((nameAlteringLoop in range(10)) and nameAltering == True):
                    userResponse2 = (str(input("Please input new character name or \"back\"." + "\n"))) 
                    FE.characterFileManager.NameInputValidation(self, userResponse2)
                    
                    if(userResponse2 == 'b' or userResponse2 == 'back'):
                        nameAltering = False
                        self.makingACharacter = False
                    
                    elif(userResponse2 == ''):
                        nullNameLoop=0
                        while(nullNameLoop in range(10) and userResponse2 == ''):
                            remainingItters = str(10 - nullNameLoop)
                            print("No input recieved. Character name cannot but null. " + remainingItters + " attempts remaining")  
                            self.currentName = (str(input("Please enter your characters name " + "\n"))).lower()
                            nullNameLoop += 1 
                            if (nullNameLoop == 10):
                                print ("Too many empty values entered. 0 attempts remaining.")
                                time.sleep(1)
                                print("Exiting game... Please play again!")
                                time.sleep(2)
                                exit()
                    
                    else:
                        doesCurrentNameExist = FE.characterFileManager.DoesCharExist(self,userResponse2,self.CharacterFile)
                        
                        if doesCurrentNameExist == True:
                            print("Charcter already Exists. Please choose a different name.")
                            nameAlteringLoop += 1
                        
                        elif doesCurrentNameExist == False:
                            #print("Test flag for making a new character")#COMMENT ME AFTER DEBUG! 
                            Character.makeNewCharacter(self, userResponse2)
                            return
                    
                self.makingACharacter = False
            
            elif (userResponse1 == 'b' or userResponse1 == 'back'):
                self.makingACharacter = False

            else:
                print("\nInvalid response! Please answer with \"yes\" or \"no\". Resuming...\n\n")
        
        if(makeNewCharacterloop == 10):#This if is used to set the flag that takes us back to the main menu in the event that all entries were invalid without running the code each time an invalid entry is entered.
            self.makingACharacter = False
        print("Returning to Main Menu.")
        return

    def PartyBuilder(self):
        self.buildingPartyCounter = 0
        for self.buildingPartyCounter in range(50):
            print ("\nthere are " + str(len(self.activeCharDF)) + " characters logged in out of a maximum of 20\n")
            #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
            self.tempPrintList =(self.activeCharDF['NAME'].tolist())
            print("The currently logged in users are", *self.tempPrintList, sep =', ')
            #print(str(len(self.activeCharDF)))#COMMENT ME AFTER DEBUG!
            #print(len(self.tempPrintList))#COMMENT ME AFTER DEBUG!
            #print (*self.tempPrintList, sep =', ')#COMMENT ME AFTER DEBUG!
            if (str(len(self.activeCharDF)) == 20):
                print("The party is full! Begining game.")
                return
            userResponse1 = (str(input("\n\nWould you like to login another character for your adventuring party? yes/no." + "\n"))).lower()
            if (userResponse1 == 'y' or userResponse1 == 'yes'):
                self.login()
            elif (userResponse1 == 'n' or userResponse1 == 'no'):
                return
            else:
                print("please answer with \"yes\" or \"no\"")
                self.buildingPartyCounter += 1
        print("Too many invalid input entries. Shutting down...")
        exit()        
                






    def attack_monster(self, monster):
        damage = self.attack - monster.defense
        if damage < 0:
            damage = 0
        monster.health -= damage
        print(f'{self.name} attacks {monster.name} for {damage} damage!')

    def defend(self):
        self.defense += 5
        print(f'{self.name} defends and raises their defense by 5!')


class Wizard(Character):
    def __init__(self, name):
        super().__init__(name, 75, 15, 5)
     
    def cast_spell(self, monster):
        spell_power = random.randint(10, 20)
        monster.health -= spell_power
        print(f'{self.name} casts a spell for {spell_power} damage!')


class Fighter(Character):
    def __init__(self, name):
    
        super().__init__(name, 100, 20, 10)
    
    def rage(self):
        self.attack += 5
        print(f'{self.name} goes into a rage and increases their attack by 5!')


class Archer(Character):
    def __init__(self, name):
        super().__init__(name, 80, 15, 5)

    def shoot_arrow(self, monster):
        arrow_power = random.randint(10, 20)
        monster.health -= arrow_power
        print(f'{self.name} shoots an arrow for {arrow_power} damage!')