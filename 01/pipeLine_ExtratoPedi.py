import os
import pandas as pd
import generalFunctions

def generate_all_ExtratPed():
    directory_relative = "G:/Drives compartilhados/Ecommerce/Relatórios_Bi/Base/Base_Nova/extrato_pedidos_bseller/2024_extrato"
    all_ExtratPed = generalFunctions.read_Excel_in_diretory(generalFunctions.obtain_directory_absolute(directory_relative))
    return all_ExtratPed