import pandas as pd

def id(df:pd.DataFrame,col_name:str):
    cleaned = (df[col_name].astype("string")
                .str.replace(r"\.\d+$","",regex=True)
                .str.strip()
               )
    return cleaned