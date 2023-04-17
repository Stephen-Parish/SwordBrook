import csv,os,sys,string
import pandas as pd

class characterFileManager:
    
    def MakeCharacterFile(CharacterFile):
        with open(CharacterFile, 'w') as CharDatFile:
            FileWrite = csv.writer(CharDatFile)
            
            Column_Titles = ['Name','Class','HP', 'AP']
            FileWrite.writerow(Column_Titles)
            #for n in range(1,20):
            #    IteratorTestList = [n,'a','b','c']
            #    FileWrite.writerow(IteratorTestList)
                
    def DoesCharExist(self,currentName,CharacterFile):
        #print(self)#COMMENT ME AFTER DEBUG!
        #print(currentName)#COMMENT ME AFTER DEBUG!
        #print(CharacterFile)#COMMENT ME AFTER DEBUG!
        #df = pd.read_csv(CharacterFile)
        #print(df)#COMMENT ME AFTER DEBUG!
        indexOfCurrentName = self.df.index[self.df['Name'] == currentName.lower()].tolist()
        #print(indexOfCurrentName)#COMMENT ME AFTER DEBUG!
        if (indexOfCurrentName == []):            
            return False
        else:
            self.currentNameIndex = indexOfCurrentName
            return True
    
    def Write(self, dataFrameToWrite, fileToWriteto):
        dataFrameToWrite.to_csv(fileToWriteto,index=False)
        return
            
    def NameInputValidation(self,inputToValidate):
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

    def FirstLoginCheck(self):
        while(str(len(self.activeCharDF)) == '0'):
            print("There are currently no characters logged in. You will need to create or login wtih atleast 1 character to play the game\n")
            userResponse1 = (str(input("Would you like to keep playing? yes/no" + "\n"))).lower()
            if(userResponse1 == 'y' or userResponse1 == 'yes'):
                self.login
            elif (userResponse1 == 'n' or userResponse1 == 'no'):
                exit()
        return