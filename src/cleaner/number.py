import pandas as pd


def numbers(df:pd.DataFrame,col_name):
    cleaned = (
        df[col_name]
            .astype(str)
            .str.strip()
    )
    print(col_name)
    return pd.to_numeric(cleaned,errors="coerce")