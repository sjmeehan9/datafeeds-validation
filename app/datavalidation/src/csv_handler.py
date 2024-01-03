import os
import pandas as pd

def load_csv(path):
    # Function to load the csv file
    if not os.path.exists(path):
        raise FileNotFoundError(f"File not found: {path}")

    if not os.path.isfile(path):
        raise ValueError(f"Invalid file path: {path}")

    _, file_extension = os.path.splitext(path)
    if file_extension.lower() != ".csv":
        raise ValueError(f"Invalid file format. Expected .csv file: {path}")

    try:
        data = pd.read_csv(path)
        return data
    except (FileNotFoundError, PermissionError) as e:
        raise e
    except UnicodeDecodeError as e:
        raise ValueError("Unable to decode the file. Please ensure it is a valid CSV file.")
    except Exception as e:
        raise ValueError(f"Error occurred while reading the CSV file: {str(e)}")
    
def write_csv(df, path):
    # Function to write the dataframe to a csv file
    try:
        df.to_csv(path, index=False)
    except (FileNotFoundError, PermissionError) as e:
        raise e
    except Exception as e:
        raise ValueError(f"Error occurred while writing the CSV file: {str(e)}")