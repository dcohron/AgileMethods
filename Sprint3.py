#  Class: SSW-555
#  Project:  Project Assignment #3
#  Author: David N. Cohron, Amie Widerkehr, Jeremy Doll
#  Date: 19 July 2017

## Other files:
# My-Family-18-May-2017-411.ged   GEDCOM file for the Brady Family
# CodeOutputProject#3.txt     Output to terminal from this program and input file above

# Honor Code Statement
# We pledge on our honor that we have not given or received any 
# unauthorized assistance on this assignment/examination. 
# We further pledge that we have not copied any material from 
# a book, article, the Internet or any other source except 
# where we have expressly cited the source.
# Signature: Jeremy Doll			Date: 19 July 2017
# Signature: Amie Widerkehr			Date: 19 July 2017
# Signature: David N. Cohron		Date: 19 July 2017

# References:
# 1) StackOverflow
# 2) GEDCOM tag full list:  http://wiki-en.genealogy.net/GEDCOM-Tags
# 3) Error Handling:  http://www.pythonforbeginners.com/error-handling/python-try-and-except

### NOTE:
# Data structure- 
# individuals[individualID] = {'NAME':'NA', 'SEX':'NA', 'BIRT':'NA', 'DEAT':'NA'}
# families[familyID] = {'HUSB':'NA', 'WIFE':'NA', 'CHIL':'NA', 'MARR':'NA', 'DIV':'NA'}
# 	All values in dictionaries are strings and therefore
#  		must be cast to other types prior to calculation
# 	AGE and ALIVE are calculated fields 
# 	CHIL, HUSB and WIFE are calculated from the "families" dictionary
# 	CHIL value is a list of strings of the children's individual IDs

monthInts = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, "DEC": 12}

def readFile(path):
    '''Reads input file and returns two dictionaries.'''
    # read in entire file into list of lines
    f = open(path, 'r')
    data = f.read().splitlines()
    f.close()

    # remove empty lines from list of lines
    data = list(filter(None, data))
    # print(data)
            
    while data:
        wordList = getWords(data)
        # print(wordList)
        
        # skips leading comments and any line that does not
        # start with a number
        if wordList[0].isdigit():
            
            # print (wordList)
            # print(len(wordList))
            remainder = ''.join(str(w + " ") for w in wordList[2:])
            
            # process individual tags
            if wordList[0] == '1' and wordList[1] in tagList:
                if wordList[1] == "NAME":
                    name = (wordList[2] + wordList[3])
                    individuals[individualID]["NAME"] = name
                    continue
                elif wordList[1] == "BIRT":
                    nextLine = getWords(data)
                    date = (nextLine[2] + nextLine[3] + nextLine[4])
                    individuals[individualID]["BIRT"] = date
                    continue
                elif wordList[1] == "DEAT":
                    nextLine = getWords(data)
                    date = (nextLine[2] + nextLine[3] + nextLine[4])
                    individuals[individualID]["DEAT"] = date
                    continue
                else:
                    # only tag left is 'SEX'
                    individuals[individualID][wordList[1]] = wordList[2]
                    continue
        
        # if tag in word 3 is one of two special tags, handle it
            elif (len(wordList) > 2) and ((wordList[2] == "INDI") or (wordList[2] == "FAM")):
                if wordList[2] == "INDI":
                    individualID = re.sub('@', '', wordList[1])

                    # US22- Check that individual ID is unique (not seen before)
                    if not uniqueIDCheck(individualID, individuals):
                        errorString = "ERROR: Individual: US22: Individual ID" + individualID + " not unique, new individual overwrote old."
                        IDErrorBuffer.append(errorString)
                        

                    individuals[individualID] = {'NAME':'NA', 'SEX':'NA', 'BIRT':'NA', 'DEAT':'NA'}
                    continue                
                else:
                    familyID = re.sub('@', '', wordList[1])

                    # US22- Check that family ID is , unique (not seen before)
                    if not uniqueIDCheck(familyID, families):
                        errorString = "ERROR: Family: US22: Family ID " + familyID + " not unique, new family overwrote old."
                        IDErrorBuffer.append(errorString)

                    # print("FamilyID= ", familyID)
                    families[familyID] = {'HUSB':'NA', 'WIFE':'NA', 'CHIL':[], 'MARR':'NA', 'DIV':'NA'}
                    wordList[0] = '1'
                    while wordList[0] != '0':
                        wordList = getWords(data)
                        #print(wordList)
                        if wordList[1] in famTags:
                            if (wordList[1] == "MARR") :
                                nextLine = getWords(data)
                                date = (nextLine[2] + nextLine[3] + nextLine[4])
                                families[familyID]["MARR"] = date
                                continue
                            elif (wordList[1] == "DIV"):
                                nextLine = getWords(data)
                                date = (nextLine[2] + nextLine[3] + nextLine[4])
                                families[familyID]["DIV"] = date
                                continue
                            elif (wordList[1] == "CHIL"):
                                individualNum = re.sub('@', '', wordList[2])
                                families[familyID]["CHIL"].append(individualNum)
                            else:
                                # for tags "HUSB" and "WIFE"
                                individualNum = re.sub('@', '', wordList[2])
                                families[familyID][wordList[1]] = individualNum
                                continue
                        else:
                            # print("Not a family tag of interest- skipping to next line.")
                            continue
                    # we have read one item into data too far
                    # to check end of family list
                    # so need to add back to data to continue processing
                    wordList = ' '.join(wordList)
                    data.insert(0, wordList)
                    continue
            
        # otherwise, invalid tag
            else:
                # print("Tag not of interest- skipping to next line.")
                continue
        else:
            # print("Exiting loop.")
            continue

    # for diagnostic purposes
    # print(individuals)
    # print(families)

    return individuals, families


