import pandas as pd
import regex as re
from .text import text
from .currency import Currency
from .gmail import Email
from .phone_number import Phone
from .rating import Rating
from .link import URL
from .percentage import Percentage
from .date import Date
from .number import numbers
from .duplicate import duplicate
from .id import id
from .name import name 
from .quantity import quantity
from .country import country


function_call = {
    "Currency" : Currency,
    "Email" : Email,
    "Phone" : Phone,
    "URL" : URL,
    "Percentage" : Percentage,
    "Rating" : Rating ,
    "Date"  : Date
}


def cleaner(df:pd.DataFrame,colums_type:dict,report:object):
    col_id = []
    for col_name in report.columns_name:
    
        if colums_type[col_name]["First_type"] == "text":
            df[col_name] = text(df,col_name)

        elif colums_type[col_name]["First_type"] == "name":
            new_cols = name(df,col_name)

            possition = df.columns.get_loc(col_name)

            df  = df.drop(columns=[col_name])  
            
            df.insert(possition,"First Name",new_cols.iloc[:,0])
            df.insert(possition+1,"Last Name",new_cols.iloc[:,1])

            

        elif colums_type[col_name]["First_type"] == "ID":
            col_id.append(col_name)
            df[col_name] = id(df,col_name)

        elif colums_type[col_name]["First_type"] == "number":
            df[col_name] = numbers(df,col_name)

        elif colums_type[col_name]["First_type"] == "quantity":
            df[col_name] = quantity(df,col_name)

        elif colums_type[col_name]["First_type"] == "country":
            df[col_name] = country(df,col_name)
        

        else:
            df[col_name]=function_call[colums_type[col_name]["First_type"]](df,col_name)


    df = duplicate(df,report)
    df = df.dropna(how="all")
    print(col_id)

    df=df.sort_values(
        col_id[0],key=(lambda x : x.str.extract(r"(\d+)")[0].astype(int))
    )

    return df.reset_index(drop=True)