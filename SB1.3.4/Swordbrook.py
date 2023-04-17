import random, csv, os, sys, time
import pandas as pd

scriptDirectoryPath = os.path.dirname(__file__)#Finds path to to this file. "Swordbrook(versionNumber).py"
#print(scriptDirectoryPath)#This line is used to verify that the path to the file where the main Swordbrook(versionNumber).py script is has been sourced correctly. Only uncomment for debugging.
sys.path.append(scriptDirectoryPath)#This line adds the swordbrook directory to the system path. this action is cleaned up whenever the program exits properly.

import MonsterModule as Monst
import CharacterModule as Char
import CharacterFileEditingAndIO as FE

def main_menu():
    stillPlaying = True
    menuEntryAttempts = 0
    while ((menuEntryAttempts in range(10)) and stillPlaying == True):
        #print('Pass number ' + str(menuEntryAttempts))#COMMENT ME AFTER DEBUG!
        
        MainState = str(input('Would you like to "play" , "reset" , or "exit" \n'))
        #MainState = MainState.lower() 
        if (MainState.lower() == "play" or MainState.lower() == "p"):
            currentGame = game() #Creates an instance of the class game for use during this session of play and executes it's initialization function.
            currentGame.session()#Calls the "session" function in game which will contain the primary game loop.
            return
        elif (MainState.lower() == "reset" or MainState.lower() == "r"):
            #This code is used to remove the existing save data for already generated characters and allow the game to start as though it was a fresh installation of Swordbrook
            try:
                #print(os.path.abspath(__file__))#COMMENT ME AFTER DEBUG!
                os.remove(scriptDirectoryPath + '/' + 'CharacterFile.csv')
                print('Game reset to orginal installation')
            except:
                print('Game already in initial state')
            menuEntryAttempts += 1
        elif (MainState.lower() == "exit" or MainState.lower() == "e"):
            sys.path.remove(scriptDirectoryPath) #this code removes the path to the main game folder from the system path as a housekeeping measure before exiting.
            exit()
        else:
            #If a user provides and input that is not on the approved list of inputs this code should catch the mistake (User Input Injection prevention to come in later version) 
            print('invalid input please enter "play" , "reset", or "exit"' + '\n \n')
            menuEntryAttempts += 1
    return
 

#==========================================================================================================

