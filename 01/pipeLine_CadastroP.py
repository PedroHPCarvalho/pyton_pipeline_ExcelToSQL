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