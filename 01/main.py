import os
import pandas as pd
import pipeLine_Correios
import pipeLine_RelatUX
import pipeLine_CadastroP
import pipeLine_ExtratoPedi

def main():
    directory_exit_CORREIOS = 'C:/Users/pedro.carvalho/Desktop/arquivo_pipelineEx_correios.xlsx'
    pipeLine_Correios.generate_all_correios().to_excel(directory_exit_CORREIOS, index=False)

    directory_exit_UX = 'C:/Users/pedro.carvalho/Desktop/arquivo_pipelineEx_UX.xlsx'
    pipeLine_RelatUX.generate_all_relatUX().to_excel(directory_exit_UX, index=False)

    directory_exit_CadProd = 'C:/Users/pedro.carvalho/Desktop/arquivo_pipelineEx_CadProd.xlsx'
    pipeLine_CadastroP.generate_cadProd().to_excel(directory_exit_CadProd, index=False)

    directory_exit_ExtratPed = 'C:/Users/pedro.carvalho/Desktop/arquivo_pipelineEx_ExtratPed.xlsx'
    pipeLine_ExtratoPedi.generate_all_ExtratPed().to_excel(directory_exit_ExtratPed, index=False)

if __name__ == "__main__":
    main()