class game(object):
    def __init__(self):
        #print("I have entered the game function init")#COMMENT ME AFTER DEBUG!
        
        #print(scriptDirectoryPath)#COMMENT ME AFTER DEBUG!
        self.CharacterFile = (scriptDirectoryPath + '/' + 'CharacterFile.csv')
        #print(self.CharacterFile)#COMMENT ME AFTER DEBUG!
        
        if (os.path.exists(self.CharacterFile) != True):
            print('Welcome to Swordbrook since Its your first time playing let\'s introduce a few things...')
        
            FE.characterFileManager.MakeCharacterFile(self.CharacterFile)
            
            print('a whooooooole bunch more info will go here when there\'s a new game \n')
        #Begin Character Gen portion
        else :
            print('Welcome back to Swordbrook!')
            
        #print('The game file exists now \n')
    
    
    def session(self):
        #Step 1 is to log the user in
        #print("I made it to the session function")#COMMENT ME AFTER DEBUG!
        self.activeCharDF = pd.DataFrame(columns=['NAME','ROWINDEX'])  #This stores a list of the currently logged in users where each name value is linked to a key containing it's index in the userdata dataframe.
        self.login()
        
        #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
        #print(self.activeCharDF.loc[0,'NAME'] + "\n")#COMMENT ME AFTER DEBUG!
        
        FE.characterFileManager.FirstLoginCheck(self)
        Char.Character.PartyBuilder(self)
        
        print("Reaching this point verifies that the entire multicharacter login and verificaiton process is working and that character data is being correctly populated into the CSV file acting as a local database for game info. The next step will be to copy the character making code into the Monster Module to automatically generate monster and then link the combat part of the code back to the login part.")
        
        
    def login(self):
        #self.activeCharDF = activeCharDF
        #print("I made it to the login function")#COMMENT ME AFTER DEBUG!
        
        self.df = pd.read_csv(self.CharacterFile) #This line creates the dataframe that will be used to read and manage the data in the character file.
        self.currentName = (str(input("What is your characters name?" + "\n")))
        FE.characterFileManager.NameInputValidation(self, self.currentName)
        self.currentNameIndex = []      
        
        ############added Space for debug################
        # print(self.currentName)
        # print(self.CharacterFile)
        # doesCurrentNameExist = FE.characterFileManager.DoesCharExist(self, self.currentName,self.CharacterFile)
        # print(doesCurrentNameExist)
        ##################################################
        
        #try:
        if(self.currentName == ''):
            nullNameLoop=0
            while(nullNameLoop in range(10) and self.currentName == ''):
                remainingItters = str(10 - nullNameLoop)
                print("No input recieved. Character name cannot but null. " + remainingItters + " attempts remaining")  
                self.currentName = (str(input("Please enter your characters name " + "\n"))).lower()
                nullNameLoop += 1 
                if (nullNameLoop == 10):
                    print ("Too many empty values entered. 0 attempts remaining.")
                    time.sleep(1)
                    print("shutting down...")
                    time.sleep(2)
                    exit()

        doesCurrentNameExist = FE.characterFileManager.DoesCharExist(self,self.currentName,self.CharacterFile)
        if doesCurrentNameExist == True:
            #print("I think the name exists!")#COMMENT ME AFTER DEBUG!
            #print (self.currentNameIndex) #COMMENT ME AFTER DEBUG!
            print ('\nplayer data found! one moment...')
            indexOfCharacterName = self.df.index[self.df['Name'] == self.currentName].tolist()
            #print(len(self.activeCharDF))#COMMENT ME AFTER DEBUG!
            #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
            self.activeCharDF.loc[len(self.activeCharDF)] = [self.currentName,indexOfCharacterName]
            
            print (self.df.iloc[self.currentNameIndex])
            print ("\n\n")
        elif doesCurrentNameExist == False:
            #print("I think the name does not exist!")#COMMENT ME AFTER DEBUG!
            self.makingACharacter = True #This variable and it's corresponding use in the following while loop could be removed and replaced with lines that set loop=10 for greater effeciency but this format provides more readable code.
            newLoginLoop = 0
            while ((newLoginLoop in range(10)) and self.makingACharacter == True):
                inputval = input ('No such character found.\nWould you like to register a new character with this name? yes/no\n').lower()
                if(inputval == 'y' or inputval == 'yes'):
                    Char.Character.makeNewCharacter(self, self.currentName)
                    #print("Called make character function")#COMMENT ME AFTER DEBUG!
                    
                elif(inputval == 'n' or inputval == 'no'):
                    print ('Returning to main menu.')
                    self.makingACharacter = False
                    return
                else:
                    print ('invalid input')
                    newLoginLoop += 1
        return()
        # except:
            # print ('File IO error detected. Potential Malicious input entry. Exiting...')
            # time.sleep(1)
            # print ('3')
            # time.sleep(1)
            # print('2')
            # time.sleep(1)
            # print ('1')
            # time.sleep(1)
            # exit()
            
        
    # def prettyPrint(txtFileName): deprecated for now
        # printFilePath = (scriptDirectoryPath + '/' + txtFileName)
        # with open(printFilePath, 'r') as printFile:
            # for char in printFile:
                # sys.stdout.write(char)
                # sys.stdout.flush()
                # time.sleep(4.0)

        





 
#========================================================================================================== 
 
def main():
    #Kept for maybe intro bit #game.prettyPrint('SwordbrookStoryIntro.rtf')
    main_menu()
    
    
if __name__ == "__main__":
    main()