# Importe os módulos necessários
import pandas as pd

from app.pipeline.transform import concat_data_frames


def testar_a_concatenacao_da_lista_de_dataframe():
    """Use o arrange, act e assert para testar a função concat_data_frames"""

    # Arrange
    # Defina ou importe os DataFrames que serão usados nos testes
    df_1 = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
    df_2 = pd.DataFrame({"col1": [5, 6], "col2": [7, 8]})

    data_frame_list = [df_1, df_2]
    data_frame = pd.concat(data_frame_list, ignore_index=True)

    # Act
    df = concat_data_frames(data_frame_list)

    # Assert
    assert df.shape == (4, 2)

    # Redefina os índices
    df.reset_index(drop=True, inplace=True)
    data_frame.reset_index(drop=True, inplace=True)

    # Compare cada elemento individualmente
    for col in df.columns:
        assert all(df[col] == data_frame[col])
