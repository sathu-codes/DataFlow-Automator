import pandas as pd

country_dict = {
    "usa" : "U.S.A",
    "uk" : "U.K",
    "uae" : "UAE"
}
def country(df:pd.DataFrame,col_name:str):
    cleaned  = (df[col_name].astype("string")
                .str.strip()
                .str.replace(r".,-","",regex=True)
                .str.lower()
                )
    cleaned = cleaned.map(country_dict).fillna(cleaned.str.capitalize())

    return cleaned