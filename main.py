import pandas as pd
from src.profile import analizer
from src.detect_type import detect



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
        
    except Exception as e :
        print(f"could not read file {e}")


if __name__ == "__main__":
    df = start()
    report = analizer(df)
    colums_type = detect(report,df)

    print(colums_type)