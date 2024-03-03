import psycopg2

def connect_to_postgres(host,port,dbname,user,password):
    try:
        conn = psycopg2.connect(
            host=host,
            port=port,
            dbname=dbname,
            user=user,
            password=password
        )
        print("Conexão bem-sucedida ao banco de dados Postgres")
        return conn
    except Exception as e:
        print(r"Erro ao conectar ao banco de dados Postgres")

def insert_into_postgres(conn,table_name,df):
    try:
        cur = conn.cursor()
        cols = ','.join(df.columns)
        for idx, row in df.iterrows():
            values = [str(val) for val in row.values]
            sql = f"INSERT INTO {table_name} ({cols}) VALUES ({','.join(values)})"
            cur.execute(sql)
        conn.commit()
        print("Dados inseridos no Postgres com sucesso")
    except Exception as e:
        print(f"Erro ao inserir dados no Postgres: {e}")
    finally:
        cur.close()    