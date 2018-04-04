import xlrd
#import csv
import os
#from collections import defaultdict
#from random import randint

def get_dict_from_xls(excelSheet, rowNumberForDatesInXLSFile):
    WHITESPACE_COUNT = rowNumberForDatesInXLSFile - 1
    workbook = xlrd.open_workbook(excelSheet)
#     workbook = xlrd.open_workbook(excelSheet, on_demand = True)
    worksheet = workbook.sheet_by_name('Poll')
    dict_keys = [] # The row_num where we stock the name of the column
    for col in range(worksheet.ncols):
        dict_keys.append( worksheet.cell_value(WHITESPACE_COUNT,col) )
    
    # transform the workbook to a list of dictionaries
    data =[]
    for row_num in range(WHITESPACE_COUNT + 1, worksheet.nrows):
        row_val = worksheet.row_values(row_num)
        #Function filterout rows?
        if row_val[0] != 'Comments' and row_val[0] != 'Count' and not(row_val[0] == '' and row_val[1] == ''): 
            elm = {} 
            for col in range(worksheet.ncols):
                elm[dict_keys[col]] = worksheet.cell_value(row_num,col)
            data.append(elm)
    return data
    




#	WHITESPACE_COUNT = rowNumberForDatesInXLSFile - 1
#	wb = xlrd.open_workbook(excelSheet)
#    sh = wb.sheet_by_name('Poll')
#    
#    for rownum in range(WHITESPACE_COUNT, sh.nrows):
#            row_num = sh.row_values(rownum)
#            if row_num[0] != 'Comments' and row_num[0] != 'Count' and not(row_num[0] == '' and row_num[1] == ''):
#                spamwriter.writerow(sh.row_values(rownum)) 
    
#	print("Test")
	
	
#def csv_from_excel(excelSheet, rowNumberForDatesInXLSFile):
#    WHITESPACE_COUNT = rowNumberForDatesInXLSFile - 1
#    wb = xlrd.open_workbook(excelSheet)
#    sh = wb.sheet_by_name('Poll')    
#    with open('TheAvailability.csv', 'w', newline='') as csvfile:
#        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#        for rownum in range(WHITESPACE_COUNT, sh.nrows):
#            row_num = sh.row_values(rownum)
#            if row_num[0] != 'Comments' and row_num[0] != 'Count' and not(row_num[0] == '' and row_num[1] == ''):
#                spamwriter.writerow(sh.row_values(rownum))            
#    availabilityList, datesList = retrieveDictionary('TheAvailability.csv')
	
#def retrieveDictionary(filename):
#    listOfCSVDict = list()
#    with open(filename) as f:
#        csv_f = csv.DictReader(f)
#        for thevalue in csv_f:
#            listOfCSVDict.append(thevalue)
#    f.close()
#    return listOfCSVDict, csv_f.fieldnames

if __name__ == "__main__":
    rowNumberForDatesInXLSFile = 5
    csv_from_excel('April18DoodleOutdoor.xls', rowNumberForDatesInXLSFile)
    Schedule()