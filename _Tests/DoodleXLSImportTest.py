import unittest
from DoodleXLSImport import DoodleXLSImport

class DoodleXLSImportTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testDictionaryIsCreatedWhenMentorsAndDateAvailibilityWithoutExcessWhiteSpace(self):
        excelFile = "XLSFiles\\SimpleDoodle.xls"
        datesRowNumber = 5
        importer = DoodleXLSImport(excelFile, datesRowNumber)
        dict_list = importer.get_dict_from_xls()
        self.assertEqual(len(dict_list), 4)
        self.assertDictEqual(dict_list[0], {'Name': 'Jim', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': ''})
        self.assertDictEqual(dict_list[1], {'Name': 'Bill', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': 'OK'})
        self.assertDictEqual(dict_list[2], {'Name': 'Fred', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': 'OK', 'Sat 14': 'OK'})
        self.assertDictEqual(dict_list[3], {'Name': 'Joe', 'Sat 7': 'OK', 'Mon 9': '', 'Thu 12': 'OK', 'Sat 14': 'OK'})

    def testDictionaryIsCreatedWhenDifferentWhitespaceIsPresent(self):
        excelFile = "XLSFiles\\SimpleDoodle2.xls"
        datesRowNumber = 7
        importer = DoodleXLSImport(excelFile, datesRowNumber)
        dict_list = importer.get_dict_from_xls()
        
        self.assertDictEqual(dict_list[0], {'Name': 'Jim', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': ''})
        self.assertDictEqual(dict_list[1], {'Name': 'Bill', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': 'OK'})
        self.assertDictEqual(dict_list[2], {'Name': 'Fred', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': 'OK', 'Sat 14': 'OK'})
        self.assertDictEqual(dict_list[3], {'Name': 'John', 'Sat 7': 'OK', 'Mon 9': '', 'Thu 12': '', 'Sat 14': 'OK'})
        self.assertDictEqual(dict_list[4], {'Name': 'Joe', 'Sat 7': 'OK', 'Mon 9': '', 'Thu 12': 'OK', 'Sat 14': 'OK'})

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()