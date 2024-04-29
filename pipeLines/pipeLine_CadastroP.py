import os
import pandas as pd
import generalFunctions

def generate_cadProd():
    file_path = 'G:/Drives compartilhados/Ecommerce/Relatórios_Bi/Base/Base_Nova/Produtos/Base_Produtos/SIGEQ230_cad_produtos.xlsx'
    cadProd_df = generalFunctions.read_arq_Excel(file_path)
    return cadProd_df


# def etl_correios(all_correios_df):
#         desired_columns_Correios = ['Etiqueta','Valor do Servico']
#         return all_correios_df[desired_columns_Correios]

def etl_cod_produtos(all_correios_df):
    # Renomear as colunas do DataFrame para corresponder aos nomes das colunas no banco de dados
    all_correios_df.rename(columns={'Etiqueta': 'etiqueta'}, inplace=True)
    
    # Converter os tipos de dados e ajustar valores, se necessário
    all_correios_df['etiqueta'] = all_correios_df['etiqueta'].astype(str)
    all_correios_df['valor_servico'] = all_correios_df['valor_servico'].str.replace('R$', '').str.replace(',', '.').astype(float).round(2)

    # Retornar o DataFrame com as colunas renomeadas e ajustadas
    return all_correios_df