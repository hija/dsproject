import pandas as pd

def load_bookings():
    """
    This function loads the bookings if the students struggled to load the original dataset.
    Instead of parsing the dataset using, we are going to load the serialized dataset, i.e. a dataset which I have loaded successfully and then serialized.
    """
    return pd.read_pickle("./data/savestate1.pkl")
    