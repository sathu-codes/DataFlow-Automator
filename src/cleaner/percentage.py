import pandas as pd 

def Percentage(df:pd.DataFrame,col_name:str):

    cleaned = (
        df[col_name].astype("string")
        .str.strip()
        .str.extract(r"^\s*([+-]?\d+(?:\.\d+)?)",expand=False)
    )
    return pd.to_numeric(cleaned)
