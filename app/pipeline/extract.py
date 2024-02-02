"""Esses módulos são para extração de dados"""

import glob
import os
from typing import List

import pandas as pd


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """
    Essa função lê arquivos Excel (.xlsx) de um diretório e cria uma lista de tabelas de dados Pandas,
    onde cada tabela representa os dados de um arquivo Excel diferente.
    """
    all_files = glob.glob(os.path.join(path, '*.xlsx'))

    data_frame_list = []
    for file in all_files:
        data = pd.read_excel(file)
        data_frame_list.append(data)

    return data_frame_list


if __name__ == '__main__':
    data_frame_list = extract_from_excel('data/input')
    print(data_frame_list)

