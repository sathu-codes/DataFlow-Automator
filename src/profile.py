

import pandas as pd




class analizer_report:

    def __init__(self):
        self.rows = 0
        self.columns = 0 
        self.columns_name = []
        self.colums_type = []
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



def analizer(df:pd.DataFrame):
    report = analizer_report()

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

