# from CSVToDict import CSVToDict
# from DoodleXLSImport import DoodleXLSImport

from collections import defaultdict

class AssignmentBuilder(object):
    def __init__(self, availability, mentor_list, assignment_weights):
        self.availability = availability
        self.mentor_list = mentor_list
        self.assignment_weights = assignment_weights
        
        self.initialize_full_dictionary()        
        self.add_to_full_dictionary(self.mentor_list.get_dictionary())
        self.add_to_full_dictionary(self.assignment_weights.get_dictionary())
        
    def get_full_dictionary_list(self):
        return self.full_dictionary
    
    #initialize dictionary to the available dict
    def initialize_full_dictionary(self):
        key = 'Name'
        self.full_dictionary = defaultdict(dict)
        for elem in self.availability.get_dict_from_xls():
            self.full_dictionary[elem[key]].update(elem)
            
    def add_to_full_dictionary(self, dictionary_list):
        key = 'Name'
        for elem in dictionary_list:
            self.full_dictionary[elem[key]].update(elem)      
    
    def _join_dictionaries_on_name(self, dictionaryList1, dictionaryList2, joinType):
        key = 'Name'
        d = defaultdict(dict)
        for elem in dictionaryList1:
            found = False
            d[elem[key]].update(elem)
            for ability in dictionaryList2:
                if elem[key] == ability[key]:
                    
                    d[elem[key]].update(ability)
                    found = True
                    break
            if not found:
                print(elem[key], " was not found in ", joinType, " key = ", key)
                print(elem)
        return d
    
#     def get_column_name
#     
#     def __retrieve_dictionary(self, file_path):
#         self.dictionary_list = list()
#         with open(file_path) as f:
#             csv_f = csv.DictReader(f)
#             for thevalue in csv_f:
#                 self.dictionary_list.append(thevalue)
#         f.close()
#         self.field_Names = csv_f.fieldnames
