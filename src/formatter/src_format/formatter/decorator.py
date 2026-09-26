import pandas as pd 
from openpyxl.styles import Alignment,Font,PatternFill
from openpyxl import load_workbook

def decorator(file,format_report):
    wb = load_workbook(file)
    ws = wb.active
    
    for intex,rows in enumerate(ws.iter_rows(),start=1):
            for cell in rows:
                cell.alignment = Alignment(
                    horizontal="left",
                    vertical="center"
                )
                if intex==1:
                     cell.fill = PatternFill(
                          fgColor="2F5D50", #1B365D
                          fill_type="solid"
                     )
                     cell.font = Font(
                          name="roboto",
                          size= 12,
                          bold=True
                     )
                else :
                     if intex%2 == 0:
                        cell.fill = PatternFill(
                                fgColor="FFFFFF",
                                fill_type="solid"
                                )
                        
                        cell.font = Font(
                                name="roboto",
                            )
                     else:
                        cell.fill = PatternFill( 
                                fgColor="EAF3E8", #ADD8E6
                                fill_type="solid"
                                )
                        
                        cell.font = Font(
                                name="roboto",
                            )                         

    wb.save(file)