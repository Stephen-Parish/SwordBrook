#---------------------------------------------------This section is for importing existing python modules----------------------------------------------------------#
import random, csv, os, sys, time
import pandas as pd
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#---------------This section find and storing the current location of the program so that it can reference other files & modules in it's directory-----------------#
scriptDirectoryPath = os.path.dirname(__file__)#Finds path to to this file. "Swordbrook(versionNumber).py"
#print(scriptDirectoryPath)#This line is used to verify that the path to the file where the main Swordbrook(versionNumber).py script is has been sourced correctly. Only uncomment for debugging.
sys.path.append(scriptDirectoryPath)#This line adds the swordbrook directory to the system path. this action is cleaned up whenever the program exits properly.
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------This section is for importing custom modules made for this program--------------------------------------------------#
import MonsterModule as Monst
import CharacterModule as Char
import CharacterFileEditingAndIO as FE
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#--------------------------------------This section is for importing text files containing game information and diolouge-------------------------------------------#
NameFile = ((os.path.dirname(__file__))+ '/' + 'NameFile.csv')
SBStory = ((os.path.dirname(__file__))+ '/TextFiles' + '/' + 'SwordbrookStoryIntro.txt')
SBNIntro = ((os.path.dirname(__file__))+ '/TextFiles' + '/' + 'SwordbrookNarratorIntro.txt')
SBFTPI = ((os.path.dirname(__file__))+ '/TextFiles' + '/' + 'SwordbrookFirstTimePlayerInfo.txt')
SBLogo = ((os.path.dirname(__file__))+ '/TextFiles' + '/' + 'SwordbrookLogo.txt')
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
 
#---------------------This section defines the mechanics for the main menu. It is called first before the game instance method is called---------------------------#
def main_menu():
    stillPlaying = True 
    menuEntryAttempts = 0
    Printer = FE.Display() #Create printer object from the Display class
    while ((menuEntryAttempts in range(10)) and stillPlaying == True):
        #print('Pass number ' + str(menuEntryAttempts))#COMMENT ME AFTER DEBUG!
        
        Printer.PrettyPrintString("Would you like to \"play\" , \"reset\" , or \"exit\"" + '\n \n','fast',clearScreen = False,allLeftJustifiedText = True)
        MainState = str(input('\n'))
        if (MainState.lower() == "play" or MainState.lower() == "p"):
            currentGame = game() #Creates an instance of the class game for use during this session of play and executes it's initialization function.0
            currentGame.session()#Calls the "session" function in game which will contain the primary game loop.
            return
        elif (MainState.lower() == "reset" or MainState.lower() == "r"):
            #This code is used to remove the existing save data for already generated characters and allow the game to start as though it was a fresh installation of Swordbrook
            try:
                #print(os.path.abspath(__file__))#COMMENT ME AFTER DEBUG!
                os.remove(scriptDirectoryPath + '/' + 'CharacterFile.csv')
                Printer.PrettyPrintString('Game reset to orginal installation','fast')
            except:
                Printer.PrettyPrintString('Game already in initial state','fast')
            menuEntryAttempts += 1
        elif (MainState.lower() == "exit" or MainState.lower() == "e"):
            sys.path.remove(scriptDirectoryPath) #this code removes the path to the main game folder from the system path as a housekeeping measure before exiting.
            Printer.AddBlankLines(3,False)
            Printer.PrettyPrintString('Goodbye!','fast')
            exit()
        else:
            #If a user provides and input that is not on the approved list of inputs this code should catch the mistake (User Input Injection prevention to come in later version) 
            Printer.Clean()
            Printer.PrettyPrintString('\ninvalid input please enter "play" , "reset", or "exit"' + '\n \n','fast',clearScreen = True,allLeftJustifiedText = False)
            menuEntryAttempts += 1
    del Printer#Clean up existing Printer Instance
    return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#-----------------------------The game class contains the primary game loop, login function, and introduction to the world/game------------------------------------#
