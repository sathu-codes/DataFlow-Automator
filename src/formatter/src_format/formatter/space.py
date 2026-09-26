import pandas as pd 
from openpyxl import load_workbook
from openpyxl.styles import Font,PatternFill,Alignment
from openpyxl.utils import get_column_letter

def space_formater(file,gen_report:object):

    wb = load_workbook(file)
    ws = wb.active

    for intex,col_name in enumerate(gen_report.columns_name,start=1):

        col_letter = get_column_letter(intex)
            
        col_name_len = len(col_name)
        col_data_avg_len = gen_report.columns_len[col_name]
        
        final_col_width = max(col_name_len,col_data_avg_len)

        """if col_name=="Email":
            print(col_data_avg_len)
            print(final_col_width)"""

        ws.column_dimensions[col_letter].width = final_col_width+9
        ws.row_dimensions[1].height = 25

    wb.save(file)


    
    return  0


