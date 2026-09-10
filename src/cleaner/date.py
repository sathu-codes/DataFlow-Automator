import pandas as pd 


def Date(df:pd.DataFrame,col_name):
    cleaned = (
        pd.to_datetime(df[col_name],errors="coerce",format="mixed")
    ).astype(str).str.strip()

    return cleaned
     