class game(object):
    def __init__(self):
        #print("I have entered the game function init")#COMMENT ME AFTER DEBUG!
        
        #print(scriptDirectoryPath)#COMMENT ME AFTER DEBUG!
        self.CharacterFile = (scriptDirectoryPath + '/' + 'CharacterFile.csv')
        #print(self.CharacterFile)#COMMENT ME AFTER DEBUG!
        Printer = self.Printer = FE.Display() #Create printer object from the Display class
        if (os.path.exists(self.CharacterFile) != True):
            Printer.AddBlankLines(3,False)
            #Printer.PrettyPrintDoc(SBLogo,'InstantNoLag',True)
            Printer.PrettyPrintString('Welcome to Swordbrook since Its your first time playing let\'s introduce a few things...','fast')
        
            FE.characterFileManager.MakeCharacterFile(self.CharacterFile)
            Printer.PrettyPrintDoc(SBFTPI,'fast',False,False,False)
            
            #print('a whooooooole bunch more info will go here when there\'s a new game \n')
        #Begin Character Gen portion
        else :
            Printer.PrettyPrintString('Welcome back to Swordbrook!','fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
            
        #print('The game file exists now \n')
    
    
    def session(self):
        #Step 1 is to log the user in
        
        #print("I made it to the session function")#COMMENT ME AFTER DEBUG!
        self.activeCharDF = pd.DataFrame(columns=['NAME','ROWINDEX'])  #This stores a list of the currently logged in users where each name value is linked to a key containing it's index in the userdata dataframe.
        self.login()
        
        #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
        #print(self.activeCharDF.loc[0,'NAME'] + "\n")#COMMENT ME AFTER DEBUG!
        
        FE.characterFileManager.FirstLoginCheck(self)
        #print(self.red)
        Char.Character.PartyBuilder(self)
        
        
        print("Reaching this point verifies that the entire multicharacter login and verificaiton process is working and that character data is being correctly populated into the CSV file acting as a local database for game info. The next step will be to copy the character making code into the Monster Module to automatically generate monster and then link the combat part of the code back to the login part.")


############################ Just tempt code to keep function from exiting while I write stuff#########################
        Merp = False
        while (Merp == False):
            time.sleep(1)
            if (input("repond 1:") == "1"):
                Merp = True
#############################Remove the above block after combat functions are written#################################        
        


    def login(self):
        #self.activeCharDF = activeCharDF
        #print("I made it to the login function")#COMMENT ME AFTER DEBUG!
        Printer = FE.Display() #Create printer object from the Display class
        
        self.df = pd.read_csv(self.CharacterFile) #This line creates the dataframe that will be used to read and manage the data in the character file.
        Printer.Clean()
        Printer.PrettyPrintString("What is your characters name?",'fast',clearScreen = False,allLeftJustifiedText = True)
        self.currentName = (str(input("\n")))
        FE.characterFileManager.NameInputValidation(self, self.currentName)
        self.currentNameIndex = [] #holds in index
        
        ############Optional debug code for checking variable values################
        # print(self.currentName)
        # print(self.CharacterFile)
        # doesCurrentNameExist = FE.characterFileManager.DoesCharExist(self, self.currentName,self.CharacterFile)
        # print(doesCurrentNameExist)
        ############################################################################
        
        #try:
        if(self.currentName == ''):
            nullNameLoop=0
            while(nullNameLoop in range(10) and self.currentName == ''):
                remainingItters = str(10 - nullNameLoop)
                Printer.PrettyPrintString("No input recieved. Character name cannot but null. " + remainingItters + " attempts remaining",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                Printer.PrettyPrintString("Please enter your characters name ",'fast',clearScreen = False,allLeftJustifiedText = True)
                self.currentName = (str(input("\n"))).lower()
                nullNameLoop += 1 
                if (nullNameLoop == 10):
                    Printer.PrettyPrintString("Too many empty values entered. 0 attempts remaining." ,'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                    time.sleep(1)
                    Printer.PrettyPrintString("shutting down...",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                    time.sleep(2)
                    exit()

        doesCurrentNameExist = FE.characterFileManager.DoesCharExist(self,self.currentName,self.CharacterFile) #Calls DoesCharExist function to check the dataframe for existing instances of this character name
        if doesCurrentNameExist == True: #loads character data if name is that of an existing character in the character file
            #print("I think the name exists!")#COMMENT ME AFTER DEBUG!
            #print (self.currentNameIndex) #COMMENT ME AFTER DEBUG!
            Printer.PrettyPrintString('\nplayer data found! one moment...','fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
            indexOfCharacterName = self.df.index[self.df['Name'] == self.currentName].tolist()
            #print(len(self.activeCharDF))#COMMENT ME AFTER DEBUG!
            #print(self.activeCharDF)#COMMENT ME AFTER DEBUG!
            self.activeCharDF.loc[len(self.activeCharDF)] = [self.currentName,indexOfCharacterName]
            
            print (self.df.iloc[self.currentNameIndex])
            print ("\n\n")
        elif doesCurrentNameExist == False: #begins Character Creation Phase
            #print("I think the name does not exist!")#COMMENT ME AFTER DEBUG!
            self.makingACharacter = True #This variable and it's corresponding use in the following while loop could be removed and replaced with lines that set loop=10 for greater effeciency but this format provides more readable code.
            newLoginLoop = 0
            while ((newLoginLoop in range(10)) and self.makingACharacter == True):
                Printer.PrettyPrintString('No such character found.','fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                Printer.PrettyPrintString('Would you like to register a new character with this name? yes/no','fast',clearScreen = False,allLeftJustifiedText = True,isArtOnly = False)
                inputval = input ('\n').lower()
                if(inputval == 'y' or inputval == 'yes'):
                    Char.Character.MakeNewCharacter(self, self.currentName)
                    #print("Called make character function")#COMMENT ME AFTER DEBUG!
                    
                elif(inputval == 'n' or inputval == 'no'):
                    Printer.PrettyPrintString('Returning to main menu.','fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                    self.makingACharacter = False
                    return
                else:
                    Printer.PrettyPrintString('Returning to main menu.','fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                    newLoginLoop += 1
        del Printer#Clean up existing Printer Instance
        return()
        #except:
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
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

        





 
#------------------Main function for program. By having it only call the main function additinal programs or options could be added later--------------------------# 
def main():
    #Kept for maybe intro bit #game.prettyPrint('SwordbrookStoryIntro.rtf')
    main_menu()
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#    
    
if __name__ == "__main__":
    main()