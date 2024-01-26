import glob
import os
from typing import List
import pandas as pd


def extract_from_excel(input_folder: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(input_folder, "*.xlsx"))

    data_frame_list = [pd.DataFrame]
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)
    return data_frame_list


if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/input")
    print(data_frame_list)
