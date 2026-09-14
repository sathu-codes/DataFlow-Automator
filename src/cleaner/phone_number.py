import pandas as pd 

def Phone(df:pd.DataFrame,col_name:str):

    cleaned = (
        df[col_name].astype("string")
        .str.strip()
    )
    
    return cleaned


    #2 5 6 8 10 11 12 13

    