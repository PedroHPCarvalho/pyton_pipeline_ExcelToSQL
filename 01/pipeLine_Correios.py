import os
import pandas as pd
import generalFunctions

def generate_all_correios():
    directory_relative = 'G:/Drives compartilhados/Ecommerce/Transportes/Indicadores/ARQUIVOS UTILIZADOS/Fechamentos de Faturas/Relatórios_Correios/2024/'
    all_correios_df = generalFunctions.read_CSV_in_diretory(generalFunctions.obtain_directory_absolute(directory_relative))
    return etl_correios(all_correios_df)


def etl_correios(all_correios_df):
        
        desired_columns_Correios = ['Etiqueta','Valor do Servico']
        renamed_columns_Correios = {'Valor do Servico': 'Valor_servico'}

        all_correios_df['Etiqueta'] = all_correios_df['Etiqueta'].astype(str)
        all_correios_df['Valor do Servico'] =  all_correios_df['Valor do Servico'].str.replace('R$','').str.replace(',','.').astype(float).round(2)

        return all_correios_df[desired_columns_Correios].rename(columns=renamed_columns_Correios)
