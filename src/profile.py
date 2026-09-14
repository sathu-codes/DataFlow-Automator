import regex as re
import pandas as pd
from email_validator import validate_email,EmailNotValidError



class general:

    def __init__(self):
        self.rows = 0
        self.columns = 0 
        self.columns_name = []
        self.colums_type = {}
        self.missing_data = {}
        self.empty_data = {}
        self.duplicate_row = 0
        self.duplicate_columns = 0
        self.unique_data = {}
        self.memory_usage = 0
        


    def __str__(self):
        return(
            f"Rows: {self.rows}\n"
            f"Columns: {self.columns}\n"
            f"Columns_name: {self.columns_name}\n"
            f"Colums_type: {self.colums_type}\n"
            f"Missing_data: {self.missing_data}\n"
            f"Empty_data: {self.empty_data}\n"
            f"Duplicate_row: {self.duplicate_row}\n"
            f"Duplicate_columns: {self.duplicate_columns}\n"
            f"Unique_data: {self.unique_data}\n"
            f"Memory_usage: {self.memory_usage}\n"
        )


class stats:
    def __init__(self):
        self.count = {}
        self.missing_ratio = {}
        self.unique_count = {}
        self.unique_ratio = {}
        self.length_std = {}
        self.digit_ratio = {}
        self.letter_ratio = {}
        self.whitespace_ratio = {}
        self.special_ratio = {}
        self.deciaml_ratio = {}

    def __str__(self):
        return (
            f"Count: {self.count}\n"
            f"Missing_ratio: {self.missing_ratio}\n"
            f"Unique_count: {self.unique_count}\n"
            f"Unique_ratio: {self.unique_ratio}\n"
            f"Length_std: {self.length_std}\n"
            f"Digit_ratio: {self.digit_ratio}\n"
            f"Letter_ratio: {self.letter_ratio}\n"
            f"Whitespace_ratio: {self.whitespace_ratio}\n"
            f"Special_ratio: {self.special_ratio}\n"
            f"Deciaml_ratio : {self.deciaml_ratio}\n"
        )

#####################################################GEN_REPORT##################################################

    
def general_data(df:pd.DataFrame):
    report = general()

    report.rows = df.shape[0]
    report.columns = df.shape[1]
    report.columns_name = list(df.columns)
    report.colums_type = df.dtypes.astype(str).to_dict()
    report.missing_data = df.isna().sum().to_dict()
    report.duplicate_row = int(df.duplicated().sum())
    report.unique_data = df.nunique(dropna=True).to_dict()
    report.memory_usage = int(df.memory_usage(deep=True).sum())

    for column in df.columns:
        if df[column].dtype == "object":
            empty_count = (
                df[column].notna() & df[column].astype(str).str.strip().eq("")
            ).sum()

        else :
            empty_count = 0

        report.empty_data[column] = int(empty_count)
    

    report.duplicate_columns = int(df.columns.duplicated().sum())

    return report


#####################################################STATS_REPORT##################################################


def stats_data(df:pd.DataFrame):
    stats_data = stats()

    for val in df.columns:
        stats_data.count[val] = len(df[val].dropna())

    for val in df.columns:
        stats_data.missing_ratio[val] = round(float(df[val].isna().mean())*100,2)
    
    for val in df.columns:
        stats_data.unique_count[val] = df[val].nunique()

    for val in df.columns:
        stats_data.unique_ratio[val] = round(float(df[val].nunique()/df[val].count())*100,2)

    for val in df.columns:
        stats_data.length_std[val] = round(float(df[val].dropna().astype(str).str.len().std()),2)

    for val in df.columns:
        value = df[val].dropna().astype("string").str.len()
        stats_data.digit_ratio[val] = round(float((df[val].dropna().astype("string").str.count(r"\d")/value).mean())*100,3)

    for val in df.columns:
        value = df[val].dropna().astype("string").str.len()
        stats_data.letter_ratio[val] = round(float((df[val].dropna().astype("string").str.count(r"[A-Za-z]")/value).mean())*100,3)

    for val in df.columns:
        value = df[val].dropna().astype("string").str.len()
        stats_data.whitespace_ratio[val] = round(float((df[val].dropna().astype("string").str.count(r"\s")/value).mean())*100,3)

    for val in df.columns:
        value = df[val].dropna().astype("string").str.len()
        stats_data.special_ratio[val] = round(float((df[val].dropna().astype("string").str.count(r"[@_+()%$&-]")/value).mean())*100,3)
    
    for val in df.columns:
        value = df[val].dropna().astype("string").str.strip().str.contains(r"\d+\.(?:\d*[1-9]\d*)",regex=True,na=False).mean()*100
        stats_data.deciaml_ratio[val]=round(float(value),3)

    return stats_data


