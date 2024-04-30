import os
import pandas as pd
from Tools import database

from PipeLines import pipeLine_Correios
from PipeLines import pipeLine_RelatUX
from PipeLines import pipeLine_CadastroP
from PipeLines import pipeLine_ExtratoPedi


from Tools.database import DataConnection,DDL


#Config DataBase Postgres
HOST = 'localhost'
PORT = '5432'
DBNAME = 'DataBase_Ecomprei'
USER = 'accesspipeline'
PASSWORD = 'Pedro0445'

def main():
    data_connection = DataConnection(HOST,PORT,DBNAME,USER,PASSWORD)
    conn = data_connection.connect_to_postgres()
    ddl_instance = DDL(conn)
    ddl_instance.create_initial_table()
    # database.insert_into_fat_correios(conn, pipeLine_Correios.generate_all_correios())
    # # database.insert_into_postgres(conn,'relat_ux', pipeLine_RelatUX.generate_all_relatUX())
    # # database.insert_into_postgres(conn,'Cad_products', pipeLine_CadastroP.generate_cadProd())
    # # database.insert_into_postgres(conn,'ExtractPed', pipeLine_ExtratoPedi.generate_all_ExtratPed())
    data_connection.closeConnection()






if __name__ == "__main__":
    main();