# test_sample_data_cleaning.py
import pandas as pd


# sample_data_cleaning.py
def cleanse_data(df):
    return df.dropna()


def test_cleanse_data():
    sample_data = pd.DataFrame({"col1": [1, None, 3]})
    expected_data = pd.DataFrame({"col1": [1, 3]})
    cleansed_data = cleanse_data(sample_data)
    pd.testing.assert_frame_equal(cleansed_data, expected_data)