def getWords(dataList):
    '''function to get next line and process into list of words'''
    line = dataList.pop(0)
    # strip trailing whitespace
    line = line.rstrip()
            
    # split line into words
    wordList = line.split()
    return wordList


####################################
# Below are functions that make calculations based on/add to the data.
# I will explain here how to work with it, with the following functions as
# examples.
# So, if you read the paragraph at the bottom about dictionaries, you know that
# they have some properties that make them annoying in some cases.  In addition
# to being easier to work with IMO, the data needs to be in list format for
# ptable.
# To do anything with the data, you need the fields (keys) and data (values),
# which
# I named the same in functions as when I made them down below for clarity.
# The table printouts are a good visualisation of the data, if you imagine each
# data row as a sub-list.
# First, find the index of what you want to work with with
# xxxFields.index(value)
# Now, you have the proper index x to call on xxxData[n][x] to reference what
# you
# need.
#
# If you need to check dates, you may need to use the parseDateString function.
# Noth that this returns multiple values, so you need to set multiple variables
# equal to its output.  If you need the current date, use the
# datetime.date.today
# method.  addAge is a good example, as it has both forms of date comparison.
#
# If you wish to add a column to the output table, remember to add the value to
# xxxData[i] and not just xxxData, and add a header for the column to
# xxxFields.
#
# Other than that, just be aware of what data types you're working with and
# keep
# them consistent.
def addAlive(indFields, indData):
    '''Adds header and data for an "alive" column for the individuals table'''
    deathIndex = indFields.index("DEAT")
    for i in range(len(indData)):
        if indData[i][deathIndex] == "NA":
            indData[i] += [True]
        else:
            indData[i] += [False]
    indFields += ["Alive"]
    return indFields, indData

def parseDateString(date):
    '''parses a date as given by the GEDCOM data and returns 3 corresponding integers
       meant to take in a string'''
    day = 0
    month = 0
    year = 0
    if date[1:4] in monthInts:
        #print(date[1:4])
        day = date[0]
        month = monthInts[date[1:4]]
        year = date[4:]
    else:
        day = date[0:2]
        month = monthInts[date[2:5]]
        year = date[5:]
    return int(day), int(month), int(year)
        
def addAge(indFields, indData):
    '''Adds header and data for an "age" column for the individuals table'''
    birthIndex = indFields.index("BIRT")
    deathIndex = indFields.index("DEAT")
    for i in range(len(indData)):
        if indData[i][deathIndex] == "NA":
            #need to use current date
            bday, bmonth, byear = parseDateString(indData[i][birthIndex])
            cday = dt.date.today().day
            cmonth = dt.date.today().month
            cyear = dt.date.today().year
            age = cyear - byear
            if cmonth <= bmonth:
                if cmonth == bmonth:
                    if cday < bday:
                        age -= 1
                else:
                    age -= 1
            indData[i] += [age]
        else:
            #need to use death date
            dday, dmonth, dyear = parseDateString(indData[i][deathIndex])
            bday, bmonth, byear = parseDateString(indData[i][birthIndex])
            age = dyear - byear
            if dmonth <= bmonth:
                if dmonth == bmonth:
                    if dday < bday:
                        age -= 1
                else:
                    age -= 1
            indData[i] += [age]
    
    indFields += ["Age"]
    return indFields, indData

