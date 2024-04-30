import os
import pandas as pd

class ARQFunctions:
    def __init__(self,directory=None,file_path=None) -> None:
        self.directory = directory,
        self.file_path = file_path

    def obtain_directory_absolute(self,directory=None):
        if directory is None:
            directory = self.directory
        return os.path.abspath(directory)

    def read_CSV_in_diretory(self,directory=None):
        if directory is None:
            directory =  self.directory
        dfs = []
        for arquivo in os.listdir(directory):
            if arquivo.endswith('.CSV') or arquivo.endswith('.csv') or arquivo.endswith('.Csv'):
                caminho_arquivo = os.path.join(directory, arquivo)
                df = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1')
                dfs.append(df)
        return pd.concat(dfs, ignore_index=True);
    
    def read_Excel_in_diretory(self,directory=None):
        if directory is None:
            directory =  self.directory
        dfs = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.xlsx'):
                    file_path = os.path.join(root, file)
                    df = pd.read_excel(file_path)
                    dfs.append(df)
        return pd.concat(dfs, ignore_index=True);

    def read_arq_Excel(self,file_path=None):
        if file_path is None:
            file_path = self.file_path
        return pd.read_excel(file_path)




    
# def read_Excel_in_diretory(directory):
#     dfs = []
#     for arquivo in os.listdir(directory):
#         if arquivo.endswith('.xlsx'):
#             caminho_arquivo = os.path.join(directory, arquivo)
#             df = pd.read_excel(caminho_arquivo)
#             dfs.append(df)
#     return pd.concat(dfs, ignore_index=True)