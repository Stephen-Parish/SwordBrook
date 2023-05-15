#---------------------------------------------------This section is for importing existing python modules----------------------------------------------------------#
import csv,os,sys,string
import pandas as pd
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------This contains functions which handle making, searching and editing the the files in the swordsbrook home directory------------------------------#
class characterFileManager:
    
    def MakeCharacterFile(CharacterFile): #This function is used to create the CharactreFile including a data template.
        with open(CharacterFile, 'w') as CharDatFile: #Creates a new instance of the CharacterFile.csv file to hold user data
            FileWrite = csv.writer(CharDatFile) #Shortens write command by assign to variable
            
            Column_Titles = ['Name','Class','HP', 'AP'] #Defines the column names for the CSV. Note that this does not include the index of each column in the dataframes made from the data in the CSV which is kept seperately as a value of the dataframe.
            FileWrite.writerow(Column_Titles)
                            
    def DoesCharExist(self,currentName,CharacterFile):
        #print(self)#COMMENT ME AFTER DEBUG!
        #print(currentName)#COMMENT ME AFTER DEBUG!
        #print(CharacterFile)#COMMENT ME AFTER DEBUG!
        #df = pd.read_csv(CharacterFile)
        #print(df)#COMMENT ME AFTER DEBUG!
        indexOfCurrentName = self.df.index[self.df['Name'] == currentName.lower()].tolist() #Converts current name to a lowercase string and then searches the name column of the dataframe for matching strings. The row index of each mach is the appended to a list.
        #print(indexOfCurrentName)#COMMENT ME AFTER DEBUG!
        if (indexOfCurrentName == []): #Checks to see if there were no instances of matching strings and if there were none the function returns false. 
            return False
        else:
            self.currentNameIndex = indexOfCurrentName #Adds first index where string matches to a variable so that we can find access it.
            return True
    
    def Write(self, dataFrameToWrite, fileToWriteto): #writes contents of a dataframe to a CSV file.
        dataFrameToWrite.to_csv(fileToWriteto,index=False)
        return
            
    def NameInputValidation(self,inputToValidate): #Compares characters in a name string to a set of lists of allowed characters to determin if name is a valid and non-malicious string.
        self.validationCounter = 0
        self.validCharacterList = set((list(string.ascii_lowercase)) + (list(string.ascii_uppercase)) + (list(string.hexdigits)) + ['_','-','~','\''])
        #print(self.validCharacterList)#COMMENT ME AFTER DEBUG!
        for self.validationCounter in range(10):
            if any(char not in self.validCharacterList for char in inputToValidate):
                print("character names must be comprised of only UPPERCASE letters, lowercase letters, numbers, spaces, and the symbols _, -, ~, or '", "\nYou have " + str(10 - self.validationCounter) + " attempts remaining")
                self.currentName = (str(input("Please try again. What is your characters name?" + "\n"))).lower()
                self.validationCounter += 1
            if (self.validationCounter == 10):
                print("Too many invalid character entries attempted!")
                time.sleep(1)
                print("Shutting down...")
                time.sleep(2)
                print("Please play again soon!")
                time.sleep(1)
                exit()
            return 

    def FirstLoginCheck(self): #This function checks to see if there is atleast one character is logged in by checking the active characters dataframe.
        while(str(len(self.activeCharDF)) == '0'): #In the event that there ar eno currently logged in characters this loop gives the player an unlimited number of attempts to either continue playing and enter the login function or exit the game.
            print("There are currently no characters logged in. You will need to create or login wtih atleast 1 character to play the game\n")
            userResponse1 = (str(input("Would you like to keep playing? yes/no" + "\n"))).lower()
            if(userResponse1 == 'y' or userResponse1 == 'yes'):
                self.login
            elif (userResponse1 == 'n' or userResponse1 == 'no'):
                exit()
        return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#