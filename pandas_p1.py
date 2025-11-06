import pandas as pd

def read_data(file_path):
    """Reads a CSV file into a pandas DataFrame."""
    csv_df = pd.read_csv(file_path)
    # In order to make it a series, we only read one column of the dataframe. 
    csv_series = csv_df['Is there anything in particular you want to use Python for?']
    return csv_series

def split_count(x):
    """Splits the strings in the series by commas and counts occurrences of each unique item."""
    index = []
    for i in range(len(x)):
        for item in x[i].split(','):
            if item.strip() not in index:
                index.append(item.strip())
    output_df = pd.DataFrame(index=index, columns=['count'])
    for i in range(len(x)):
        for item in x[i].split(','):
            item = item.strip()
            if pd.notna(output_df.at[item, 'count']):
                output_df.at[item, 'count'] = output_df.at[item, 'count'] + 1
            else:
                output_df.at[item, 'count'] = 1
    output_df = output_df.sort_values(by='count', ascending=True)
    return output_df

if __name__ == "__main__":
    file_path = 'survey_data.csv'
    data_series = read_data(file_path)
    print(split_count(data_series))