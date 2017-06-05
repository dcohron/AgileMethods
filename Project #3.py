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

def getLine(dataList):
	line = dataList.pop(0)
	return line

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
	tagInterest = ["NAME", "SEX", "BIRT", "DEAT", "CHIL", "HUSB", "WIFE", "MARR"]
	tagList = tagInterest
	
	# declare empty dictionary as primary data structure
	individuals = {}

	# read in entire file into list of lines
	f = open(path, 'r')
	data = f.read().splitlines()

	# remove empty lines from list of lines
	data = list(filter(None, data))
	
		
	for line in data:
		print(line)
		
		# skips leading comments and any line that does not 
		# start with a number
		if line[0].isdigit():
			# strip trailing whitespace
			line = line.rstrip()
			
			# split line into words
			wordList = line.split()
			print (wordList)
			# print(len(wordList))
			remainder = ''.join(str(w + " ") for w in wordList[2:])
			# if word is in the list of tags, add to dictionary
			if wordList[0] == '1' and wordList[1] in tagList:
				individuals[id][wordList[1]] = remainder
				
			# if tag in word 3 is one of two special tags, handle it	
			elif len(wordList) > 2 and (wordList[2] == "INDI" or wordList[2] == "FAM"):
				if wordList[2] == "INDI":
					individualID = re.sub('@', '', wordList[1])
					print(individualID)
					individuals[individualID] = {'NAME':'NA', 'SEX':'NA', 'BIRT':'NA', 'DEAT':'NA', 'CHIL':'NA', 'HUSB':'NA', 'WIFE':'NA', 'MARR':'NA'}
					print(individuals)
				else:
					famID = re.sub('@', '', wordList[1])
					print("FamilyID= ", famID)	
			
			# otherwise, invalid tag
			else:
				print("Tag not of interest- skipping to next line")

		else:
			continue

except IOError:
	print("An error occured trying to access the data file.")

except ImportError:
	print("No module found.")	

except:
	print("An error occured.")
				
				




# End of File