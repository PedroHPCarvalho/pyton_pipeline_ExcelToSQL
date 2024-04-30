import psycopg2

class DataConnection:
    def __init__(self,host,port,dbname,user,password) -> None:
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect_to_postgres(self):
        try:
            self.conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            print("Conexão bem-sucedida ao banco de dados Postgres")
            return self.conn
        except Exception as e:
            print("Erro ao conectar ao banco de dados Postgres", e)

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
            print("Conexão com o banco de dados encerrada")
            self.conn = None            




class DDL:
    def __init__(self, conn) -> None:
        self.conn=conn


    def create_initial_table(self):
        # Criar um cursor para executar comandos SQL
        cur = self.conn.cursor()

        # Comando SQL para criar a tabela Fat_Correios
        create_table_query_fat_correios = '''
        CREATE TABLE IF NOT EXISTS Fat_Correios (
        etiqueta VARCHAR(255),
        valor_servico NUMERIC
        );
        '''

        # Comando SQL para criar a tabela Fat_Correios
        create_table_query_cad_products = '''
        CREATE TABLE IF NOT EXISTS Cad_Products (
        sku NUMERIC,
        nome VARCHAR(255),
        departamento VARCHAR(10),
        setor VARCHAR(50),
        familia VARCHAR(50),
        subfamilia VARCHAR(15)
        );
        '''

        create_table_query_extrat_ped = '''
        CREATE TABLE IF NOT EXISTS Extrat_Ped (
        entrega INTEGER,
        data_emissao DATE,
        vl_mercadoria NUMERIC,
        vl_frete_cliente NUMERIC,
        vl_total NUMERIC,
        vl_meio NUMERIC,
        ult_ponto VARCHAR(5),
        sku INTEGER,
        qtd_fat INTEGER
        );
        '''

        create_table_query_relat_ux = '''
        CREATE TABLE IF NOT EXISTS Relat_ux (
        codentrega INTEGER,
        sro VARCHAR(15)
        );
        '''

        # Executar o comando SQL para criar a tabela
        cur.execute(create_table_query_fat_correios)
        cur.execute(create_table_query_cad_products)
        cur.execute(create_table_query_extrat_ped)
        cur.execute(create_table_query_relat_ux)

        # Commit para confirmar a transação
        self.conn.commit()

                                                                                                                                                                                                                                        # Fechar o cursor
        cur.close()
        print("tabelas Primordiais Criadas")




# class DML:





#     def insert_into_fat_correios(conn, etiqueta_df):
#     # Criar um cursor para executar comandos SQL
#     cur = conn.cursor()

#       # Iterar sobre os valores da coluna "Etiqueta" e "Valor_servico" e inseri-los na tabela
#     for etiqueta, valor_servico in zip(etiqueta_df['Etiqueta'], etiqueta_df['Valor_servico']):
#         # Executar a instrução de inserção para cada etiqueta e valor_servico
#         cur.execute("INSERT INTO Fat_Correios (Etiqueta, Valor_servico) VALUES (%s, %s)", (etiqueta, valor_servico))

#     # Commit para confirmar a transação
#     conn.commit()

#     # Fechar o cursor
#     cur.close()

    

#     def insert_into_postgres(conn,table_name,df):
#         try:
#             cur = conn.cursor()
#             cols = ','.join(df.columns)
#             for idx, row in df.iterrows():
#                 values = [str(val) for val in row.values]
#                 sql = f"INSERT INTO {table_name} ({cols}) VALUES ({','.join(values)})"
#                 cur.execute(sql)
#             conn.commit()
#             print("Dados inseridos no Postgres com sucesso")
#         except Exception as e:
#             print(f"Erro ao inserir dados no Postgres: {e}")
#         finally:
#             cur.close()    












