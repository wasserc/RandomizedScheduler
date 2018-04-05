import xlrd
#import csv
# import os
#from collections import defaultdict
#from random import randint

class DoodleXLSImport(object):
    def __init__(self, file_path, row_number_for_dates_in_xls_file):
        workbook = xlrd.open_workbook(file_path)
        self.poll_sheet = workbook.sheet_by_name('Poll')
        self.rowNumberForDatesInXLSFile = row_number_for_dates_in_xls_file
        self.get_column_names(row_number_for_dates_in_xls_file - 1)
        
        
    def get_column_names(self, dates_row_num):
        self.dict_keys = [] # The row_num where we stock the name of the column
        for col in range(self.poll_sheet.ncols):
            self.dict_keys.append( self.poll_sheet.cell_value(dates_row_num, col) )
        
    def get_dict_from_xls(self):
        # transform the workbook to a list of dictionaries
        data =[]
        for row_num in range(self.rowNumberForDatesInXLSFile, self.poll_sheet.nrows):
            row_val = self.poll_sheet.row_values(row_num)
            #Function filterout rows?
            if row_val[0] != 'Comments' and row_val[0] != 'Count' and not(row_val[0] == '' and row_val[1] == ''): 
                elm = {} 
                for col in range(self.poll_sheet.ncols):
                    elm[self.dict_keys[col]] = self.poll_sheet.cell_value(row_num,col)
                data.append(elm)
        return data
    