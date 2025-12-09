import os
from datetime import datetime
from data_save import write_to_csv

"""Test data save module."""

def test_save_data_no_timestamp(tmp_path):
    """Test saving data with no timestamp."""
    from data_save import save_data

    parsed_data = {'Wind_angle': 45.0, 'Wind_speed': 10.5}
    directory = tmp_path

    # Should not raise an error
    save_data(parsed_data, directory)
    # Check that no files were created
    assert len(list(tmp_path.iterdir())) == 0

def test_write_to_csv(tmp_path):
    """Test writing data to CSV."""
    parsed_data = {
        'Timestamp': datetime(2024, 6, 1, 12, 0, 0),
        'Wind_angle_deg': 45.0,
        'Wind_speed': 10.5
    }
    directory = tmp_path
    date_str = parsed_data['Timestamp'].strftime("%Y-%m-%d")
    filename = f"{directory}/data_{date_str}.csv"

    write_to_csv(filename, parsed_data)

    # Check that the file was created
    assert os.path.exists(filename)

    # Read back the file and check contents
    with open(filename, 'r') as f:
        lines = f.readlines()
        assert lines[0].strip() == 'Timestamp,Wind_angle_deg,Wind_speed'
        assert lines[1].strip() == '2024-06-01 12:00:00,45.0,10.5'