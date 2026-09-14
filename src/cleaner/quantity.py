import pandas as pd


def quantity(df:pd.DataFrame,col_name:str):
    cleaned = (df[col_name].astype("string")
                .str.strip()
                .str.replace(r"[A-Za-z]" , "" ,regex=True)
                .str.replace(r"[+-]","",regex=True)
                
               )

    return pd.to_numeric(cleaned) 