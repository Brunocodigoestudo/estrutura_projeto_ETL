import pandas as pd
from typing import List

"""
função para transformar uma lista de dataframe em um único dataframe

"""


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list)
