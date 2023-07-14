import csv
import os
import sys
import time
import textwrap
import pandas as pd

NameFile = ((os.path.dirname(__file__))+ '/' + 'NameFile.csv')
SBStory = ((os.path.dirname(__file__))+ '/Text' + '/' + 'SwordbrookStoryIntro.txt')
SBNIntro = ((os.path.dirname(__file__))+ '/Text' + '/' + 'SwordbrookNarratorIntro.txt')
SF = ((os.path.dirname(__file__))+ '/' + '/Text' + 'ShortFile.txt')
SBLogo = ((os.path.dirname(__file__))+ '/Text' + '/' + 'SwordBrookLogo.txt')
SBLogoT = ((os.path.dirname(__file__))+ '/Text' + '/' + 'SwordBrookLogoTest.txt')
SBLogoTNT = ((os.path.dirname(__file__))+ '/Text' + '/' + 'SwordBrookLogoTestNotTxt')

# def referencecodenotmine():
    # with open('eggs.csv', 'w', newline='') as csvfile:
        # spamwriter = csv.writer(csvfile, delimiter=' ',
                                # quotechar='|', quoting=csv.QUOTE_MINIMAL)
        # spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
        # spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

def MkFile():
    NameFile = ((os.path.dirname(__file__))+ '/' + 'NameFile.csv')
    with open(NameFile, 'w') as FileOfNames:
        NameWrite = csv.writer(FileOfNames)
        
        Column_Titles = ['Name','Class','HP', 'AP']
        NameWrite.writerow(Column_Titles)
        for n in range(1,20):
            if((n == 10)or(n == 15) or (n==20)):
                IteratorTestList = ['greg','x','y','z']
                NameWrite.writerow(IteratorTestList)
            
            else:
                IteratorTestList = [n,'a','b','c']
                NameWrite.writerow(IteratorTestList)
                kevinTestList = ['kevin',n,n,n]
                NameWrite.writerow(kevinTestList)
                
        print('end of FileOfNames write function')
        
def editfile():
    playerNameToDataFileRowDict = { 'Testkey1':'TestValue1','Testkey1':'TestValue1',}
    print('ayo')
    #with open(NameFile, 'r+', newline='') as csvfile:
        #reader = csv.reader(csvfile)
        # loop through the rows in the CSV file
        
    df = pd.read_csv(NameFile)
    #print(df)
    #print(df.shape)
    df['Name'] = df['Name'].replace(['kevin'], 'larry')
    #print(df)
    #indexNum = df[df['Name'] == 'greg'] #[samwise]
    #indexNum2 = df['Name'].value_counts()
    #indexNum3 = df.loc[0]
    searchName = 'godzilla'
    indexNum4 = df.index[df['Name'] == searchName].tolist()
    #indexNum = df.query('Name' == 'greg') #['samwise']
    print(df.values[df['Name'] == 'greg'])
    print(df.loc[7,'Name'])
    #print(indexNum)
    
    #print(indexNum2)
    #print(indexNum)
    print('\n')
    
    #var = ['appendedname']
    #pd.concat(df,var)
    df.loc[len(df)] = ["appendedname",0,0,0]
    printlist =(df['Name'].tolist())
    print (*printlist, sep =', ')
    #########################################
    #print(NameFile)
    #print(df)
    df.to_csv(NameFile)
    
    #########################################
    
    
    try:
        print(indexNum4[0])
    except:
        print('no instances of ' + searchName + ' found.')
    if (indexNum4 == ''):
        print('it was empty!')
    #df.to_csv(NameFile)
    
        
############################################################################################################################################
###########################################################The Function below will be used to test pretty printing##########################
############################################################################################################################################

def PrettyPrintDoc(printDoc, printSpeed,clearScreen = True,allLeftJustifiedText = False,isArtOnly = False):

    #####################Define local variables not given by arguments########################    
    artPrintFlag = False
    leftJustifiedTextFlag = False
    clearScreenFlag = True
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
        Clean()
    with open(printDoc, 'r+') as printText:
        for char in printText:
            printStr = str(char)    
                
            if (printStr == ' \n'):
                print('\n')
                time.sleep(0.01)
                
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
                if(len(printStr) <= (terminalSizeTuple[0]-1)):
                    if (leftJustifiedTextFlag == False and allLeftJustifiedText == False):
                        printStr = printStr.center(terminalSizeTuple[0]) 
                for character in printStr:
                    print(character, end='') 
                    sys.stdout.flush() 
                    time.sleep(speed)
                time.sleep(hangtime)
                if (clearScreen and clearScreenFlag):
                    Clean()
            
            
            else:
                time.sleep(0.001)
                if (clearScreen and clearScreenFlag):
                    Clean()
                
