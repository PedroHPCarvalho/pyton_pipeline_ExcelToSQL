import os
import pandas as pd
import pipeLine_Correios
import pipeLine_RelatUX
import pipeLine_CadastroP
import pipeLine_ExtratoPedi
import database

#Config DataBase Postgres
HOST = 'localhost'
PORT = '5432'
DBNAME = 'DataBase_Ecomprei'
USER = 'accesspipeline'
PASSWORD = 'Pedro0445'



def main():
    conn = database.connect_to_postgres(HOST,PORT,DBNAME,USER,PASSWORD)

    database.insert_into_postgres(conn,'Fat_Correios', pipeLine_Correios.generate_all_correios())

    # database.insert_into_postgres(conn,'Ux_tracking', pipeLine_RelatUX.generate_all_relatUX())

    # database.insert_into_postgres(conn,'Cad_products', pipeLine_CadastroP.generate_cadProd())

    # database.insert_into_postgres(conn,'ExtractPed', pipeLine_ExtratoPedi.generate_all_ExtratPed())

    conn.close()

if __name__ == "__main__":
    main()