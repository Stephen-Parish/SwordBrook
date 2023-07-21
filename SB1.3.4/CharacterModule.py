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
    
#---#This block contains a currently unneeded init function for the Character class. May be re-enabled if valueable later.-----------------------------------------#
    # |#def __init__():#(self, name, health, attack, defense):
    # |    #self.name = name
    # |    #self.health = health
    # |    #self.attack = attack
    # |    #self.defense = defense
    # |
    # |#def __str__(self):
    # |#    return(f'{self.name} - Health: {self.health} | Attack: {self.attack} | Defense: {self.defense}')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
    
#--------------------------This function is used for defining a new character. including populating it's verious stats in the characterFile.csv--------------------#
    def MakeNewCharacter(self, characterName):
    
        MakeNewCharacterloop = 0 #initializing a counter variable to 0
        
        while ((MakeNewCharacterloop in range(10)) and self.makingACharacter == True): #Give player 10 chances to correctly move through the character creation options or return to the main menu
            self.Printer.Clean()
            self.Printer.PrettyPrintString("New character's name will be: " + characterName + "\n",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
            time.sleep(1)
            self.Printer.PrettyPrintString("Is this name alright? yes/no or \"back\" to return to previous step.",'fastNoLag',clearScreen = False,allLeftJustifiedText = True,isArtOnly = False)
            userResponse1 = (str(input("\n"))).lower() #This line gives the player an oportunity to confirm that the character name they have entered is correct before it is added to the game.
            
            if (userResponse1 == 'y' or userResponse1 == 'yes'): #If the player answers yes then this code will write a new line to the character file containing that name with fields for the various charachter stats
                self.Printer.PrettyPrintString("Making a New Character!",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                newDataRowEntry = [characterName,'0','0','0']
                self.df.loc[len(self.df)] = newDataRowEntry #appends row containing new character template to last row of dataframe
                #indexOfCharacterName = self.df.index[self.df['Name'] == characterName] #writes the index of the row containing the data for the new character to a variable
                indexOfCharacterName = int(self.df[self.df['Name']==characterName].index.values) #writes the index of the row containing the data for the new character to a variable
                self.activeCharDF.loc[len(self.activeCharDF)] = [characterName,indexOfCharacterName] #Adds character to list of actively logged in characters
                #print(indexOfCharacterName)#COMMENT ME AFTER DEBUG!
                #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
                self.makingACharacter = False #ends character making loop

######################################################################################################Tempt work frame begin            
                Character.PickCharacterArchetype(self, characterName, indexOfCharacterName)
                
                
                
                
                
                
                
                
                
                
                
                
                FE.characterFileManager.Write(self,self.df,self.CharacterFile) #calles function to write the character info dataframe to the CharacterFile.csv
######################################################################################################Temp work frame End
                return
            
            elif (userResponse1 == 'n' or userResponse1 == 'no'): # If the player answers no then they are given 10 chances to either provide a different name for the new character or return to the main menu 
                nameAltering = True
                nameAlteringLoop = 0 #initializing a counter variable to 0
                
                while ((nameAlteringLoop in range(10)) and nameAltering == True): #loop so that players attempts at making new character are limited to 10. This prevents the program infinetely looping if endless invalid attempts are made.
                    self.Printer.PrettyPrintString("Please input new character name or \"back\".",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                    userResponse2 = (str(input("\n"))) 
                    FE.characterFileManager.NameInputValidation(self, userResponse2)
                    
                    if(userResponse2 == 'b' or userResponse2 == 'back'): #returns to previous step 
                        nameAltering = False
                        self.makingACharacter = False
                    
                    elif(userResponse2 == ''): #handles emtpy input entries for userResponse2
                        nullNameLoop=0
                        
                        while(nullNameLoop in range(10) and userResponse2 == ''):
                            remainingItters = str(10 - nullNameLoop)
                            self.Printer.PrettyPrintString("No input recieved. Character name cannot but null. " + remainingItters + " attempts remaining",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                            self.Printer.PrettyPrintString("Please enter your characters name ",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                            self.currentName = (str(input("\n"))).lower()
                            nullNameLoop += 1 
                            
                            if (nullNameLoop == 10):
                                self.Printer.Clean()
                                self.Printer.PrettyPrintString("Too many empty values entered. 0 attempts remaining.",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                                time.sleep(1)
                                self.Printer.PrettyPrintString("Exiting game... Please play again!",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False) 
                                time.sleep(2)
                                exit()
                    
                    else:
                        doesCurrentNameExist = FE.characterFileManager.DoesCharExist(self,userResponse2,self.CharacterFile) #call function for File Editing Module to see if the newly entered name already exists in the character database(CharacterFile.csv)
                        
                        if doesCurrentNameExist == True: #if character name is already in use game warns character and resumes character entry loop
                            self.Printer.PrettyPrintString("Charcter already Exists. Please choose a different name.",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                            nameAlteringLoop += 1
                        
                        elif doesCurrentNameExist == False: #If character name is not already in use then MakeNewCharacter function from this class is recursively called to create a new character with that name
                            #print("Test flag for making a new character")#COMMENT ME AFTER DEBUG! 
                            Character.MakeNewCharacter(self, userResponse2)
                            return
                    
                self.makingACharacter = False
            
            elif (userResponse1 == 'b' or userResponse1 == 'back'): #returns to previous step if use selects "back"
                self.makingACharacter = False
            else:
                self.Printer.PrettyPrintString("\nInvalid response! Please answer with \"yes\" or \"no\". Resuming...\n\n",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False) #case for handling all invalid responses. Returns to top of loop
                MakeNewCharacterloop += 1

                
        #--------------------------------------------------------------------------No longer used------------------------------------------------------------------#
        #if(MakeNewCharacterloop == 10):#This case is used to set the flag that takes us back to the main menu in the event that all entries were invalid without running the code each time an invalid entry is entered
        #    self.makingACharacter = False
        #----------------------------------------------------------------------------------------------------------------------------------------------------------#
        
        print("Returning to Main Menu.")
        return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------This functino allows multiple characters to be to loggin simulatniously. This creates a "party" of adventurers for the turnbased combat-----------------#
    def PartyBuilder(self):
        self.buildingPartyCounter = 0
        
        for self.buildingPartyCounter in range(100): #allows user 100 total chances for logging in new characters before returning to main menu
            self.tempPrintString = ""
            self.tempPrintList = []
            self.Printer.Clean()
            
            self.Printer.PrettyPrintString("\nthere are " + str(len(self.activeCharDF)) + " characters logged in out of a maximum of 20\n",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False) #displays number of currently logged in characters
            #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
            self.tempPrintList =(self.activeCharDF['NAME'].tolist())
            #self.tempPrintList.pop(0) #Remove the 0th element from the list because it contains only the name of the column in the dataframe and not an actual character Name Value
            for temporaryIteratorIndexVar in range(len(self.tempPrintList)):
                if (temporaryIteratorIndexVar == len(self.tempPrintList)-1):
                    self.tempPrintString += str(self.tempPrintList[temporaryIteratorIndexVar] + ".")
                else:
                    self.tempPrintString += str(self.tempPrintList[temporaryIteratorIndexVar] + ", ")
                    
            self.Printer.PrettyPrintString("The currently logged in users are:" + self.tempPrintString,'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
            #print("The currently logged in users are", *self.tempPrintList, sep =', ') #Displays list of all currently logged in characters seperated by commas #This is the old method before converting to string so that I could use PrettyPrintString
            #print(str(len(self.activeCharDF)))#COMMENT ME AFTER DEBUG!
            #print(len(self.tempPrintList))#COMMENT ME AFTER DEBUG!
            #print (*self.tempPrintList, sep =', ')#COMMENT ME AFTER DEBUG!
            if (str(len(self.activeCharDF)) == 20): #Tracks the number of currently logged in character so that there can be no more than a maximum of twenty
                self.Printer.PrettyPrintString("The party is full! Begining game..." + self.tempPrintString,'slow',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                return
            
            
            self.Printer.PrettyPrintString("\n\nWould you like to login another character for your adventuring party? yes/no\n",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
            userResponse1 = (str(input("\n"))).lower()
            if (userResponse1 == 'y' or userResponse1 == 'yes'): #Calls login function from game class in main program to login additional characters if player responds yes
                self.login()
            elif (userResponse1 == 'n' or userResponse1 == 'no'): #returns from function to begin game if user is done adding characters to party
                print("Party selected! Begining game.")
                return
            else:
                print("\n\n\nIncorrect input. Please answer with \"yes\" or \"no\"")
                self.buildingPartyCounter += 1
        print("Too many invalid input entries. Returning to main menu...")
        return        
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#



    def PickCharacterArchetype(self, CName, CIndex):
        print("I made it to the class picker!")
        pickingClass = True
        counter = 0
        self.Printer.PrettyPrintString("Please select a class from \"Wizard\", \"Swordsman\", \"Archer\" \"Knight\"",'fast',clearScreen = False,allLeftJustifiedText = True,isArtOnly = False)
        self.chosenClass = (str(input("\n")))
        self.chosenClass = self.chosenClass.lower()
        FE.characterFileManager.InputValidation(self, self.currentName,"Please select a class from \"Wizard\", \"Swordsman\", \"Archer\" \"Knight\"")
        
        while counter in range(10) and pickingClass == True:
            #print(CIndex)
            #print(self.df)
            #print(self.df.iloc[0])
            #print(self.df.iloc[CIndex])
            #dataFrameData = self.df[self.df['Name']==CName]
            #print(dataFrameData)
            # = self.df[self.df['NAME']==CName]['COUNTRY']
            #print(self.df.index[self.df['Name']])
            #print(self.df.index[self.df['Name'] == characterName])
            
            
            if (self.chosenClass == 'w' or self.chosenClass == 'wizard'): #Calls login function from game class in main program to login additional characters if player responds yes
                self.df.at[CIndex,'Class'] = 'Wizard'
                self.df.at[CIndex,'HP'] = 'WizHP'
                self.df.at[CIndex,'AP'] = 'Wizard'
                temptFillIn = (str(input("Respond1")))
                return
            elif (self.chosenClass == 's' or self.chosenClass == 'swordsman'): #returns from function to begin game if user is done adding characters to party
                self.df.at[CIndex,'Class'] = 'Swordsman'
                self.df.at[CIndex,'HP'] = 'SwordHP'
                self.df.at[CIndex,'AP'] = 'SwordAP'
                pickingClass = False
                return
            elif (self.chosenClass == 'a' or self.chosenClass == 'archer'): #returns from function to begin game if user is done adding characters to party
                self.df.at[CIndex,'Class'] = 'Archer'
                self.df.at[CIndex,'HP'] = 'ArchHP'
                self.df.at[CIndex,'AP'] = 'ArchAP'
                pickingClass = False
                return
            elif (self.chosenClass == 'k' or self.chosenClass == 'knight'): #returns from function to begin game if user is done adding characters to party
                self.df.at[CIndex,'Class'] = 'Knight'
                self.df.at[CIndex,'HP'] = 'KHP'
                self.df.at[CIndex,'AP'] = 'KAP'
                pickingClass = False
                return
            elif (self.chosenClass == 'b' or self.chosenClass == 'back'): #returns from function to begin game if user is done adding characters to party
                self.df.at[CIndex,'Class'] = 'Wizard'
                self.df.at[CIndex,'HP'] = 'WizHP'
                self.df.at[CIndex,'AP'] = 'Wizard'
                pickingClass = False
                return
            else:
                self.Printer.Clean()
                self.Printer.PrettyPrintString("\n\nInvalid input!",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                self.Printer.PrettyPrintString("Please select a class from \"Wizard\", \"Swordsman\", \"Archer\" \"Knight\"",'fast',clearScreen = False,allLeftJustifiedText = True,isArtOnly = False)
                self.chosenClass = (str(input("\n")))
                counter += 1
        print("Too many invalid input entries. Returning to main menu...")
        return        

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