import pandas as pd
import regex as re
from .text import text
from  .currency import Currency
from  .gmail import Email
from  .phone_number import Phone
from  .rating import Rating
from .link import URL
from .percentage import Percentage
from .date import Date
from .number import numbers
from .duplicate import duplicate


function_call = {
    "Currency" : Currency,
    "Email" : Email,
    "Phone" : Phone,
    "URL" : URL,
    "Percentage" : Percentage,
    "Rating" : Rating ,
    "Date" : Date
}
def cleaner(df:pd.DataFrame,colums_type:dict,report:object):
    
    for col_name in report.columns_name:

        if colums_type[col_name] in ("str","object"):
            df[col_name] = text(df,col_name)
        
        elif colums_type[col_name] == "float64" :
            df[col_name]=numbers(df,col_name)

        else:
            df[col_name]=function_call[colums_type[col_name]](df,col_name)


    df = duplicate(df,report)
        
    return df.reset_index(drop=True)