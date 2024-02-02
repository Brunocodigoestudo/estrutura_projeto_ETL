from typing import List

import pandas as pd


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    função para transformar uma lista de dataframe em um único dataframe
    """

    return pd.concat(data_frame_list)
