import xlrd

class DoodleXLSImport(object):
    def __init__(self, file_path, row_number_for_dates_in_xls_file):
        workbook = xlrd.open_workbook(file_path)
        self.poll_sheet = workbook.sheet_by_name('Poll')
        self.rowNumberForDatesInXLSFile = row_number_for_dates_in_xls_file
        self.__get_column_names(row_number_for_dates_in_xls_file - 1)
        
    def get_dict_from_xls(self):
        # transform the workbook to a list of dictionaries
        data =[]
        for row_num in range(self.rowNumberForDatesInXLSFile, self.poll_sheet.nrows):
            row_val = self.poll_sheet.row_values(row_num)
            #Function filterout rows?
            if(self.__row_is_valid(row_val)):
                elm = {} 
                for col in range(self.poll_sheet.ncols):
                    elm[self.dict_keys[col]] = self.poll_sheet.cell_value(row_num,col)
                data.append(elm)
        return data
    
    def __get_column_names(self, dates_row_num):
        self.dict_keys = [] # The row_num where we stock the name of the column
        for col in range(self.poll_sheet.ncols):
            column_name = self.poll_sheet.cell_value(dates_row_num, col)
            if('' == column_name):
                column_name = 'Name'
            self.dict_keys.append( column_name )
    
    def __row_is_valid(self, row_val):
        first_column = 0
        second_column = 1
        return row_val[first_column] != 'Comments' and row_val[first_column] != 'Count' and not(row_val[first_column] == '' and row_val[second_column] == '')