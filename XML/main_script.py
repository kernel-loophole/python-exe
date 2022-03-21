from dataclasses import replace
from typing_extensions import final
from stringcolor import cs
from random import sample
from matplotlib.pyplot import title
import xlsxwriter as xl
import bs4 as bs
def open_xml_file(filename):
    with open(filename, 'r') as f:
        bs_data=bs.BeautifulSoup(f, 'xml')
    # print(bs_data.find_all('row'))
    # print(bs_data.find_all[("title")::5])
    title_file=bs_data.find('title')
    text_value=bs_data.find("text")
    return title_file,text_value

     
def writer(filename,xml_file):
    filedata,text_value=open_xml_file(xml_file)
    print("file data",filedata)
    print("text value",text_value)
    original_text=text_value.text.split()
    final_string=""
    for i in original_text:
        if i.startswith("#") or i.startswith("@") or i.startswith("$") or i.startswith("!"):
            original_text.remove(i)
            continue
        final_string=final_string+i+" "+i
     
        print(cs("text value","red"),i)
    print(cs("text value","green"),original_text)
    replace_list=['#','@','$','!','R','{','}','[',']','(',')','.','?','!','*','&','%','$','^','~','`','|','\\','<','>','/','+','=','-','_']
    for i in final_string:
        if i in replace_list:
            final_string=final_string.replace(i,"")
    
    print(cs("text value","green"),final_string)
    print(cs("text value","green"),filedata.text)
    try:
        workbook = xl.Workbook(filename)
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0, filedata.text)
        worksheet.write(1, 0, final_string)
        workbook.close()
        print("Success")
    except  e as e:
        print("errror",e) 
if __name__=="__main__":
    writer("sample.xlsx","sample.xml")
    