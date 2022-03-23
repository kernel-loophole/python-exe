
import pandas as pd
import openpyxl as xl
from openpyxl import workbook
from pyspark import Row
from sympy import E
def read_from_workbook(filename):
    wb = xl.load_workbook(filename)
    ws = wb.active
    df = pd.DataFrame(ws)
    return df
def excel_coloring(df,filename):
    wb = xl.load_workbook(filename)
    ws = wb.active
    ws.title = 'Colored'
    
  
def display_data(df):
    print(df.all)
    
def get_column_data(df,column_name):
    return df[column_name]    


    


def make_remove(df,filename):
    count=0
    wb = xl.load_workbook(filename)
    ws = wb.active
    try:
        for i in ws['AL']:
            
            if i.value != None:
                ws.cell(row=i.row, column=i.column).font = xl.styles.Font(bold=True)
                ws.cell(row=i.row, column=i.column).fill = xl.styles.PatternFill(fgColor="8B4513", bgColor="8B4513", fill_type="solid")      
                ws.row_dimensions[i.row].height = 30
            
            else:
                ws.row_dimensions[i.row].height = 12
                ws.cell(row=i.row, column=i.column).value = None
                ws.cell(row=i.row, column=i.column).font = xl.styles.Font(bold=True)
                
                ws.cell(row=i.row, column=i.column).fill = xl.styles.PatternFill(fgColor="FF0000", bgColor="FF0000", fill_type="solid")
        
    except E as e:
        print(e)
    print("following sheets are appended with color")
    print(wb.sheetnames)
    print("file is update")
    print("file is saved")
    wb.save(filename)
def get_index_value(df,column_name):
    return df.index.get_level_values(column_name)

    
def fatch_column_data(df,column_name):
    return df[column_name]

if __name__ == '__main__':
    namefile=input("enter the file name")
    make_remove(read_from_workbook(namefile), namefile)
