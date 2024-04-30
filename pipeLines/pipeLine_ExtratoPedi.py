import os
import pandas as pd
from Tools.generalFunctions import ARQFunctions


def generate_all_ExtratPed():
    directory_relative = "G:/Drives compartilhados/Ecommerce/Relatórios_Bi/Base/Base_Nova/extrato_pedidos_bseller/2024_extrato"
    arq_functions_instance = ARQFunctions()
    all_ExtratPed = arq_functions_instance.read_Excel_in_diretory(arq_functions_instance.obtain_directory_absolute(directory_relative))
    return all_ExtratPed