def addFamNames(indFields, indData, famFields, famData):
    '''Adds header and data for spouse name columns for the families table'''
    wifeIndex = famFields.index("WIFE")
    husbIndex = famFields.index("HUSB")
    nameIndex = indFields.index("NAME")
    for i in range(len(famData)):
        hname = "NA"
        wname = "NA"
        husbID = famData[i][husbIndex]
        #print(husbID)
        for j in range(len(indData)):
            if(husbID == "NA"):
                hname = "NA"
                break
            if(indData[j][0] == husbID):
                hname = indData[j][nameIndex]
                break
        wifeID = famData[i][wifeIndex]
        #print(wifeID)
        for j in range(len(indData)):
            if(wifeID == "NA"):
                wname = "NA"
                break
            if(indData[j][0] == wifeID):
                wname = indData[j][nameIndex]
                break
        famData[i] += [hname, wname]
    famFields += ["HUSB Name", "WIFE Name"]
    return famFields, famData

def addChildSpouse(indFields, indData, famFields, famData):
    '''Adds header and data for Child and Spouse columns for the individuals table'''
    wifeIndex = famFields.index("WIFE")
    husbIndex = famFields.index("HUSB")
    childIndex = famFields.index("CHIL")
    for i in range(len(indData)):
        cID = indData[i][0]
        childlist = []
        for j in range(len(famData)):
            if cID in famData[j][childIndex]:
                childlist += [famData[j][0]]
        spouselist = []
        for j in range(len(famData)):
            if (cID == famData[j][wifeIndex]) or (cID == famData[j][husbIndex]):
                spouselist += [famData[j][0]]
        indData[i] += [childlist, spouselist]
    indFields += ["Child", "Spouse"]
    return indFields, indData  


def checkDates(dateString1, dateString2, offsetDays=0):
    ''' function to test if date2 occurs after date1
        passed two date strings and offset (in days), return boolean
        used to test: birth/death, birth/marriage, marriage/divorce
              marriage/death, divorce/death, birth date of parents/children'''
    dateGood = True
    date1 = dt.datetime.strptime(dateString1, "%d%b%Y")
    date2 = dt.datetime.strptime(dateString2, "%d%b%Y") 
    # print(date1 + dt.timedelta(days=offsetDays), date2)
    if (date1 + dt.timedelta(days=offsetDays)) >= date2: 
        dateGood = False
    # print(dateGood)
    return dateGood


def  marriageBeforeDivorce(marrString, divorceString):
    '''Sprint1 US04 - Marriage Before Divorce Check'''
    #print ()
    #print("Running Marriage Before Divorce Function")
 
    if checkDates(marrString, divorceString):
        # print("Divorce date is after marriage date check successful.")
        return True
    else:
        print("ERROR: US04: Divorce date is before marriage date, check unsuccessful.")
        return False
    

def marriageBeforeDeathCheck(key, marrString, husbDeathString, wifeDeathString):
    '''Sprint1 US05 - Marriage Before Death Check'''
    #print()

    if husbDeathString == "NA":
        # print(key, ":", families[key]["HUSB"], "- still alive or NA.")
        pass
    else:
        if checkDates(marrString, husbDeathString):
            # print(key, ":", families[key]["HUSB"], "- marriage prior to death, Successful check!")
            return True
        else:
            print("ERROR: US05:", key, ":", families[key]["HUSB"], "- marriage after death, Failed check!")
            return False
                   
    if wifeDeathString == "NA":
        # print(key, ":", families[key]["WIFE"], "- still alive or NA.")
        return True
    else:
        if checkDates(marrString, wifeDeathString):
            # print(key, ":", families[key]["WIFE"], "- marriage prior to death, Successful check!")
            return True
        else:
            print("ERROR: USO5:", key, ":", families[key]["WIFE"], "- marriage after death, Failed check!")
            return False
     

