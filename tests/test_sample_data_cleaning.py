# sample_data_cleaning.py
def cleanse_data(df):
    return df.dropna()


# test_sample_data_cleaning.py
import pytest
import pandas as pd
from sample_data_cleaning import cleanse_data


def test_cleanse_data():
    sample_data = pd.DataFrame({"col1": [1, None, 3]})
    expected_data = pd.DataFrame({"col1": [1, 3]})
    cleansed_data = cleanse_data(sample_data)
    pd.testing.assert_frame_equal(cleansed_data, expected_data)
