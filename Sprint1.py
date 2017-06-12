#  Class: SSW-555
#  Project:  Project Assignment #3
#  Author: David N. Cohron, Amie Widerkehr, Jeremy Doll
#  Date: 7 June 2017

## Other files:
# My-Family-18-May-2017-411.ged   GEDCOM file for the Brady Family
# CodeOutputProject#3.txt     Output to terminal from this program and input file above

# Honor Code Statement
# We pledge on our honor that we have not given or received any 
# unauthorized assistance on this assignment/examination. 
# We further pledge that we have not copied any material from 
# a book, article, the Internet or any other source except 
# where we have expressly cited the source.
# Signature: Jeremy Doll			Date: 7 June 2017
# Signature: Amie Widerkehr			Date: 7 June 2017
# Signature: David N. Cohron		Date: 7 June 2017

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
# I will explain here how to work with it, with the following functions as examples.
# So, if you read the paragraph at the bottom about dictionaries, you know that
# they have some properties that make them annoying in some cases. In addition
# to being easier to work with IMO, the data needs to be in list format for ptable.
# To do anything with the data, you need the fields (keys) and data (values), which
# I named the same in functions as when I made them down below for clarity.
# The table printouts are a good visualisation of the data, if you imagine each 
# data row as a sub-list.
# First, find the index of what you want to work with with xxxFields.index(value)
# Now, you have the proper index x to call on xxxData[n][x] to reference what you
# need. 
#
# If you need to check dates, you may need to use the parseDateString function.
# Noth that this returns multiple values, so you need to set multiple variables 
# equal to its output. If you need the current date, use the datetime.date.today
# method. addAge is a good example, as it has both forms of date comparison.
#
# If you wish to add a column to the output table, remember to add the value to 
# xxxData[i] and not just xxxData, and add a header for the column to xxxFields.
#
# Other than that, just be aware of what data types you're working with and keep 
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


# function to test if date2 occurs after date1
# passed two date strings and offset (in days), return boolean
# used to test: birth/death, birth/marriage, marriage/divorce
#               marriage/death, divorce/death, birth date of parents/children
def checkDates(dateString1, dateString2, offsetDays=0):
    dateGood = True
    date1 = dt.datetime.strptime(dateString1, "%d%b%Y")
    date2 = dt.datetime.strptime(dateString2, "%d%b%Y") 
    # print(date1, date2)  
    if (date1 + dt.timedelta(days=offsetDays)) >= date2: 
        dateGood = False
    # print(dateGood)
    return dateGood



# put code into try/except for error handling
try: 
    ## Import needed libraries
    import re
    import datetime as dt
    from dateutil.parser import parse as dtparse
    from prettytable import PrettyTable
    finalp = PrettyTable()
    finalp2 = PrettyTable()

    # Define where to find the data file
    #path1 = "./My-Family-18-May-2017-411.ged"
    path1 = "./My-Family-18-May-2017-411.ged"
    path2 = ""
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
    # read in entire file into list of lines
    f = open(path, 'r')
    data = f.read().splitlines()

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
                    individuals[individualID] = {'NAME':'NA', 'SEX':'NA', 'BIRT':'NA', 'DEAT':'NA'}
                    continue				
                else:
                    familyID = re.sub('@', '', wordList[1])
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
    
    # this output is for development, comment out as necessary
    #print(individuals)
    #print(families)



    ### Output functionality 
    # Some neat facts to know about this for better understanding:
    # Dictionarys in Python are unordered, meaning they do not have an index
    # associated with KV pairs as a list of tuples might. This is why when you
    # run this and print out the dictionaries, they appear in random orders.
    # The keys or values can be converted into a list, in the order that the
    # program stores them. What is weird but also very nice is that the subdictonaries
    # always have the same ordering relative to each other. So as you will see when you
    # run this, the table columns are in different orders each time because dictionaries
    # are unordered, but the data is never gets mixed up because subdictionaries are always
    # relatively the same. The filthy snake language strikes again.

    # We chose as a team to print empty set '[]' instead of 'NA' for table cells with no value.

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
        indiIndexList[i-1] = indi.index(ckey) #set list value to location of that key
    for i in range(1, len(famIndexList) + 1):        
        ckey = "F" + str(i)
        famIndexList[i-1] = fami.index(ckey)

    # Uncomment these for a better visual on what I'm doing
    #print(indi)
    #print(indiIndexList)
    #print(fami)
    #print(famIndexList)

    indFields = ["ID"] + list(indv[indiIndexList[0]].keys())
    indData = []
    famFields = ["ID"] + list(famv[famIndexList[0]].keys())
    famData = []
    # Using those lists, we listify our data (for easier printing) and sort it in one go
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
    # if you get an import error run "pip install -U ptable" in the command line
    # Individual Table

    indFields, indData = addAlive(indFields, indData)
    indFields, indData = addAge(indFields, indData)
    indFields, indData = addChildSpouse(indFields, indData, famFields, famData)

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


    ### Sprint 1:
    # US02: Check Birth before Marriage
    print()
    print("Birth/Marriage check")
    # print(families)
    for key, value in families.items():
        print("Family number:", key)
        marrString = families[key]["MARR"]
        if marrString == "NA":
            print("For family %s no marriage date given." %key)
            continue

        # check husband birthdate
        husband = families[key]["HUSB"]
        husbandBirthString = individuals[husband]["BIRT"]
        if husbandBirthString == "NA":
            print("No husband.")
        elif checkDates(husbandBirthString, marrString):
            print("Husband birth date checks.")
        else:
            print("Husband birth date does not check.")        

        # check wife birthdate
        wife = families[key]["WIFE"]
        wifeBirthString = individuals[wife]["BIRT"]
        if wifeBirthString == "NA":
            print("No wife.")
        elif checkDates(wifeBirthString, marrString):
            print("Wife birth date checks.")
        else:
            print("Wife birth date does not check.")


    # US03: Check Birth before Death
    print()
    print("Birth/Death check")
    # print(individuals)
    for key, value in individuals.items():
        birthString = individuals[key]["BIRT"]
        deathString = individuals[key]["DEAT"]
        # print(birthString, deathString)
        if deathString == 'NA':
            print(key, "- individual still alive.")
            continue
        elif not(checkDates(birthString, deathString)):
            print(key, "- death prior to birth.")
            continue
        else:
            print(key, "- birth/death dates check.")
            continue




except IOError:
    print("An error occured trying to access the data file.")

except ImportError:
    print("No module found.")	

except BaseException as e:
    print("Base exception", str(e))
				
except:
	print("An unknown error occured.")				




# End of File
