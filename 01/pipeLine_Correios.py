import os
import pandas as pd
import generalFunctions

def generate_all_correios():
    directory_relative = 'G:/Drives compartilhados/Ecommerce/Transportes/Indicadores/ARQUIVOS UTILIZADOS/Fechamentos de Faturas/Relatórios_Correios/2024/'
    all_correios_df = generalFunctions.read_CSV_in_diretory(generalFunctions.obtain_directory_absolute(directory_relative))
    return etl_correios(all_correios_df)


def etl_correios(all_correios_df):
        desired_columns_Correios = ['Etiqueta','Valor do Servico']
        return all_correios_df[desired_columns_Correios]