from typing import List

import pandas as pd

"""
função para transformar uma lista de dataframe em um único dataframe

"""


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list)