def divorceBeforeDeath(key, divorceString, husbDeathString, wifeDeathString):
    '''Sprint 1 US06 - Check Divorce before death'''
    if husbDeathString == "NA" and  wifeDeathString == "NA":
        # print(key, "- both still alive or NA.")
        return True
    else: # may need to check if both
        if husbDeathString != "NA" and not(checkDates(divorceString, husbDeathString)):
            print("ERROR: US06:", key, "/", families[key]["HUSB"], "- husband death prior to divorce.")
            return False
        elif wifeDeathString != "NA" and not(checkDates(divorceString, wifeDeathString)):
            print("ERROR: US06:", key, "/", families[key]["WIFE"], "- wife death prior to divorce.")
            return False
        else:
            # print(key, "- divorce/death dates check.")
            return True


def parentChildAgeCheck(key, childBirth, husbBirthString, wifeBirthString):
    '''Sprint 1 US12 - Check if parents are too old for their children'''

    if husbBirthString == "NA":
        # mother only
        if wifeBirthString == "NA":
            print("ERROR: US12:", key, "No mother or father listed for family, don't think this is possible")
            return False
        else:
            if checkDates(wifeBirthString, childBirth, 21915): # 60 years 15 leap
                print("ERROR: US12:", key, "- mother (", families[key]["WIFE"], ") > 60 years older than child.")
                return False
            else:
                # print(key, "- parent/child birth dates check.")
                return True
    elif wifeBirthString == "NA":
        #father only
        if husbBirthString == "NA":
            print("ERROR: US12:", key, "No mother or father listed for family, don't think this is possible")
            return False
        else:
            if checkDates(husbBirthString, childBirth, 29220): # 80 years 20 leap
                print("ERROR: US12:", key, "- father (", families[key]["HUSB"], ") > 80 years older than child.")
                return False
            else:
                # print(key, "- parent/child birth dates check.")
                return True
    else: # both parents present in row, THIS MAY NEED WORK IF BOTH
        if checkDates(husbBirthString, childBirth, 29220): # 80 years
            print("ERROR: US12:", key, "- father (", families[key]["HUSB"], ") > 80 years older than child.")
            return False
        elif checkDates(wifeBirthString, childBirth, 21915): # 60 years
            print("ERROR: US12:", key, "- mother (", families[key]["WIFE"], ") > 60 years older than child.")
            return False
        else:
            # print(key, "- parent/child birth dates check.")
            return True


def uniqueIDCheck(IDToCheck, IDDictionary):
    '''Sprint 2 US22 - Check that individual or family IDs are unique.'''
    IDList = list(IDDictionary.keys()) 
    return not (IDToCheck in IDList)



def CheckMultipleBirths(childList):
     '''US 14 - Check for less than 5 multiple births in family'''
     if childList == []:
         return True

     if len(childList) < 5:
         return True
     else:
         counter = 0
         newList = []
         for i in range(len(childList)):
             childsBirth = individuals[childList[i]]["BIRT"]
             newList.append(childsBirth)
         
         opt = [i for i, x in enumerate(newList) if newList.count(x) > 1]

         if len(opt) >= 5:
             print("ERROR: US14:", key, " Family has more than 5 births happening! (", len(opt), ")")
             return False
         else:
             return True

#
def CheckSameLastNameAsFather(childList):
    '''US 16 - Check for children have the same name as father'''
    if families[key]["HUSB"] != "NA":
        fathers_name = individuals[families[key]["HUSB"]]["NAME"]
    else:
        return True

    if childList == []:
        return True

    for i in range(len(childList)):
        child_name = individuals[childList[i]]["NAME"]
        childs_last_name = child_name.split('/')[1]
        fathers_last_name = fathers_name.split('/')[1]
        
        if childs_last_name != fathers_last_name:
            print ("ERROR: US16:", key, ": Family: Dad and Child don't have the same last name - Dad:", fathers_last_name, "Childs:", childs_last_name)
            return False
        else:
            return True


def uniqueFamilyCheck(familyDict):
    '''Sprint 2 US24 - Check that families are unique, by marriage date and spouse names.'''
    # if any of marriage date or spouse names are 'NA', cannot check that family => skip to next family
    uniqueTest = True
    familyList = []

    # iterate over dictionary of families looking for repeats
    for family, value in familyDict.items():
        marriageDate = familyDict[family]['MARR']
        husbandID = familyDict[family]['HUSB']
        wifeID = familyDict[family]['WIFE']

        # check for conditions that invalidate uniqueness check
        if marriageDate == 'NA' or husbandID == 'NA' or wifeID == 'NA':
            continue

        husbandName = individuals[husbandID]['NAME']
        wifeName = individuals[wifeID]['NAME']
        familyTuple = (marriageDate, husbandName, wifeName)

        # check for conditions that invalidate uniqueness check
        if 'NA' in familyTuple:
            continue

        if familyTuple in familyList:
            uniqueTest = False
            print("ERROR: Family: US24: Family", family,"not unique by marriage date and spouse names.")
        else:
            familyList.append(familyTuple)
    return uniqueTest

