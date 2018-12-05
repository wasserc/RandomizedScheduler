import unittest
from src.CSVToDict import CSVToDict

class CSVToDictTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDictionaryIsCreatedWhenSampleMentorListIsImported(self):
        csvFile = "XLSFiles\\SampleMentorsList.csv"
        importer = CSVToDict(csvFile)
        dict_list = importer.get_dictionary()
        self.assertEqual(len(dict_list), 7)
        self.assertDictEqual(dict_list[0], {'Name': 'Bill', 'Leadership': 'Y', 'Gender': 'M', 'RouteLead': 'Y'})
        self.assertDictEqual(dict_list[1], {'Name': 'Jim', 'Leadership': 'N', 'Gender': 'M', 'RouteLead': 'N'})
        self.assertDictEqual(dict_list[2], {'Name': 'John', 'Leadership': 'Y', 'Gender': 'M', 'RouteLead': 'N'})
        self.assertDictEqual(dict_list[3], {'Name': 'Joe', 'Leadership': 'N', 'Gender': 'M', 'RouteLead': 'Y'})
        self.assertDictEqual(dict_list[4], {'Name': 'Fred', 'Leadership': 'N', 'Gender': 'M', 'RouteLead': 'N'})
        self.assertDictEqual(dict_list[5], {'Name': 'Sarah', 'Leadership': 'N', 'Gender': 'F', 'RouteLead': 'N'})
        self.assertDictEqual(dict_list[6], {'Name': 'Carol', 'Leadership': 'Y', 'Gender': 'F', 'RouteLead': 'Y'})
 
    def testDictionaryIsCreatedWhenSampleMentorWeightsIsImported(self):
        csvFile = "XLSFiles\\SampleMentorWeights.csv"
        importer = CSVToDict(csvFile)
        dict_list = importer.get_dictionary()
        self.assertEqual(len(dict_list), 7)
        self.assertDictEqual(dict_list[0], {'Name': 'Bill', 'Count': '5'})
        self.assertDictEqual(dict_list[1], {'Name': 'Jim', 'Count': '10'})
        self.assertDictEqual(dict_list[2], {'Name': 'John', 'Count': '7'})
        self.assertDictEqual(dict_list[3], {'Name': 'Joe', 'Count': '3'})
        self.assertDictEqual(dict_list[4], {'Name': 'Fred', 'Count': '8'})
        self.assertDictEqual(dict_list[5], {'Name': 'Sarah', 'Count': '12'})
        self.assertDictEqual(dict_list[6], {'Name': 'Carol', 'Count': '2'})
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()