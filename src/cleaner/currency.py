import pandas as pd
import regex as re

def Currency(df:pd.DataFrame,col_name):
    cleaned = (
        df[col_name].astype(str).fillna('')
        .str.strip()
        .str.replace(r"[$€£¥₹₽¢]","",regex=True)
        .str.replace(r"(?:USD|EUR|GBP|JPY|LKR)","",case=False, regex=True)
    )

    return pd.to_numeric(cleaned,errors="coerce")