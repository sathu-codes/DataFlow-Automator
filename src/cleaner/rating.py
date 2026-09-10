import pandas as pd 

def Rating(df:pd.DataFrame,col_name):

    cleaned = (
        df[col_name].astype("string")
        .str.extract(r"^\s*([+-]?\d+(?:\.\d+)?)",expand=False)
        .str.strip()
    )
    return pd.to_numeric(cleaned)
