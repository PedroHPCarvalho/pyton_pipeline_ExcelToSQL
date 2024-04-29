import os
import pandas as pd

class GeneralFunctions:
    def __init__(self,directory_relativeire) -> None:
        self.directory_relative = directory_relativeire

    def obtain_directory_absolute(self):
        return os.path.abspath(self.directory_relative)

    def read_CSV_in_diretory(directory):

        dfs = []
        for arquivo in os.listdir(directory):
            if arquivo.endswith('.CSV') or arquivo.endswith('.csv') or arquivo.endswith('.Csv'):
                caminho_arquivo = os.path.join(directory, arquivo)
                df = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1')
                dfs.append(df)
        return pd.concat(dfs, ignore_index=True);
    
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

    