def checkUniqueChildrenNames(key, individuals, childList):
    '''US25 - Check if each child in a family has a unique name'''
    if len(childList) < 2:
        return True
    else:
        names = []
        for item in childList:
            temp = individuals[item]["NAME"].rsplit("/")
            names += [temp[0]] # add only first name as per spec
        if len(childList) != len(set(names)):
            print("ERROR: US25:", key, "- has multiple children with the same name")
            return False
        else:
            # print("US25 passed length check")
            return True

def checkFamToIndi26(key, families, individuals):
    '''US26 - Corresponding entries
       makes sure all Individual tags in a Family row appear in the individuals table'''
    idList = families[key]["CHIL"] # get children IDs
    if families[key]["HUSB"] != "NA":
        idList += [families[key]["HUSB"]] # get HUSB Id if it exists
    if families[key]["WIFE"] != "NA":
        idList += [families[key]["WIFE"]] # get WIFE Id if it exists
    for item in idList:
        if item not in individuals:
            print("ERROR: US26: Key", item, "from", key, "not in table.")
    return True

# This function is probably not necessary
def checkIndiToFam26(key, families, US26):
    '''US26 - Corresponding entries
       makes sure all Family tags in a individual row appear in the families table'''

    idList = US26[-1] + US26[-2] # the concatenated FIDs as appearing in the individuals table child and spouse columns

    for item in idList:
        if item not in families:
            print("ERROR: US26: Key", item, "from", key, "not in table.")
    return True

def ageCalc(birthDateString, dateString = '0'):
    '''US34 and US35- Calculate age in days at specific date.'''
    # If do not pass in second date, use today's date
    # print(birthDateString)
    # print(dateString)
    if dateString == '0':
        date1 = dt.datetime.today()
    else:
        date1 = dt.datetime.strptime(dateString, "%d%b%Y")

    birthDate = dt.datetime.strptime(birthDateString, "%d%b%Y")
    return (date1 - birthDate).days


