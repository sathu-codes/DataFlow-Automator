import pandas as pd 


class formater_analizis:
        def __init__(self):
            self.columns_name = []
            self.columns_len = {}

        def __str__(self):
            return(
                f"columns_name : {self.columns_name}\n"
                f"Columns_len : {self.columns_len}\n"
            )
        
def formatter_analizer(df):

    format_report = formater_analizis()

    format_report.columns_name = list(df.columns)

    for col_name in df.columns:
            len = round(float(df[col_name].dropna().astype(str).str.strip().str.len().mean()),2)
            format_report.columns_len[col_name]=len

    return format_report



