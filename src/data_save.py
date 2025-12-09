import csv

"""Module to save data to files."""

def save_data(parsed_data, directory="data"):
    """Save parsed data to CSV files based on datetime."""
    timestamp = parsed_data.get('Timestamp', None)
    if timestamp is None:
        print("No timestamp found in data; cannot save.")
        return
    
    # Save data to CSV files by day
    date_str = timestamp.strftime("%Y-%m-%d")
    filename = f"{directory}/data_{date_str}.csv"
    write_to_csv(filename, parsed_data)

def write_to_csv(filename, parsed_data):
    """Write parsed data to a CSV file."""
    file_exists = False
    try:
        with open(filename, 'r') as f:
            file_exists = True
    except FileNotFoundError:
        pass

    with open(filename, 'a', newline='') as csvfile:
        fieldnames = parsed_data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerow(parsed_data)
    print(f"Data saved to {filename}")