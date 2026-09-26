import pandas as pd 
from src.formatter.src_format.analizer import formatter_analizer
from src.formatter.src_format.formatter.decorator import decorator
from src.formatter.src_format.formatter.space import space_formater




def format_main():
    file = "/media/sathu/Fewrio1/DataFlow Automator/output/clean_data.xlsx"
    
    df = pd.read_excel("/media/sathu/Fewrio1/DataFlow Automator/output/clean_data.xlsx")  

    format_report = formatter_analizer(df)

    space_formater(file,format_report)
    decorator(file,format_report)


