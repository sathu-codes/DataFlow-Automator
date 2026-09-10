import pandas as pd 


def text(df:pd.DataFrame,col_name:str):
    cleaned = (
        df[col_name].str.strip()
        .astype("string")
        .str.replace(r"\s+"," ",regex=True)
        .str.replace(r",","",regex=True)
        .str.lower()
        .str.capitalize()
    )

    return cleaned