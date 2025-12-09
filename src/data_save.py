import csv
import pandas as pd
import os
from datetime import datetime

"""Module to save data to files."""

def save_data(parsed_data: pd.DataFrame, directory="data"):
    """Save parsed data to CSV files based on datetime."""
    # Check if directory exists, create if not
    if not os.path.exists(directory):
        os.makedirs(directory)

    timestamp = parsed_data.index[0]

    if timestamp is None:
        print("No timestamp found in data; cannot save.")
        return
    
    # Save data to CSV files by day
    date_str = timestamp.strftime("%Y-%m-%d")
    filename = f"{directory}/data_{date_str}.csv"
    write_to_csv(filename, parsed_data)

def write_to_csv(filename, parsed_data):
    """Write parsed data to a CSV file."""
    # Check if file exists to write header
    print("Parsed Data: ", parsed_data)
    data_dict = parsed_data.iloc[0].to_dict()
    file_exists = False
    try:
        with open(filename, 'x') as f:
            file_exists = False;
    except FileExistsError:
        file_exists = True; # File already exists
    
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data_dict.keys())
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow({k: v for k, v in data_dict.items()})
        print(f"Data saved to {filename}.")