#####################################################REGEX_REPORT##################################################


data_pattern = {

    "ID": r"^[A-Za-z0-9]+[\s_-]?\d{3,15}[\s_\.-]?[A-Za-z0-9]?$",
    "Email":  r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+[@]+[A-Za-z0-9-]+[.,][A-Za-z0-9.-]+$",
    "Phone_number": r"^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?:\s*x(\d+))?\s*$",
    "URL": r"^https?://(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}(?:/[^\s]*)?$",
    "Currency": r"^(?:[€$£¥]\s*)?\d+(?:,\d{3})*(?:\.\d{1,4})?(?:\s+[A-Za-z]{3})?$",
    "Percentage": r"^\d+(?:\.\d+)?%?$",
    "Rating": r"^(?:[1-5](?:\.\d)?)(?:\s+[A-Za-z]+)?$",
    "Date": r"^(?:\d{4}[-/.]\d{1,2}[-/.]\d{1,2}|\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\d{1,2}(?:st|nd|rd|th)?[-/\s.][A-Za-z]{3,9}[-/\s.]\d{2,4}|[A-Za-z]{3,9}[-/\s.]\d{1,2}(?:st|nd|rd|th)?[-/\s.,]+\d{2,4})$"
}

"""header_pattern = {
    "Email" : r"\b([eg][\s_-]*)?(mail)(?:[\s_-]*(?:address|id))?\b",
    "Phone" : r"\b(?:tele[\s_-]*)?(?:phone|tele)\b",
    "URL" : r"\b(?:web|link)([\s_-]*(site))?\b",
    "Currency" : r"\b(?:price|amount|cost|total|revenue|salary|balance|currency)([\s_-]*)?\b",
    "Percentage" : r"\b(?:percentage|percent|pct|rate|discount|tax|growth|margin)\b",
    "Rating" : r"\b(rating)",
    "Date" : r"\b(?:date|day|created|year|updated)\b"
}"""

def regex_data(df:pd.DataFrame,report:object):
    regex_result = {}
    def email_validate(value):
        try:
            validate_email(str(value),check_deliverability=False)
            return True
        except EmailNotValidError :
            return False

    for col_name in report.columns_name:
        data_capsule = {}
        for pattern in data_pattern :
            """if pattern == "Date":
                data = pd.to_datetime(df[col_name],format="mixed",errors="coerce")
                percentage = float(data.notna().mean() * 100)
                data_capsule[pattern] = round(percentage,3)"""
                
            if pattern=="Email":
                data = df[col_name].astype("string").str.strip().str.match(data_pattern["Email"],na=False).sum()
                percentage = float((data/(report.rows-report.duplicate_row))*100)
                data_capsule[pattern] = round(percentage,3)
                #mask = ~df[col_name].astype("string").apply(email_validate)

                #print(df.loc[mask, col_name].to_list())

            else :  
                data = df[col_name].astype("string").str.strip().str.match(data_pattern[pattern],na=False).sum()
                percentage = float((data/report.rows)*100)

                data_capsule[pattern] = round(percentage,3)
                

        #data_capsule[col_name] = {report.colums_type[col_name]}
        regex_result[col_name]= data_capsule
        continue   

    return regex_result
