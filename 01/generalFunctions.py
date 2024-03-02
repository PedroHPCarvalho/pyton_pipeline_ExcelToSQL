import os
import pandas as pd

def obtain_directory_absolute(directory_relative):
    return os.path.abspath(directory_relative)

def read_CSV_in_diretory(directory):
    dfs = []
    for arquivo in os.listdir(directory):
        if arquivo.endswith('.CSV') or arquivo.endswith('.csv') or arquivo.endswith('.Csv'):
            caminho_arquivo = os.path.join(directory, arquivo)
            df = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1')
            dfs.append(df)
    return pd.concat(dfs, ignore_index=True);
    

# def read_Excel_in_diretory(directory):
#     dfs = []
#     for arquivo in os.listdir(directory):
#         if arquivo.endswith('.xlsx'):
#             caminho_arquivo = os.path.join(directory, arquivo)
#             df = pd.read_excel(caminho_arquivo)
#             dfs.append(df)
#     return pd.concat(dfs, ignore_index=True)

def read_Excel_in_diretory(directory):
    dfs = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.xlsx'):
                file_path = os.path.join(root, file)
                df = pd.read_excel(file_path)
                dfs.append(df)
    return pd.concat(dfs, ignore_index=True);

def read_arq_Excel(file_path):
    return pd.read_excel(file_path)

    
