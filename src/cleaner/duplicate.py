import pandas as pd 
import regex as re

def duplicate(df:pd.DataFrame,report:dict):   

    pattern  = r"^order[\s_-]*id$"
    for col_name in report.columns_name:
        if re.fullmatch(pattern,col_name,flags=re.IGNORECASE):
            non_duplicate = df.drop_duplicates()
            non_duplicate = non_duplicate.drop_duplicates(subset=[col_name],keep="first")
            
            return non_duplicate

    return df.drop_duplicates()