def PrettyPrintString(printDoc, printSpeed,clearScreen = True,allLeftJustifiedText = False,isArtOnly = False):

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
    
    printStr = str(stringToPrint)
    if (printStr != '' and printStr != '\n' and printStr != ' \n'):
        if(isArtOnly==False):
            print("\n")
            printStr = textwrap.fill(printStr, width=terminalSizeTuple[0])
        if(len(printStr) <= (terminalSizeTuple[0]-1)):
            if (allLeftJustifiedText == False):
                printStr = printStr.center(terminalSizeTuple[0]) 
        for character in printStr:
            print(character, end='') 
            sys.stdout.flush() 
            time.sleep(speed)
        time.sleep(hangtime)
        if (clearScreen):
            Clean()

    elif(printStr == ' \n' or '\n'):
        print('\n')
        time.sleep(0.01)
    
    else:
        time.sleep(0.001)
        if (noClear ==  False):
            self.Clean()

def Clean():
    # For Windows
    if os.name == 'nt':
        os.system('cls')

    # For macOS and Linux
    else:
        os.system('clear')
    
# def PrintafileTest():
    # with open(SBLogo, 'r+') as printText:
        # text = printText.read
        # print(text)

        
        
        
        
        
        
        
        
############################################################################################################################################        


###########################################################################################################################################
###########################################################The Function below will be used to test pretty printing##########################
############################################################################################################################################

# def Clean():
    # # For Windows
    # if os.name == 'nt':
        # os.system('cls')

    # # For macOS and Linux
    # else:
        # os.system('clear')

############################################################################################################################################





#def TinyFunc():
#    variable = 'AAA bbb ccc ddd'













  
        # interestingrows=[row for idx, row in enumerate(reader) if idx in (3,4)]
        # print(interestingrows)
        
        # for row in enumerate(reader):
            # # check if this is the 3rd row (i.e. index 2)

            # if i == 2:
                # # replace the element in the 4th column (i.e. index 3)
                # row[3] = 700000
        
        
        
        
        
        # for row in csvfile:
            # if (row[0] == 'kevin'):            
                # sys.stdout.write(row[2])
                # sys.stdout.flush()
                # time.sleep(1.0)
        


############################################################################################################################################
###############################################Function calls###############################################################################
############################################################################################################################################


PrettyPrintDoc(SBLogo,'instantNoLag',True,False,False)
time.sleep(5)
#PrettyPrintDoc(SBStory,'slow')
#stringThatImGonnaPrint = "\nThis is a long string that should prove the formating for the string version of the pretty printing function is working correctly"
#PrettyPrintString(stringThatImGonnaPrint,'slow')
#PrintafileTest()

#MkFile()
#editfile()
#TinyFunc()   
#############################################^Function calls^###############################################################################    
    
    

        # # get number of columns
        # for line in csvfile.readlines():
            # array = line.split(',')
            # first_item = array[0]

        # num_columns = len(array)
        # csvfile.seek(0)

        # reader = csv.reader(csvfile, delimiter=' ')
            # included_cols = [1, 2, 6, 7]

        # for row in reader:
                # content = list(row[i] for i in included_cols)
                # print content
                
# print('     _                                                                    __   ')
# print('    | |            _____                 _ _               _              \ \  ')
# print(' ___| |_____ _____|   __|_ _ _ ___ ___ _| | |_ ___ ___ ___| |_ _____ _____ \ \ ')
# print('|___| |_____|_____|__   | | | | . |  _| . | . |  _| . | . | \'_|_____|_____| > >')
# print('    | |_____|_____|_____|_____|___|_| |___|___|_| |___|___|_,_|_____|_____|/ / ')
# print('    |_|                                                                   /_/  ')