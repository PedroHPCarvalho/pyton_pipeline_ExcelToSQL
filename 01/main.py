import os
import pandas as pd
import database
import pipeLine_Correios
import pipeLine_RelatUX
import pipeLine_CadastroP
import pipeLine_ExtratoPedi
from database import DataConnection

#Config DataBase Postgres
HOST = 'localhost'
PORT = '5432'
DBNAME = 'DataBase_Ecomprei'
USER = 'accesspipeline'
PASSWORD = 'Pedro0445'

def main():
    data_connection = DataConnection(HOST,PORT,DBNAME,USER,PASSWORD)
    conn = data_connection.connect_to_postgres()
    # database.create_table_fat_correios(connEstab)
    # database.insert_into_fat_correios(connEstab, pipeLine_Correios.generate_all_correios())
    # # database.insert_into_postgres(conn,'Ux_tracking', pipeLine_RelatUX.generate_all_relatUX())
    # # database.insert_into_postgres(conn,'Cad_products', pipeLine_CadastroP.generate_cadProd())
    # # database.insert_into_postgres(conn,'ExtractPed', pipeLine_ExtratoPedi.generate_all_ExtratPed()
    data_connection.closeConnection()
    ##data_connection.closeConnection()






if __name__ == "__main__":
    main();