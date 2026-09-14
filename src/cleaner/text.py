import pandas as pd 


def text(df:pd.DataFrame,col_name:str):
    cleaned = (
        df[col_name]
        .astype("string")
        .str.strip()
        .str.replace(r"\s+"," ",regex=True)
        .str.replace(r"\s*&\s*"," & ",regex=True)
        .str.replace(r",","",regex=True)
        .str.replace(r"\band\b","&",case=False,regex=True)
        .str.lower()
        .str.capitalize()
    )

    return cleaned