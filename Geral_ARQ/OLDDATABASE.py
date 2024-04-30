import psycopg2

class DataConection:
    def __init__(self,host,port,dbname,user,password) -> None:
        self.host = host
        self.port = port
        self.dbname = dbname
        self.user = user
        self.password = password

    def connect_to_postgres(self):
        try:
            self.conn = psycopg2.connect(
                self.host,
                self.port,
                self.dbname,
                self.user,
                self.password
            )
            print("Conexão bem-sucedida ao banco de dados Postgres")
            return self.conn
        except Exception as e:
            print(r"Erro ao conectar ao banco de dados Postgres")

    def closeConnection(self):
        if self.conn is not None:
            self.conn.close()
            print("Conexão com o banco de dados encerrada")
            self.conn = None            







def insert_into_fat_correios(conn, etiqueta_df):
    # Criar um cursor para executar comandos SQL
    cur = conn.cursor()

      # Iterar sobre os valores da coluna "Etiqueta" e "Valor_servico" e inseri-los na tabela
    for etiqueta, valor_servico in zip(etiqueta_df['Etiqueta'], etiqueta_df['Valor_servico']):
        # Executar a instrução de inserção para cada etiqueta e valor_servico
        cur.execute("INSERT INTO Fat_Correios (Etiqueta, Valor_servico) VALUES (%s, %s)", (etiqueta, valor_servico))

    # Commit para confirmar a transação
    conn.commit()

    # Fechar o cursor
    cur.close()

    







def create_table_fat_correios(conn):
    # Criar um cursor para executar comandos SQL
    cur = conn.cursor()

    # Comando SQL para criar a tabela
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Fat_Correios (
    Etiqueta VARCHAR(255),
    Valor_servico NUMERIC
    );
    '''

    # Executar o comando SQL para criar a tabela
    cur.execute(create_table_query)

    # Commit para confirmar a transação
    conn.commit()

                                                                                                                                                                                                                                     # Fechar o cursor
    cur.close()
    print("tabela Criada")

