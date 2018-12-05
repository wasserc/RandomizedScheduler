import unittest
from src.AssignmentBuilder import AssignmentBuilder
from src.DoodleXLSImport import DoodleXLSImport
from src.CSVToDict import CSVToDict

class AssignmentBuilder_test(unittest.TestCase):
    
    def setUp(self):
        self.availability = DoodleXLSImport("_Tests\\XLSFiles\\SimpleDoodle.xls", 5)
        self.mentor_list = CSVToDict("_Tests\\XLSFiles\\SampleMentorsList.csv")
        self.assignment_weights = CSVToDict("_Tests\\XLSFiles\\SampleMentorWeights.csv")
        pass

    def tearDown(self):
        pass

    def testGetListMentorListReturnsDictionaryListWithAvailabilityAndAbilitiesAndWeights(self):
        data_handler = AssignmentBuilder(self.availability, self.mentor_list, self.assignment_weights)
        
        dict_list = data_handler.get_full_dictionary_list()
        self.assertEqual(len(dict_list), 7)
        self.assertDictEqual(dict_list['Bill'], {'Name': 'Bill', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': 'OK', 'Leadership': 'Y', 'Gender': 'M', 'RouteLead': 'Y', 'Count': '5'})
        self.assertDictEqual(dict_list['Jim'], {'Name': 'Jim', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': '', 'Leadership': 'N', 'Gender': 'M', 'RouteLead': 'N', 'Count': '10'})
        self.assertDictEqual(dict_list['John'], {'Name': 'John', 'Sat 7': '', 'Mon 9': 'OK', 'Thu 12': '', 'Sat 14': '', 'Leadership': 'Y', 'Gender': 'M', 'RouteLead': 'N', 'Count': '7'})
        self.assertDictEqual(dict_list['Joe'], {'Name': 'Joe', 'Sat 7': 'OK', 'Mon 9': '', 'Thu 12': 'OK', 'Sat 14': 'OK', 'Leadership': 'N', 'Gender': 'M', 'RouteLead': 'Y', 'Count': '3'})
        self.assertDictEqual(dict_list['Fred'], {'Name': 'Fred', 'Sat 7': 'OK', 'Mon 9': 'OK', 'Thu 12': 'OK', 'Sat 14': 'OK', 'Leadership': 'N', 'Gender': 'M', 'RouteLead': 'N', 'Count': '8'})
        self.assertDictEqual(dict_list['Sarah'], {'Name': 'Sarah', 'Sat 7': 'OK', 'Mon 9': '', 'Thu 12': 'OK', 'Sat 14': '', 'Leadership': 'N', 'Gender': 'F', 'RouteLead': 'N', 'Count': '12'})
        self.assertDictEqual(dict_list['Carol'], {'Name': 'Carol', 'Sat 7': '', 'Mon 9': 'OK', 'Thu 12': 'OK', 'Sat 14': 'OK', 'Leadership': 'Y', 'Gender': 'F', 'RouteLead': 'Y', 'Count': '2'})
 
 
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()