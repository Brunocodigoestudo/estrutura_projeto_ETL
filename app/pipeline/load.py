import os

import pandas as pd


def load_excel(data_frame: pd.DataFrame, output_path: str, file_name: str) -> str:
    """ ""
     Receber dataframe e salvar como excel

     args:
     data_frame (pd.DataFrame): dataframe a ser salvo com excel
     o   utput_path (str): caminho onde o arquivo será salvo
    file_name (str): nomedo arquivo a ser salvo

    return: "Arquivo salvo com sucesso"
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)
    data_frame.to_excel(f"{output_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"
