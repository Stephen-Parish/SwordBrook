import csv
import os
import sys
import time
import pandas as pd

NameFile = ((os.path.dirname(__file__))+ '/' + 'NameFile.csv')


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
        
    
MkFile()
editfile()
    
    
    
    

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