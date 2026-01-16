import pandas as pd

from example_project.dataset import load_data


def test_load_data():
    data = load_data()

    assert isinstance(data, pd.DataFrame)
    assert len(data.columns) == 1
