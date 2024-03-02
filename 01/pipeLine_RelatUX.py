import os
import pandas as pd
import generalFunctions

def generate_all_relatUX():
    directory_relative = 'G:/Drives compartilhados/Ecommerce/Transportes/Indicadores/ARQUIVOS UTILIZADOS/Tabelas/Relatórios/Relatórios UX Fusion/2023-2024/2024/'
    all_relatUx_df = generalFunctions.read_CSV_in_diretory(generalFunctions.obtain_directory_absolute(directory_relative))
    return etl_relatUX(all_relatUx_df)

def etl_relatUX(all_relatUx_df):
    desired_columns_UX = ['CodEntrega','Sro']
    return all_relatUx_df[desired_columns_UX]

