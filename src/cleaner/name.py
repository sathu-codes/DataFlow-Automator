import pandas as pd 



def name(df:pd.DataFrame,col_name:str):
    cleaned = (df[col_name]
                .astype("string")
                .str.strip()
                .str.split(r"\s+",n=1,expand=True)
                .apply(lambda col : col.str.strip()
                                       .str.replace(r"[,.`'~()!#$%^&@*-]","",regex=True)
                                       .str.capitalize()
                                    )
               )

    return cleaned

