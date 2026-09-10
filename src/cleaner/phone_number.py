import pandas as pd 

def Phone(df:pd.DataFrame,col_name:str):

    cleaned = (
        df[col_name].astype("string")
        .str.strip()
        .str.replace(r"[(),_+\-\s]","",regex=True)
    )
    
    return pd.to_numeric(cleaned)