import pandas as pd

from example_project.config import DATA_DIR


def load_data():
    return pd.read_csv(DATA_DIR / "example.csv", index_col=0)