# Main body of code:
# put code into try/except for error handling
try: 
    ## Import needed libraries
    import re
    import datetime as dt
    # from datetime import date

    from dateutil.parser import parse as dtparse
    from prettytable import PrettyTable
    finalp = PrettyTable()
    finalp2 = PrettyTable()

    # Define where to find the data file
    path1 = "./My-Family-18-May-2017-411.ged"
    path = path1

    # List of valid GEDCOM tags
    tagLong = ["ABBR", "ADDR", "ADR1", "ADR2", "ADOP", "AFN", "AGE", "AGNC", "ALIA", "ANCE", "ANCI", "ANUL", "ASSO", "AUTH", "BAPL", "BAPM", "BARM", "BASM", "BIRT", "BLES", "BLOB", "BURI", "CALN", "CAST", "CAUS", "CENS", "CHAN", "CHAR", "CHIL", "SHR", "CHRA", "CITY", "CONC", "CONF", "CONL", "CONT", "COPR", "CORP", "CREM", "CTRY", "DATA", "DATE", "DEAT", "DESC", "DESI", "DEST", "DIV", "DIVF", "DSCR", "EDUC", "EMAIL", "EMIG", "ENDL", "ENGA", "EVEN", "FACT", "FAM", "FAMC", "FAMF", "FAMS", "FAX", "FCOM", "FILE", "FONE", "FORM", "GEDC", "GIVN", "GRAD", "HEAD", "HUSB", "IDNO", "IMMI", "INDI", "LANG", "LATI", "LEGA", "LONG", "MAP", "MARB", "MARC", "MARL", "MARR", "MARS", "MEDI", "NAME", "NATI", "NATU", "NCHI", "NICK", "NMR", "NOTE", "NPFX", "NSFX", "OBJE", "OCCU", "ORDI", "ORDN", "PAGE", "PEDI", "PHON", "PLAC", "POST", "PROB", "PROP", "PUBL", "QUAY", "REFN", "RELA", "RELI", "REPO", "RESI", "RESN", "RETI", "RFN", "RIN", "ROLE", "ROMN", "SEX", "SLGC", "SLGS", "SOUR", "SPFX", "SSN", "STAE", "STAT", "SUBM", "SUBN", "SURN", "TEMP", "TEXT", "TIME", "TITL", "TRLR", "TYPE", "VERS", "WIFE", "WWW", "WILL"]
    tagShort = ["INDI", "NAME", "SEX", "BIRT", "DEAT", "FAMC", "FAMS", "FAM", "MARR", "HUSB", "WIFE", "CHIL", "DIV", "DATE", "HEAD", "TRLR", "NOTE"]
    tagInterest = ["NAME", "SEX", "BIRT", "DEAT"]
    famTags = ["HUSB", "WIFE", "CHIL", "MARR", "DIV"]
    tagList = tagInterest
    
    # declare empty dictionary as primary data structure
    individuals = {}
    families = {}

    # declare empty list to hold errors checked during read
    IDErrorBuffer = []

    individual, families = readFile(path)
    
    # this output is for development, comment out as necessary
    #print(individuals)
    #print(families)



    ### Output functionality
    # Some neat facts to know about this for better understanding:
    # Dictionarys in Python are unordered, meaning they do not have an index
    # associated with KV pairs as a list of tuples might.  This is why when you
    # run this and print out the dictionaries, they appear in random orders.
    # The keys or values can be converted into a list, in the order that the
    # program stores them.  What is weird but also very nice is that the
    # subdictonaries
    # always have the same ordering relative to each other.  So as you will see
    # when you
    # run this, the table columns are in different orders each time because
    # dictionaries
    # are unordered, but the data is never gets mixed up because
    # subdictionaries are always
    # relatively the same.  The filthy snake language strikes again.

    # We chose as a team to print empty set '[]' instead of 'NA' for table
    # cells with no value.

    # Idea:
    # build list w/ indices 0, 1 , 2 etc as normal
    # where 0 = index of I1, 1 = index of I2, etc
    indiIndexList = [0] * len(individuals) # populate with 0s
    indi = list(individuals.keys()) # unordered list of INDI keys
    indv = list(individuals.values()) # unordered list of values
    famIndexList = [0] * len(families) # populate with 0s
    fami = list(families.keys())
    famv = list(families.values())

    # This creates lists as specified above
    for i in range(1, len(indiIndexList) + 1):        
        ckey = "I" + str(i) #create "current key" that we want to find
        indiIndexList[i - 1] = indi.index(ckey) #set list value to location of that key
    for i in range(1, len(famIndexList) + 1):        
        ckey = "F" + str(i)
        famIndexList[i - 1] = fami.index(ckey)

    # Uncomment these for a better visual on what I'm doing
    #print(indi)
    #print(indiIndexList)
    #print(fami)
    #print(famIndexList)

    indFields = ["ID"] + list(indv[indiIndexList[0]].keys())
    indData = []
    famFields = ["ID"] + list(famv[famIndexList[0]].keys())
    famData = []
    # Using those lists, we listify our data (for easier printing) and sort it
    # in one go
    for i in range(len(individuals)):
        #sortedInd.update({indi[indiIndexList[i]]: indv[indiIndexList[i]]})
        temp = [indi[indiIndexList[i]]] + list(indv[indiIndexList[i]].values())
        indData += [temp]
    for i in range(len(families)):
        #sortedFam.update({fami[famIndexList[i]]: famv[famIndexList[i]]})
        temp = [fami[famIndexList[i]]] + list(famv[famIndexList[i]].values())
        famData += [temp]

    # This is the formatting magic
    # guide: https://pypi.python.org/pypi/PTable/0.9.2
    # if you get an import error run "pip install -U ptable" in the command
    # line
    # Individual Table

    indFields, indData = addAlive(indFields, indData)
    indFields, indData = addAge(indFields, indData)
    indFields, US26 = addChildSpouse(indFields, indData, famFields, famData)
    indData = US26 # this variable is used in the US26 evaluation
    famFields, famData = addFamNames(indFields, indData, famFields, famData)    
    
    finalp.field_names = indFields
    for i in range(len(indData)):
        finalp.add_row(indData[i])
    print(finalp)
    # Families Table
    finalp2.field_names = famFields
    for i in range(len(famData)):
        finalp2.add_row(famData[i])
    
    print(finalp2)

    print()
    print()
    print()

    ### Sprint 1:
    # US02: Check Birth before Marriage
    # print()
    # print("Birth/Marriage check")
    # print(families)
    for key, value in families.items():
        # print("Family number:", key)
        marrString = families[key]["MARR"]
        if marrString == "NA":
            print("ERROR: US02: For family %s no marriage date given." % key)
            continue

        # check husband birthdate
        husband = families[key]["HUSB"]
        husbandBirthString = individuals[husband]["BIRT"]
        if husbandBirthString == "NA":
            print("ERROR: US02: No husband.")
        elif checkDates(husbandBirthString, marrString):
            # print("   Husband birth date checks.")
            pass
        else:
            print("ERROR: US02: Husband", husband,"birth date does not check.")

        # check wife birthdate
        wife = families[key]["WIFE"]
        wifeBirthString = individuals[wife]["BIRT"]
        if wifeBirthString == "NA":
            print("ERROR: US02  No wife.")
        elif checkDates(wifeBirthString, marrString):
            # print("   Wife birth date checks.")
            pass
        else:
            print("ERROR: US02: Wife", wife,"birth date does not check.")


    # US03: Check Birth before Death
    # print()
    # print("Birth/Death check")
    # print(individuals)
    for key, value in individuals.items():
        # print(key)
        birthString = individuals[key]["BIRT"]
        deathString = individuals[key]["DEAT"]
        # print(birthString, deathString)
        if deathString == 'NA':
            # print(key, "- individual still alive.")
            continue
        elif not(checkDates(birthString, deathString)):
            print("ERROR: US03", key, "- death prior to birth.")
            continue
        else:
            # print(key, "- birth/death dates check.")
            continue


    # US04: Check Marriage before Divorce
    # print()
    # print("S1, US04 - Marriage before Divorce check")
    
    for key, value in families.items():
        #print("Family number:", key)
        marrString = families[key]["MARR"]
        if marrString == "NA":
            # print(key, ": was never married")
            continue

        divorceString = families[key]["DIV"]
        if divorceString == "NA":
            # print(key, ": married and not divorced")
            pass
        else:
            marriageBeforeDivorce(marrString, divorceString)


    # US05: Check Marriage before Death
    # print()
    # print("S1, US05 - Marriage before Death check")
    # print(families)
    for key, value in families.items():
        #print("Family number:", key)

        if families[key]["HUSB"] != "NA":
            husbDeathString = individuals[families[key]["HUSB"]]["DEAT"]
        else:
            husbDeathString = "NA"
        if families[key]["WIFE"] != "NA":
            wifeDeathString = individuals[families[key]["WIFE"]]["DEAT"]
        else:
            wifeDeathString = "NA"
        
        if husbDeathString == "NA" and wifeDeathString == "NA":
            # print(key, ": husband and wife still alive")
            continue

        marrString = families[key]["MARR"]

        if marrString == "NA":
            # print(key, ": was never married")
            continue
        else:
           #print("Family Number:", key, " Marriage Date: ", marrString, " Husband Death: ", husbDeathString, " Wife Death: ", wifeDeathString)
           marriageBeforeDeathCheck(key, marrString, husbDeathString, wifeDeathString)


    # US06: Check if Divorce Date is before Death Date
    # print()
    # print("Sprint 1 US06: Divorce before Death check")
    # print(individuals)
    for key, value in families.items():

        if families[key]["HUSB"] != "NA":
            husbDeathString = individuals[families[key]["HUSB"]]["DEAT"]
        else:
            husbDeathString = "NA"
        if families[key]["WIFE"] != "NA":
            wifeDeathString = individuals[families[key]["WIFE"]]["DEAT"]
        else:
            wifeDeathString = "NA"
        divorceString = families[key]["DIV"]
        if divorceString == 'NA':
            # print(key, "- spouses never divorced.")
            continue
        else:
            # from here goes into function
            # print("Calling func")
            divorceBeforeDeath(key, divorceString, husbDeathString, wifeDeathString)


    # US12: Check if Parents are too old
    # print()
    # print("Sprint 1 US12: Parent/child age check")
    # print(individuals)
    for key, value in families.items():

        if families[key]["HUSB"] != "NA":
            husbBirthString = individuals[families[key]["HUSB"]]["BIRT"]
        else:
            husbBirthString = "NA"
        if families[key]["WIFE"] != "NA":
            wifeBirthString = individuals[families[key]["WIFE"]]["BIRT"]
        else:
            wifeBirthString = "NA"
        #if families[key]["CHIL"] != []:
        childList = families[key]["CHIL"]
        #else:
         #   wifeBirthString = "NA"
        
        if childList == []:
            # print(key, "- no children.")
            continue
        else:
            for i in range(len(childList)):
                if childList[i] not in individuals:
                    continue
                childBirth = individuals[childList[i]]["BIRT"]
                #print("CALLING us12")
                parentChildAgeCheck(key, childBirth, husbBirthString, wifeBirthString)

    # normal spacing is here   


    ### Sprint #2
    # US14 and US16
    # print()
    for key, value in families.items():
       childList = families[key]["CHIL"]
       temp = []
       for item in childList:
           if item not in individuals: # for US26
               continue
           else:
               temp += [item]
       # US14 - multiple births < 5
       CheckMultipleBirths(temp)

       # US16 - Male last name same as fathers
       CheckSameLastNameAsFather(temp)


    # US22:  Unique IDs
    # This check is not useful in our implementation as the dictionary
    # structure requires that the IDs for both individual and family be unique.
    # Therefore must check as read in file.
    # Checked in function "uniqueIDCheck"
    # Stored in IDErrorBuffer and printed here
    # print()
    # print("US22: Unique individual and family ID check done at time of file read.")
    for item in IDErrorBuffer:
        print(item)


    # US24: Unique families by spouse name and marriage date
    # There are two ways to do this check;
    # 1) At the time of reading in the family data, and
    # 2) Parsing the family data at any time after "individuals" and "families" dictionaries are created.
    # I have chosen to implement #2 in this increment.
    uniqueFamilyCheck(families)


    # US25: Unique first names in families (no 2 children have the same name)
    # print()
    # print("Sprint 2 US25: Unique First Names in Families")
    for key, value in families.items():
        childList = families[key]["CHIL"] #get child individual IDs
        temp = []
        for item in childList:
            if item not in individuals:  # for US26
                continue
            else:
                temp += [item]
        checkUniqueChildrenNames(key, individuals, temp)

    # US26: Corresponding entries
    # Make sure everything that appears in the families table is in the individuals table
    # and vice-versa
    # print()
    # print("Sprint 2 US26: Corresponding Entries")
    for key, value in families.items():
        # do stuff
        checkFamToIndi26(key, families, individuals)
    i = 0
    for key, value in individuals.items():
        # do same but different
        checkIndiToFam26(key, families, US26[i])
        i += 1


    ### Sprint 3

    # US34- List large age differences
    # List all couples who were married when the older spouse was more than twice as old as the younger spouse.
    for key, value in families.items():
        # eliminate cases with no marriage date
        marriageDate = families[key]['MARR']
        if marriageDate == 'NA':
            continue
        husbandID = families[key]['HUSB']
        wifeID = families[key]['WIFE']

        husbandAgeDays = ageCalc(individuals[husbandID]['BIRT'], marriageDate)
        wifeAgeDays = ageCalc(individuals[wifeID]['BIRT'], marriageDate)
        # print(husbandAgeDays, wifeAgeDays)

        if husbandAgeDays > (2 * wifeAgeDays):
            print("ERROR: Family: US34:", key,": Husband", husbandID, individuals[husbandID]['NAME'],"was more than twice his wife's age on the date of marriage. (", round(husbandAgeDays/365,1)," to", round(wifeAgeDays/365,1), ") years of age.")

        elif wifeAgeDays > (2 * husbandAgeDays):
            print("ERROR: Family: US34:", key, ": Wife", wifeID, individuals[wifeID]['NAME'],"was more than twice his wife's age on the date of marriage.")


    # US35- List recent births
    # List all people in a GEDCOM file who were born in the last 30 days.
    for key, value in individuals.items():
        ageDays = ageCalc(individuals[key]['BIRT'])
        if ageDays <= 30:
            print("ERROR: Individual: US35:", key, individuals[key]['NAME'], "is less than 30 days old: (",ageDays,") days old.")



except IOError:
    print("An error occured trying to access the data file.")

except ImportError:
    print("No module found.")

except BaseException as e:
    print("Base exception", str(e))

except:
    print("An unknown error occured.")

print()
print()
print()
print()

# for diagnostic purposes
# print(individuals)
# print(families)

# End of File
