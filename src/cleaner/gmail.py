import pandas as pd 

def Email(df:pd.DataFrame,col_name):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    email = (  
            df[col_name]
            .astype("string")
            .str.strip()
            .str.lower()
            .str.replace(r"@+","@",regex=True)
            .str.replace(r"\s+","",regex=True)
        )

    match = email.str.fullmatch(pattern)
    email = email.where(match)


    return email