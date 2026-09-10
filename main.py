import pandas as pd
from src import profile
from src import detect_type
from src.cleaner.cleaner import cleaner


def start():
    try:
        df = pd.read_excel("input/messy_data.xlsx")
        return df

    except ImportError:
        print("Required Excel library is missing.")

    except FileNotFoundError:
        print("file not found or wrong file name.")

    except PermissionError:
        print("Permission denied.")

    except Exception as e:
        print(f"could not read file {e}")


if __name__ == "__main__":
    df = start()

    stats_report = profile.stats_data(df)
    gen_report = profile.general_data(df)
    regex_report = profile.regex_data(df, gen_report)

    stat_dict = detect_type.dict_make(stats_report, gen_report,regex_report)
    print(stat_dict)

    #print(regex_report)
    """
    final_df = cleaner(df,colums_type,report)
    output_path = "output/clean_data.xlsx"

    final_df.to_csv(output_path,index=False)"""
