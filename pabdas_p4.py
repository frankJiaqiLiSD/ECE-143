import pandas as pd
from pandas.api.types import CategoricalDtype

def read_data(file_path):
    """Reads a CSV file into a pandas DataFrame."""
    csv_df = pd.read_csv(file_path)
    return csv_df

def add_month_yr(x):
    """Adds a 'month-yr' column to the DataFrame based on the 'Timestamp' column."""
    x['Timestamp'] = pd.to_datetime(x['Timestamp'])
    x['month-yr'] = x['Timestamp'].dt.strftime('%b-%Y')
    return x

def fix_categorical(x):
    """
    Ensures 'month-yr' is an ordered CategoricalDtype in chronological order.
    Expects 'Timestamp' and 'month-yr' columns (use add_month_yr first).
    """
    x['Timestamp'] = pd.to_datetime(x['Timestamp'])

    month_order = (
        x.sort_values('Timestamp')['Timestamp']
         .dt.to_period('M')
         .dt.strftime('%b-%Y')
         .drop_duplicates()
         .tolist()
    )

    # Apply ordered categorical dtype
    cat_type = CategoricalDtype(categories=month_order, ordered=True)
    x['month-yr'] = x['month-yr'].astype(cat_type)
    return x

if __name__ == "__main__":
    file_path = 'survey_data.csv'
    data_frame = read_data(file_path)
    add_month_yr(data_frame)
    print(data_frame.groupby('month-yr')['Timestamp'].count().to_frame().sort_index())
