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

def count_month_yr(x):
    """Counts occurrences of each unique 'month-yr' in the DataFrame."""
    index = x['month-yr']
    output_df = pd.DataFrame(index=index.unique(), columns=['count'])
    for i in index:
        if pd.notna(output_df.at[i, 'count']):
            output_df.at[i, 'count'] = output_df.at[i, 'count'] + 1
        else:
            output_df.at[i, 'count'] = 1
    return output_df.sort_index()

if __name__ == "__main__":
    file_path = 'survey_data.csv'
    data_frame = read_data(file_path)
    add_month_yr(data_frame)
    count_month_yr(data_frame)
    print(data_frame.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())