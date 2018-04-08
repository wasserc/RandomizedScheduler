import csv

class CSVToDict(object):
    def __init__(self, file_path):
        self.file_path = file_path
        self.__retrieve_dictionary(file_path)
        
    def get_dictionary(self):
        return self.dictionary_list
    
#     def get_column_name
    
    def __retrieve_dictionary(self, file_path):
        self.dictionary_list = list()
        with open(file_path) as f:
            csv_f = csv.DictReader(f)
            for thevalue in csv_f:
                self.dictionary_list.append(thevalue)
        f.close()
        self.field_Names = csv_f.fieldnames
