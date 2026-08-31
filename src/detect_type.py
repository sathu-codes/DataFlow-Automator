import regex as re
import pandas as pd

data_pattern = {
    "Email" : r"^[^\s@]+@[^\s@]+\.[^@\s]+$",
    "Phone" : r"^[+]?\d{5,15}$",
    "URL" : r"^https?://[^\s]+$",
    "Currency" : r"^([\$€£¥]\s)?\d+(?:,\d{3})*(?:\.\d{1,2})?(:?\s[A-Za-z]{3})?$",
    "Percentage" : r"^\d+(?:\.\d+)?%?$"
} 

header_pattern = {
    "Email" : r"\b([eg][\s_-]*)?(mail)(?:[\s_-]*(?:address|id))?\b",
    "Phone" : r"\b(?:tele[\s_-]*)?(?:phone|tele)\b",
    "URL" : r"\b(?:web|link)([\s_-]*(site))?\b",
    "Date" : r"\b(Date)([\s_-]*)?\b",
    "Currency" : r"\b(?:price|amount|cost|total|revenue|salary|balance|currency)([\s_-]*)?\b",
    "Percentage" : r"\b(?:percentage|percent|pct|rate|discount|tax|growth|margin)\b"
}


def detect(report:object ,df:pd.DataFrame):
    result = {}
    value = False
    for col_name in report.columns_name:
        
        for i,(pattern,regex) in enumerate(header_pattern.items()):
           
            if re.search(regex,col_name.lower()):

                data = df[col_name] 

                if pattern == "Phone":
                    data = (
                        df[col_name].astype(str).str.strip().str.replace(r"[\s()-]","",regex=True)
                    )
                
                possible_data=data.astype("string").str.strip().str.match(data_pattern[pattern],na=False).sum()
                percentage = (possible_data/report.rows)*100

                if percentage>60 :
                    print (f"{pattern}  {percentage}%\n")
                    result[col_name]=pattern
                    value = True
                    break

                else :
                    print(f"pattern dosn't matched {col_name}\n")
                    break
            
            else:
                value = False
                continue


        if value == False:
            result[col_name] = report.colums_type[col_name]
            continue
        else:
            continue

    return result