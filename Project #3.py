#  Class: SSW-555
#  Project:  Project Assignment #3
#  Author: David N. Cohron, Amie Widerkehr, Jeremy Doll
#  Date: 2 June 2017

## Other files:
# My-Family-18-May-2017-411.ged   GEDCOM file for the Brady Family
# CodeOutputProject#3.txt     Output to terminal from this program and input file above

# Honor Code Statement
# We pledge on our honor that we have not given or received any 
# unauthorized assistance on this assignment/examination. 
# We further pledge that we have not copied any material from 
# a book, article, the Internet or any other source except 
# where we have expressly cited the source.
# Signature: Jeremy Doll			Date: 2 June 2017
# Signature: Amie Widerkehr			Date: 2 June 2017
# Signature: David N. Cohron		Date: 2 June 2017

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




# function to get next line and process into list of words
def getWords(dataList):
	line = dataList.pop(0)
	# strip trailing whitespace
	line = line.rstrip()
			
	# split line into words
	wordList = line.split()
	return wordList

# put code into try/except for error handling
try: 

	## Import needed libraries
	import re

	# Define where to find the data file
	path1 = "/Users/Nick/Stevens Institute of Technology/Agile Methods/Project/AgileMethods/My-Family-18-May-2017-411.ged"
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
						# print(wordList)
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
	print(individuals)
	print(families)



	### Output functionality
	# Insert here


except IOError:
	print("An error occured trying to access the data file.")

except ImportError:
	print("No module found.")	

except:
	print("An error occured.")
				
				




# End of File