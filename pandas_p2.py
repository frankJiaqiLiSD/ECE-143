import pandas as pd

def read_data(file_path):
    """Reads a CSV file into a pandas DataFrame."""
    csv_df = pd.read_csv(file_path)
    return csv_df

def add_month_yr(x):
    """Adds a 'month-yr' column to the DataFrame based on the 'Timestamp' column."""
    x['Timestamp'] = pd.to_datetime(x['Timestamp'])
    x['month-yr'] = x['Timestamp'].dt.strftime('%b-%Y')
    return x

if __name__ == "__main__":
    file_path = 'survey_data.csv'
    data_frame = read_data(file_path)
    print(add_month_yr(data_frame))