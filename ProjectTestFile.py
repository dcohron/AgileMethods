#  Class: SSW-555
#  Project:  GEDCOM Project Test Repository
#  Author: David N. Cohron, Amie Widerkehr, Jeremy Doll
#  Date: 02 August 2017

# Testing Project Increments

# Honor Code Statement
# W pledge on our honor that we have not given or received any 
# unauthorized assistance on this assignment/examination. 
# We further pledge that we have not copied any material from 
# a book, article, the Internet or any other source except 
# where we have expressly cited the source.
# Signature: Jeremy Doll            Date: 02 August 2017
# Signature: Amie Widerkehr         Date: 02 August 2017
# Signature: David N. Cohron        Date: 02 August 2017

# References:
# 1) StackOverflow
# 2) PyUnit Tutorial: "Page." PyUnit - Python Wiki. N.p., n.d. Web. 13 June 2017.

import unittest
from Sprint4 import *

class AgileProjectTests(unittest.TestCase):

    def setUp(self):
        # Call before every test case.
        # self.checkdates = checkDates()
        
        self.date1 = ("10MAR1960")
        self.date2 = ("10MAR1970")
        self.emptyDate = "NA"

        self.date3 = ("10MAR1889")
        self.date4 = ("10MAR1899")
        self.date5 = ("10MAR1920")

        # if it breaks change this back
        self.individualsTest = {'I24': {'BIRT': '6FEB1990', 'SEX': 'M', 'NAME': 'Homsar/Runner/', 'DEAT': 'NA'}, 'I5': {'BIRT': '10MAR1955', 'SEX': 'M', 'NAME': 'Greg/Brady/', 'DEAT': 'NA'}, 'I17': {'BIRT': '10MAR2010', 'SEX': 'F', 'NAME': 'Homestar/Runner/', 'DEAT': 'NA'}, 'I8': {'BIRT': '10MAR1956', 'SEX': 'F', 'NAME': 'Marcia/Nelson/', 'DEAT': 'NA'}, 'I1': {'BIRT': '10MAR1940', 'SEX': 'M', 'NAME': 'Mike/Brady/', 'DEAT': 'NA'}, 'I23': {'BIRT': '6FEB1990', 'SEX': 'M', 'NAME': 'Strongsad/Runner/', 'DEAT': 'NA'}, 'I9': {'BIRT': '10MAR1958', 'SEX': 'F', 'NAME': 'Jan/Nelson/', 'DEAT': 'NA'}, 'I10': {'BIRT': '10MAR1960', 'SEX': 'F', 'NAME': 'Cindy/Nelson/', 'DEAT': 'NA'}, 'I19': {'BIRT': '6FEB1990', 'SEX': 'M', 'NAME': 'Strongbad/Runner/', 'DEAT': 'NA'}, 'I7': {'BIRT': '10MAR1960', 'SEX': 'M', 'NAME': 'Bobby/Brady/', 'DEAT': 'NA'}, 'I11': {'BIRT': '5JUL2017', 'SEX': 'M', 'NAME': 'Tiger/Brady/', 'DEAT': 'NA'}, 'I25': {'BIRT': '6FEB1990', 'SEX': 'M', 'NAME': 'Bubs/Runner/', 'DEAT': 'NA'}, 'I6': {'BIRT': '10MAR1950', 'SEX': 'M', 'NAME': 'Peter/Brady/', 'DEAT': 'NA'}, 'I2': {'BIRT': '10MAR1945', 'SEX': 'F', 'NAME': 'Carol/Martin/', 'DEAT': 'NA'}, 'I13': {'BIRT': '10MAR1979', 'SEX': 'M', 'NAME': 'Samuel/Jackson/', 'DEAT': 'NA'}, 'I4': {'BIRT': '10MAR1925', 'SEX': 'F', 'NAME': 'Alice/Nelson/', 'DEAT': 'NA'}, 'I20': {'BIRT': '6FEB1990', 'SEX': 'M', 'NAME': 'Strongbad/Runner/', 'DEAT': 'NA'}, 'I15': {'BIRT': '17JAN1706', 'SEX': 'M', 'NAME': 'Benjamin/Franklin/', 'DEAT': '17APR1790'}, 'I22': {'BIRT': '6FEB1990', 'SEX': 'M', 'NAME': 'Strongmad/Runner/', 'DEAT': 'NA'}, 'I12': {'BIRT': '10MAR1942', 'SEX': 'F', 'NAME': 'Sally/Fields/', 'DEAT': '10MAR1940'}, 'I18': {'BIRT': '1APR1990', 'SEX': 'F', 'NAME': 'Marzipan/Chapman/', 'DEAT': 'NA'}, 'I21': {'BIRT': '6FEB1990', 'SEX': 'NA', 'NAME': 'Cheat/Runner/', 'DEAT': 'NA'}, 'I14': {'BIRT': '30MAR1981', 'SEX': 'F', 'NAME': 'Natashia/Richards/', 'DEAT': '10MAR2012'}, 'I3': {'BIRT': '10MAR1915', 'SEX': 'M', 'NAME': 'Sam/Franklin/', 'DEAT': 'NA'}, 'I16': {'BIRT': '10MAR1800', 'SEX': 'F', 'NAME': 'Deborah/Reed/', 'DEAT': '16JUL2017'}}
        self.familiesTest1 = {'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': [], 'MARR': '10MAR1970', 'DIV': 'NA'}, 'F2': {'HUSB': 'I1', 'WIFE': 'I12', 'CHIL': [], 'MARR': '10MAR1969', 'DIV': 'NA'}, 'F3': {'HUSB': 'I3', 'WIFE': 'I4', 'CHIL': ['I2'], 'MARR': '10MAR1928', 'DIV': 'NA'}, 'F4': {'HUSB': 'I15', 'WIFE': 'I16', 'CHIL': ['I3', 'I17'], 'MARR': '10MAR1990', 'DIV': '10MAR1889'}, 'F5': {'HUSB': 'I1', 'WIFE': 'NA', 'CHIL': ['I5', 'I6', 'I7'], 'MARR': 'NA', 'DIV': 'NA'}, 'F6': {'HUSB': 'NA', 'WIFE': 'I2', 'CHIL': ['I8', 'I9', 'I10'], 'MARR': 'NA', 'DIV': 'NA'}, 'F7': {'HUSB': 'I5', 'WIFE': 'NA', 'CHIL': ['I11'], 'MARR': 'NA', 'DIV': 'NA'}, 'F8': {'HUSB': 'I13', 'WIFE': 'I14', 'CHIL': [], 'MARR': '10MAR2013', 'DIV': '1JAN1980'}}
        self.familiesTest2 = {'F1': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': [], 'MARR': '10MAR1970', 'DIV': 'NA'}, 'F2': {'HUSB': 'I1', 'WIFE': 'I12', 'CHIL': [], 'MARR': '10MAR1969', 'DIV': 'NA'}, 'F3': {'HUSB': 'I3', 'WIFE': 'I4', 'CHIL': ['I2'], 'MARR': '10MAR1928', 'DIV': 'NA'}, 'F4': {'HUSB': 'I15', 'WIFE': 'I16', 'CHIL': ['I3', 'I17'], 'MARR': '10MAR1990', 'DIV': '10MAR1889'}, 'F5': {'HUSB': 'I1', 'WIFE': 'NA', 'CHIL': ['I5', 'I6', 'I7'], 'MARR': 'NA', 'DIV': 'NA'}, 'F6': {'HUSB': 'NA', 'WIFE': 'I2', 'CHIL': ['I8', 'I9', 'I10'], 'MARR': 'NA', 'DIV': 'NA'}, 'F7': {'HUSB': 'I5', 'WIFE': 'NA', 'CHIL': ['I11'], 'MARR': 'NA', 'DIV': 'NA'}, 'F8': {'HUSB': 'I13', 'WIFE': 'I14', 'CHIL': [], 'MARR': '10MAR2013', 'DIV': '1JAN1980'}, 'F9': {'HUSB': 'I17', 'WIFE': 'I18', 'CHIL': ['I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25', 'I90'], 'MARR': 'NA', 'DIV': 'NA'}, 'F10': {'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': [], 'MARR': '10MAR1970', 'DIV': 'NA'}}
        # used in read test only
        self.familiesTest6 = {'F4': {'DIV': '10MAR1889', 'HUSB': 'I15', 'WIFE': 'I16', 'CHIL': ['I3', 'I17'], 'MARR': '10MAR1990'}, 'F7': {'DIV': 'NA', 'HUSB': 'I5', 'WIFE': 'NA', 'CHIL': ['I11'], 'MARR': 'NA'}, 'F1': {'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': [], 'MARR': '10MAR1970'}, 'F5': {'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'NA', 'CHIL': ['I5', 'I6', 'I7'], 'MARR': 'NA'}, 'F8': {'DIV': '1JAN1980', 'HUSB': 'I13', 'WIFE': 'I14', 'CHIL': [], 'MARR': '29AUG2013'}, 'F6': {'DIV': 'NA', 'HUSB': 'NA', 'WIFE': 'I2', 'CHIL': ['I8', 'I9', 'I10'], 'MARR': 'NA'}, 'F10': {'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2', 'CHIL': ['I11', 'I12', 'I13', 'I14', 'I15', 'I16', 'I17', 'I18', 'I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25'], 'MARR': '10MAR1970'}, 'F9': {'DIV': 'NA', 'HUSB': 'I17', 'WIFE': 'I18', 'CHIL': ['I19', 'I20', 'I21', 'I22', 'I23', 'I24', 'I25', 'I90'], 'MARR': 'NA'}, 'F3': {'DIV': 'NA', 'HUSB': 'I3', 'WIFE': 'I4', 'CHIL': ['I2'], 'MARR': '10MAR1928'}, 'F2': {'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I12', 'CHIL': [], 'MARR': '10MAR1969'}}


        #for us25
        self.individualsTest2 = {'I6': {'DEAT': 'NA', 'BIRT': '10MAR1950', 'NAME': 'Peter/Brady/', 'SEX': 'M'}, 'I2': {'DEAT': 'NA', 'BIRT': '10MAR1945', 'NAME': 'Carol/Martin/', 'SEX': 'F'}, 'I1': {'DEAT': 'NA', 'BIRT': '10MAR1940', 'NAME': 'Mike/Brady/', 'SEX': 'M'}, 'I13': {'DEAT': 'NA', 'BIRT': '10MAR1979', 'NAME': 'Samuel/Jackson/', 'SEX': 'M'}, 'I17': {'DEAT': 'NA', 'BIRT': '10MAR1990', 'NAME': 'Homestar/Franklin/', 'SEX': 'M'}, 'I5': {'DEAT': 'NA', 'BIRT': '10MAR1955', 'NAME': 'Peter/Brady/', 'SEX': 'M'}, 'I11': {'DEAT': 'NA', 'BIRT': '10MAR1965', 'NAME': 'Tiger/Brady/', 'SEX': 'M'}, 'I8': {'DEAT': 'NA', 'BIRT': '10MAR1956', 'NAME': 'Marcia/Nelson/', 'SEX': 'F'}, 'I10': {'DEAT': 'NA', 'BIRT': '10MAR1960', 'NAME': 'Cindy/Nelson/', 'SEX': 'F'}, 'I9': {'DEAT': 'NA', 'BIRT': '10MAR1958', 'NAME': 'Jan/Nelson/', 'SEX': 'F'}, 'I14': {'DEAT': '10MAR2012', 'BIRT': '30MAR1981', 'NAME': 'Natashia/Richards/', 'SEX': 'F'}, 'I3': {'DEAT': 'NA', 'BIRT': '10MAR1930', 'NAME': 'Sam/Franklin/', 'SEX': 'M'}, 'I4': {'DEAT': 'NA', 'BIRT': '10MAR1925', 'NAME': 'Alice/Nelson/', 'SEX': 'F'}, 'I7': {'DEAT': 'NA', 'BIRT': '10MAR1960', 'NAME': 'Bobby/Brady/', 'SEX': 'M'}, 'I16': {'DEAT': '10MAR1880', 'BIRT': '10MAR1800', 'NAME': 'Deborah/Reed/', 'SEX': 'F'}, 'I15': {'DEAT': '17APR1790', 'BIRT': '17JAN1706', 'NAME': 'Benjamin/Franklin/', 'SEX': 'M'}, 'I12': {'DEAT': '10MAR1940', 'BIRT': '10MAR1942', 'NAME': 'Sally/Fields/', 'SEX': 'F'}}
        self.familiesTest3 = {'F1': {'MARR': '10MAR1970', 'CHIL': ['I1', 'I2'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2'}, 'F8': {'MARR': '10MAR2013', 'CHIL': ['I13', 'I14'], 'DIV': '1JAN1980', 'HUSB': 'I13', 'WIFE': 'I14'}, 'F9': {'MARR': '10MAR1970', 'CHIL': ['I1', 'I2'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2'}, 'F7': {'MARR': 'NA', 'CHIL': ['I11', 'I5'], 'DIV': 'NA', 'HUSB': 'I5', 'WIFE': 'NA'}, 'F2': {'MARR': '10MAR1969', 'CHIL': ['I1', 'I12'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I12'}, 'F6': {'MARR': 'NA', 'CHIL': ['I8', 'I9', 'I10', 'I2'], 'DIV': 'NA', 'HUSB': 'NA', 'WIFE': 'I2'}, 'F3': {'MARR': '10MAR1928', 'CHIL': ['I2', 'I3', 'I4'], 'DIV': 'NA', 'HUSB': 'I3', 'WIFE': 'I4'}, 'F4': {'MARR': '10MAR1990', 'CHIL': ['I3', 'I17', 'I15', 'I16'], 'DIV': '10MAR1889', 'HUSB': 'I15', 'WIFE': 'I16'}, 'F5': {'MARR': 'NA', 'CHIL': ['I5', 'I6', 'I7', 'I1'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'NA'}}

        #for us26
        self.familiesTest4 = {'F1': {'MARR': '10MAR1970', 'CHIL': ['I1', 'I2'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2'}, 'F8': {'MARR': '10MAR2013', 'CHIL': ['I13', 'I14'], 'DIV': '1JAN1980', 'HUSB': 'I13', 'WIFE': 'I14'}, 'F9': {'MARR': '10MAR1970', 'CHIL': ['I1', 'I2'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2'}, 'F7': {'MARR': 'NA', 'CHIL': ['I11', 'I5'], 'DIV': 'NA', 'HUSB': 'I5', 'WIFE': 'NA'}, 'F2': {'MARR': '10MAR1969', 'CHIL': ['I1', 'I12'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I12'}, 'F6': {'MARR': 'NA', 'CHIL': ['I8', 'I9', 'I10', 'I2'], 'DIV': 'NA', 'HUSB': 'NA', 'WIFE': 'I2'}, 'F3': {'MARR': '10MAR1928', 'CHIL': ['I2', 'I3', 'I4'], 'DIV': 'NA', 'HUSB': 'I3', 'WIFE': 'I4'}, 'F4': {'MARR': '10MAR1990', 'CHIL': ['I3', 'I17', 'I15', 'I16'], 'DIV': '10MAR1889', 'HUSB': 'I15', 'WIFE': 'I16'}, 'F5': {'MARR': 'NA', 'CHIL': ['I5', 'I6', 'I7', 'I1', 'I30'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'NA'}}

        #for us15
        self.familiesTest5 = {'F1': {'MARR': '10MAR1970', 'CHIL': ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15'], 'DIV': 'NA', 'HUSB': 'I1', 'WIFE': 'I2'}}

    def tearDown(self):
        # Call after every test case.
        print("Test complete.")

    def testCompareDate(self):
        # Test case to check date comparison.
         assert checkDates(self.date1, self.date2) == True, "Dates do not check."

    def testReverseCompareDate(self):
        # Test case to check date comparison of reversed.
        assert checkDates(self.date2, self.date1) == False, "Reverse dates do not check."

    def testSameDate(self):
        # Test case to check date comparison of same dates.
        assert checkDates(self.date1, self.date1) == False, "Same dates do not check."    

    def testOffset1(self):
        # Test case to check offset calculation.
        assert checkDates(self.date1, self.date2, 35598) == False, "Offset1 incorrect."

    def testOffset2(self):
        # Test case to check offset calculation.
        assert checkDates(self.date1, self.date2, 10) == True, "Offset2 incorrect."

    def testOffset3(self):
        # Test case to check offset calculation.
        assert checkDates(self.date1, self.date1, -36000) == True, "Offset3 incorrect."

    def testRead(self):
        # test if read is correct
        print()
        print("Testing file read:")
        path = "./My-Family-18-May-2017-411.ged"
        individuals, families = readFile(path)
        self.assertEqual(self.individualsTest, individuals) 
        self.assertEqual(self.familiesTest6, families)

    def testUS04_CheckDivorceAfterMarriage(self):
        print()
        
        # Successful Path: Will be successful:
        print("Testing US04_checkMarriageBeforeDivorce Check:")

        assert marriageBeforeDivorce(self.date1, self.date2) == True, "Marriage: " + self.date1 + " Divorce: " + self.date2        

        # Negative Test Case: Will Fail:
        #print("Testing US04_checkMarriageBeforeDivorce Negative Test Case:")
        #assert marriageBeforeDivorce(self.date2, self.date1) == True, "Marriage: " + self.date2 + " Divorce: " + self.date1

    def testUS05_CheckDeathAfterMarriage(self):
        print()

         # Successful Path: Will be successful:
        print("Testing US05_marriageBeforeDeathCheck:")

        assert marriageBeforeDeathCheck("F1", self.date1, self.date2, self.date2) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.date2
    
        assert marriageBeforeDeathCheck("F1", self.date1, self.date2, self.emptyDate) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.emptyDate

        assert marriageBeforeDeathCheck("F1", self.date1, self.emptyDate, self.date2) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date2

        assert marriageBeforeDeathCheck("F1", self.date1, self.emptyDate, self.emptyDate) == True, "F1: " + "Marriage: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.emptyDate
        
        # Negative Test Case: Will Fail
        
        #print("Testing US05_marriageBeforeDeathCheck Negative Test Case:")

        #assert marriageBeforeDeathCheck("F1", self.date2, self.date1, self.date2) == True, "F1: " + "Marriage: " + self.date2 + " Husband Death: " + self.date1 + " Wife Death: " + self.date2
    
        #assert marriageBeforeDeathCheck("F1", self.date2, self.date1, self.emptyDate) == True, "F1: " + "Marriage: " + self.date2+ " Husband Death: " + self.date1 + " Wife Death: " + self.emptyDate

        #assert marriageBeforeDeathCheck("F1", self.date2, self.emptyDate, self.date1) == True, "F1: " + "Marriage: " + self.date2 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date1

    def testUS06_CheckDivorceBeforeDeath(self):
        print()
        print("Testing US06_divorceBeforeDeath:")

        assert divorceBeforeDeath("F1", self.date1, self.date2, self.date2) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.date2

        assert divorceBeforeDeath("F1", self.date1, self.date2, self.emptyDate) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.date2 + " Wife Death: " + self.emptyDate

        assert divorceBeforeDeath("F1", self.date1, self.emptyDate, self.date2) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date2

        assert divorceBeforeDeath("F1", self.date1, self.emptyDate, self.emptyDate) == True, "F1: " + "Divorce: " + self.date1 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.emptyDate

        # Negative cases

        # assert divorceBeforeDeath("F1", self.date2, self.date1, self.date2) == True, "F1: " + "Divorce: " + self.date2 + " Husband Death: " + self.date1 + " Wife Death: " + self.date2

        # assert divorceBeforeDeath("F1", self.date2, self.date1, self.emptyDate) == True, "F1: " + "Divorce: " + self.date2 + " Husband Death: " + self.date1 + " Wife Death: " + self.emptyDate

        # assert divorceBeforeDeath("F1", self.date2, self.emptyDate, self.date1) == True, "F1: " + "Divorce: " + self.date2 + " Husband Death: " + self.emptyDate + " Wife Death: " + self.date1

    def testUS12_CheckParentsTooOld(self):
        print()
        print("Testing US12_parentChildAgeCheck:")
        #self.date3 = ("10MAR1889")
        #self.date4 = ("10MAR1899")
        #self.date5 = ("10MAR1920")

        assert parentChildAgeCheck("F1", self.date1, self.date5, self.date5) == True, "F1: " + "Child Birth: " + self.date1 + " Father Birth: " + self.date5 + " Mother Birth: " + self.date5
        
        assert parentChildAgeCheck("F1", self.date1, self.date5, self.date4) == False, "F1: " + "Child Birth: " + self.date1 + " Father Birth: " + self.date5 + " Mother Birth: " + self.date4
        
        assert parentChildAgeCheck("F1", self.date2, self.date3, self.date5) == False, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date5
        
        assert parentChildAgeCheck("F1", self.date2, self.date3, self.date4) == False, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date4
       
        #Negative Cases
        # mother 61 years older
        # assert parentChildAgeCheck("F1", self.date1, self.date5, self.date4) == True, "F1: " + "Child Birth: " + self.date1 + " Father Birth: " + self.date5 + " Mother Birth: " + self.date4
        # father 81 years older
        # assert parentChildAgeCheck("F1", self.date2, self.date3, self.date5) == True, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date5
        # both too old 
        # assert parentChildAgeCheck("F1", self.date2, self.date3, self.date4) == True, "F1: " + "Child Birth: " + self.date2 + " Father Birth: " + self.date3 + " Mother Birth: " + self.date4


    def testUS14_CheckMultipleBirths(self):
        # test case to check if multiple births have the same birthday
        print()
        print("Testing US14_multipleBirths:")       
        for key, value in self.familiesTest1.items():
           childList = self.familiesTest1[key]["CHIL"]
           self.assertTrue(CheckMultipleBirths(childList))
           #self.assertFalse(CheckMultipleBirths(childList))
    
    def testUS16_CheckSameLastNameAsFather(self):
        # Test case to check if the last name of child, is same as father
        print()
        print("Testing US16_lastNames:")       
        for key, value in self.familiesTest1.items():
           childList = self.familiesTest1[key]["CHIL"]
           #self.assertTrue(CheckSameLastNameAsFather(childList))

    def testUniqueIDUS22(self):
        # test case to check IndividualID is unique.
        print()
        print("Testing US22_uniqueIDs:")
        self.assertFalse(uniqueIDCheck('I1', individuals))

        # test case to check FamilyID is unique.
        self.assertFalse(uniqueIDCheck('F1', families))

    def testUniqueFamilyUS24(self):
        # test case to check IndividualID is False.
        print()
        print("Testing US24_uniqueFamilies:")
        self.assertFalse(uniqueFamilyCheck(self.familiesTest2))

        # test case to check IndividualID is True.
        self.assertTrue(uniqueFamilyCheck(self.familiesTest1))

    def testUniqueChildrenNames(self):
        # testing US25
        print()
        print("Testing US25_uniqueNames:")
        self.assertFalse(checkUniqueChildrenNames("F5", self.individualsTest2, ["I5", "I6", "I7", "I1"]))
        self.assertTrue(checkUniqueChildrenNames("F1", self.individualsTest2, ["I1", "I2"]))
        self.assertTrue(checkUniqueChildrenNames("F2", self.individualsTest2, []))

    def testCorrespondingIndividuals(self):
        # testing US26 function checkFamToIndi26
        print()
        print("Testing US26_CorrespondingEntries:")
        self.assertTrue(checkFamToIndi26("F5", self.familiesTest4, self.individualsTest2))
        self.assertTrue(checkFamToIndi26("F1", self.familiesTest4, self.individualsTest2))

    def testSortChildrenByAge(self):
        # testing US28 function SortChildrenByAge
        print()
        print("Testing US28_SortChildrenByAge")
        self.assertTrue(SortChildrenByAge("F5", ["I5", "I6", "I7", "I1"]))

    def testMarriedLiving(self):
        # testing US30 function ListMarriedLiving
        print()
        print("Testing US30_List Living and Married:")
        self.assertTrue(ListMarriedLiving("F1"))
        self.assertFalse(ListMarriedLiving("F5"))

    def testOrphan(self):
        print()
        print("Testing US33_orphans")
        self.assertTrue(checkOrphan("F3", self.individualsTest, ["I18"], "I12", "I13"))
        self.assertTrue(checkOrphan("F3", self.individualsTest, ["I18", "I21"], "I12", "I13"))
        self.assertFalse(checkOrphan("F3", self.individualsTest, ["I11", "I18"], "I14", "I15"))

    def testMarriageAge(self):
        # testing US34- large age differences at marriage
        print()
        print("Testing US34_Large age differences at marriage:")
        self.assertTrue(ageCalc("10MAR1965", "10MAR2005") > (2 * ageCalc("10MAR1986", "10MAR2005")))
        self.assertFalse(ageCalc("10MAR1965", "10MAR1985") > (2 * ageCalc("10MAR1965", "10MAR1985")))

    def testNewBirth(self):
        # testing US35- list all births within last 30 days
        print()
        print("Testing US35_List recent births:")
        self.assertTrue(ageCalc("5JUL2017") < 30)
        self.assertFalse(ageCalc("10MAR1965") < 30)

    def testDeath(self):
        # testing US36- list all deaths within last 30 days
        print()
        print("Testing US36_List recent births:")
        self.assertTrue(ageCalc("15JUL2017") < 30)
        self.assertFalse(ageCalc("10MAR1965") < 30)

    def testAge(self):
        # testing US07- check <= 150 years old today (if alive) or at time of death
        print()
        print("Testing US07_Age less than 150:")
        self.assertTrue(ageCalc("10MAR1950") < (150*365))
        self.assertFalse(ageCalc("10MAR1850") < (150*365))

    def testDeceased(self):
        # Testing US29 - List if individual is deceased
        print()
        print("Testing US29 - List of individuals deceased")

        self.assertTrue(ListIfDeceased("I12"))
    
    def test15ChildList(self):
        # Testing US15 - Check if the childlist < 15
        print()
        print("Testing US15 - < than 15 siblings")

        childList = ['I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9', 'I10', 'I11', 'I12', 'I13', 'I14', 'I15']

        self.assertTrue(CheckForChildList(childList))

    def testUpcomingAnniversary(self):
        # Testing US39- Upcoming anniversary (next 30 days)
        print()
        print("Testing US39 - Anniversary in next 30 days")
        self.assertTrue(checkUpcomingAnniversary("F6", "10NOV1986", dt.datetime(2017, 11, 6)))
        self.assertTrue(checkUpcomingAnniversary("F5", "6JAN2001", dt.datetime(2017, 12, 16)))
        self.assertTrue(checkUpcomingAnniversary("F50", "6JAN2001", dt.datetime(2017, 1, 2)))
        self.assertFalse(checkUpcomingAnniversary("F10", "NA", dt.datetime(2017, 11, 6)))
        self.assertFalse(checkUpcomingAnniversary("F1", "31OCT1923", dt.datetime(2017, 11, 6)))

    def testProperRoles(self):
        # Testinf US21- Proper Roles
        # HUSB must be Male
        # Wife must be Female
        print()
        print("Testing US21 - Proper Roles in Marriage")
        self.assertTrue(checkProperRoles("F9", "I2", "F", "WIFE"))
        self.assertTrue(checkProperRoles("F9", "I3", "M", "HUSB"))
        self.assertFalse(checkProperRoles("F10", "I4", "F", "HUSB"))
        self.assertFalse(checkProperRoles("F10", "I5", "M", "WIFE"))

if __name__ == "__main__":

	# run all tests
    unittest.main() 

# End of File
