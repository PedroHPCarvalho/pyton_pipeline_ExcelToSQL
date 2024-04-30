import os
import pandas as pd
from Tools.generalFunctions import ARQFunctions

def generate_all_correios():
    directory_relative = 'G:/Drives compartilhados/Ecommerce/Transportes/Indicadores/ARQUIVOS UTILIZADOS/Fechamentos de Faturas/Relatórios_Correios/2024/'
    arq_functions_instance =  ARQFunctions()
    all_correios_df = arq_functions_instance.read_CSV_in_diretory(arq_functions_instance.obtain_directory_absolute(directory_relative))
    return etl_correios(all_correios_df)

def etl_correios(all_correios_df):
    #Renomear colunas
    all_correios_df.rename(columns={'Valor do Servico': 'Valor_servico'}, inplace=True)

    # Selecionar apenas a coluna "Etiqueta" e fazer uma cópia do DataFrame
    select_df = all_correios_df[['Etiqueta', 'Valor_servico']].copy()
    
    # Converter os valores da coluna "Etiqueta" para strings
    select_df['Etiqueta'] = select_df['Etiqueta'].astype(str)
    select_df['Valor_servico'] = select_df['Valor_servico'].str.replace('R$', '').str.replace(',', '.').astype(float)

    return select_df
    

