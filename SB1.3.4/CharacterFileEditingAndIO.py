#---------------------------------------------------This section is for importing existing python modules----------------------------------------------------------#
import csv,os,sys,string,time,textwrap
import pandas as pd
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#------------------This contains functions which handle making, searching and editing the the files in the swordsbrook home directory------------------------------#
class characterFileManager():
    
    #self.red = 3
    
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
                Display.Clean()
                Display.PrettyPrintString("character names must be comprised of only UPPERCASE letters, lowercase letters, numbers, spaces, and the symbols _, -, ~, or '", "\nYou have " + str(10 - self.validationCounter) + " attempts remaining",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                Display.PrettyPrintString("Please try again. What is your characters name?",'fast',clearScreen = False,allLeftJustifiedText = True,isArtOnly = False)
                self.currentName = (str(input("\n"))).lower()
                self.validationCounter += 1
            if (self.validationCounter == 10):
                self.Printer.PrettyPrintString("Too many invalid character entries attempted!",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
                time.sleep(1)
                self.Printer.Clean()
                self.Printer.PrettyPrintString("Shutting down...",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                time.sleep(2)
                self.Printer.PrettyPrintString("Please play again soon!",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                time.sleep(1)
                exit()
            return 

    def FirstLoginCheck(self): #This function checks to see if there is atleast one character is logged in by checking the active characters dataframe.
        while(str(len(self.activeCharDF)) == '0'): #In the event that there are no currently logged in characters this loop gives the player an unlimited number of attempts to either continue playing and enter the login function or exit the game.
            self.Printer.PrettyPrintString("There are currently no characters logged in. You will need to create or login wtih atleast 1 character to play the game\n",'fast',clearScreen = True,allLeftJustifiedText = False,isArtOnly = False)
            self.Printer.PrettyPrintString("Would you like to keep playing? yes/no",'fast',clearScreen = False,allLeftJustifiedText = True,isArtOnly = False)
            userResponse1 = (str(input("\n"))).lower()
            if(userResponse1 == 'y' or userResponse1 == 'yes'):
                self.login()
            elif (userResponse1 == 'n' or userResponse1 == 'no'):
                self.Printer.Clean()
                time.sleep(1)
                self.Printer.PrettyPrintString("Shutting down...",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                time.sleep(2)
                self.Printer.PrettyPrintString("Please play again soon!",'fast',clearScreen = False,allLeftJustifiedText = False,isArtOnly = False)
                time.sleep(1)
                exit()
        return
#------------------------------------------------------------------------------------------------------------------------------------------------------------------#
class Display(object):

    def PrettyPrintDoc(self,printDoc: str, printSpeed,clearScreen = True,allLeftJustifiedText = False,isArtOnly = False):

        #####################Define local variables not given by arguments########################    
        artPrintFlag = False
        leftJustifiedTextFlag = False
        terminalSizeTuple = os.get_terminal_size()  
        ##########################################################################################    
        
        
        #####Set local vaiables for print speed and paragraph pauses from functino arguments######
        
        if (printSpeed == 'slow'):
            speed = 0.065
            hangtime = 5
        elif (printSpeed == 'fast'):
            speed = 0.020
            hangtime = 2
        elif (printSpeed == 'veryfast'):
            speed = 0.0001
            hangtime = 2
        elif (printSpeed == 'instant'):
            speed = 0.000
            hangtime = 4
        elif (printSpeed == 'slownolag'):
            speed = 0.065
            hangtime = 0.020
        elif (printSpeed == 'fastNoLag'):
            speed = 0.020
            hangtime = 0.020
        elif (printSpeed == 'veryFastNoLag'):
            speed = 0.050
            hangtime = 0.020
        elif (printSpeed == 'instantNoLag'):
            speed = 0.000
            hangtime = 0.005
        ##########################################################################################
       
        if (clearScreen):
            self.Clean()
        with open(printDoc, 'r+') as printText:
            for char in printText:
                printStr = str(char)    
                    
                if (printStr == ' \n'):
                    print('\n')
                    time.sleep(0.01)
                
                elif (printStr.lower().startswith('-clean')):
                    self.Clean()
                    printStr=''                
                elif (printStr.lower().startswith('-artprint')):
                    artPrintFlag^=True
                    printStr=''
                elif (printStr.lower().startswith('-justifytext')):
                    if printStr.endswith('\n'):
                            printStr = printStr[:-1]
                    if (printStr.lower().endswith('left')):
                        leftJustifiedTextFlag = True
                    elif (printStr.lower().endswith('center')):
                        leftJustifiedTextFlag = False
                    printStr=''
                elif (printStr.lower().startswith('-clearscreen')):
                    clearScreenFlag^=True
                    printStr=''
                elif (printStr.lower().startswith('-setprintspeed')):
                        if printStr.endswith('\n'):
                            printStr = printStr[:-1]
                        if (printStr.lower().endswith('slow')):
                            speed = 0.065
                            hangtime = 5
                        elif (printStr.lower().endswith('fast')):
                            speed = 0.020
                            hangtime = 2
                        elif (printStr.lower().endswith('veryfast')):
                            speed = 0.0001
                            hangtime = 2
                        elif (printStr.lower().endswith('instant')):
                            speed = 0.000
                            hangtime = 4
                        elif (printStr.lower().endswith('slownolag')):
                            speed = 0.065
                            hangtime = 0.020
                        elif (printStr.lower().endswith('fastnolag')):
                            speed = 0.020
                            hangtime = 0.020
                        elif (printStr.lower().endswith('veryFastNoLag')):
                            speed = 0.000001
                            hangtime = 0.020
                        elif (printStr.lower().endswith('instantnolag')):
                            speed = 0.000
                            hangtime = 0.005
                        printStr=''
                
                elif (printStr != '' and printStr != '\n'):
                    if printStr.endswith('\n'):
                        printStr = printStr[:-1]
                    if(artPrintFlag==False and isArtOnly==False):
                        print("\n")
                        printStr = textwrap.fill(printStr, width=terminalSizeTuple[0])
                    if(len(printStr) <= (terminalSizeTuple[0])):
                        if (leftJustifiedTextFlag == False and allLeftJustifiedText == False):
                            printStr = printStr.center(terminalSizeTuple[0]) 
                    for character in printStr:
                        print(character, end='') 
                        sys.stdout.flush() 
                        time.sleep(speed)
                    time.sleep(hangtime)
                    if (clearScreen and clearScreenFlag):
                        self.Clean()
                
                
                else:
                    time.sleep(0.001)
                    if (clearScreen and clearScreenFlag):
                        self.Clean()
                    
    def PrettyPrintString(self,printStr: str, printSpeed,clearScreen = True,allLeftJustifiedText = False,isArtOnly = False):

        #####################Define local variables not given by arguments########################    
        terminalSizeTuple = os.get_terminal_size()  
        ##########################################################################################
        
        if (printSpeed == 'slow'):
            speed = 0.065
            hangtime = 5
        elif (printSpeed == 'fast'):
            speed = 0.020
            hangtime = 2
        elif (printSpeed == 'veryfast'):
            speed = 0.0001
            hangtime = 2
        elif (printSpeed == 'instant'):
            speed = 0.000
            hangtime = 4
        elif (printSpeed == 'slownolag'):
            speed = 0.065
            hangtime = 0.020
        elif (printSpeed == 'fastNoLag'):
            speed = 0.020
            hangtime = 0.020
        elif (printSpeed == 'veryFastNoLag'):
            speed = 0.050
            hangtime = 0.020
        elif (printSpeed == 'instantNoLag'):
            speed = 0.000
            hangtime = 0.005
        
        if (clearScreen):
            self.Clean()
        
        #printStr = str(stringToPrint)
        if (printStr != '' and printStr != '\n' and printStr != ' \n'):
            if(isArtOnly==False):
                print("\n")
                printStr = textwrap.fill(printStr, width=terminalSizeTuple[0])
            if(len(printStr) <= (terminalSizeTuple[0])):
                if (allLeftJustifiedText == False):
                    printStr = printStr.center(terminalSizeTuple[0])
            for character in printStr:
                print(character, end='') 
                sys.stdout.flush() 
                time.sleep(speed)
            time.sleep(hangtime)
            if (clearScreen):
                self.Clean()

        elif(printStr == ' \n' or '\n'):
            print('\n')
            time.sleep(0.01)
        
        else:
            time.sleep(0.001)
            if (noClear ==  False):
                self.Clean()

    def Clean(self):
        # For Windows
        if os.name == 'nt':
            os.system('cls')

        # For macOS and Linux
        else:
            os.system('clear')
            
    def AddBlankLines(self,numberOfLines,noClear):
        if (noClear ==  False):
            self.Clean()
        for n in range(numberOfLines):
            print('\n')