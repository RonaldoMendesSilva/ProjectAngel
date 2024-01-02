import mysql.connector
print("Executing database.py")

def get_naturezas():
    connection = mysql.connector.connect(
        host="localhost",
        port = 8080,
        user="root",
        password="Rioverde1",
        database="mydb"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT id, nome FROM natureza")
    naturezas = cursor.fetchall()
    cursor.close()
    connection.close()
    return naturezas

def get_naturezas_from_database(connection, tabela='natureza'):
    """
    Obtém as naturezas da tabela especificada no banco de dados.

    Parameters:
    - connection: Conexão com o banco de dados.
    - tabela: Nome da tabela a ser consultada (padrão: 'natureza').

    Returns:
    - Lista de naturezas da tabela especificada.
    """
    try:
        with connection.cursor() as cursor:
            # Modifique a consulta para selecionar apenas da tabela especificada
            query = f"SELECT * FROM {tabela}"
            cursor.execute(query)
            naturezas = cursor.fetchall()
            return naturezas
    except Exception as e:
        # Lidar com exceções de consulta de banco de dados conforme necessário
        raise e

def escape(text):
    return text.replace("'", "\\'")

def insert_natureza(connection, nome, descricao, status_nat):
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO natureza (nome, descricao, status_nat) VALUES (%s, %s, %s)",
        (nome, descricao, status_nat)
    )

    connection.commit()
    cursor.close()

def cadastrar_ocorrencia(data):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="rioverde"
    )
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO ocorrencia (Bombeiro, guarnicao, endereco_ocorr, bairro_ocorr, municipio_ocorr, status, custodia_id_custodia, unid_saude_id_unid_saude, natureza_id_natureza, usuario_id_usuario, usuario_cadvit_pessoa_id, usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos, usuario_guarnicao_id_guarnicao)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (data["Bombeiro"], data["guarnicao"], data["endereco_ocorr"], data["bairro_ocorr"], data["municipio_ocorr"], data["status"], data["custodia_id_custodia"], data["unid_saude_id_unid_saude"], data["natureza_id_natureza"], data["usuario_id_usuario"], data["usuario_cadvit_pessoa_id"], data["usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos"], data["usuario_guarnicao_id_guarnicao"])
    )

    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    naturezas = get_naturezas()

    ocorrencia = {
        "Bombeiro": "Bombeiro 1",
        "guarnicao": "Guarnição 1",
        "endereco_ocorr": "Rua das Flores, 123",
        "bairro_ocorr": "Centro",
        "municipio_ocorr": "Rio Verde",
        "status": "Em andamento",
        "custodia_id_custodia": 1,
        "unid_saude_id_unid_saude": 1,
        "natureza_id_natureza": naturezas[0][0],
        "usuario_id_usuario": 1,
        "usuario_cadvit_pessoa_id": 1,
        "usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos": 1,
        "usuario_guarnicao_id_guarnicao": 1
    }

    cadastrar_ocorrencia(ocorrencia)

def connect():
    # Substitua com suas configurações de banco de dados
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="Rioverde1",
        database="mydb"
    )
    return connection

def create_tables(connection):
    cursor = connection.cursor()

    # Comandos SQL para criar tabelas
    create_ocorrencia_table_query = """
    CREATE TABLE IF NOT EXISTS ocorrencia (
        Bombeiro VARCHAR(255) NOT NULL,
        guarnicao VARCHAR(255) NOT NULL,
        endereco_ocorr VARCHAR(255) NOT NULL,
        bairro_ocorr VARCHAR(255) NOT NULL,
        municipio_ocorr VARCHAR(255) NOT NULL,
        status VARCHAR(255) NOT NULL,
        custodia_id_custodia INT,
        unid_saude_id_unid_saude INT,
        natureza_id_natureza INT,
        usuario_id_usuario INT,
        usuario_cadvit_pessoa_id INT,
        usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos INT,
        usuario_guarnicao_id_guarnicao INT,
        PRIMARY KEY (Bombeiro, guarnicao),
        INDEX idx_Bombeiro (Bombeiro),
        INDEX idx_guarnicao (guarnicao)
    );
    """

    # Execute o comando SQL para criar a tabela 'ocorrencia'
    cursor.execute(create_ocorrencia_table_query)

    # Commit para aplicar as alterações no banco de dados
    connection.commit()

    # Feche o cursor
    cursor.close()

# Exemplo de utilização
if __name__ == "__main__":
    # Conectar ao banco de dados
    db_connection = connect()

    # Criar tabelas
    create_tables(db_connection)

    # Fechar a conexão com o banco de dados
    db_connection.close()

# Adicione funções semelhantes para outras tabelas
def insert_custodia(connection, data):
    cursor = connection.cursor()
    insert_custodia_query = """
    INSERT INTO custodia (name, cpf_cnpj, orgao_expd, telefone_cust, municipio_cust, bairrocust, estado_cust)
    VALUES (%(name)s, %(cpf_cnpj)s, %(orgao_expd)s, %(telefone_cust)s, %(municipio_cust)s, %(bairrocust)s, %(estado_cust)s);
    """
    cursor.execute(insert_custodia_query, data)
    connection.commit()
    cursor.close()

def insert_unid_saude(connection, data):
    cursor = connection.cursor()
    insert_unid_saude_query = """
    INSERT INTO unid_saude (unida_saude, endereco, complemento, municipio, numero, uf_unid, bairro_unid, telefone_unid)
    VALUES (%(unida_saude)s, %(endereco)s, %(complemento)s, %(municipio)s, %(numero)s, %(uf_unid)s, %(bairro_unid)s, %(telefone_unid)s);
    """
    cursor.execute(insert_unid_saude_query, data)
    connection.commit()
    cursor.close()

def insert_ocorrencia(connection, data):
    cursor = connection.cursor()

    # Verificar se o registro já existe
    check_query = "SELECT COUNT(*) FROM ocorrencia WHERE Bombeiro = %s AND guarnicao = %s"
    cursor.execute(check_query, (data['Bombeiro'], data['guarnicao']))
    if cursor.fetchone()[0] > 0:
        # Registro já existe, trate conforme necessário
        raise ValueError("Ocorrência já cadastrada para Bombeiro e Guarnição específicos.")

    try:
        # Tentar inserir o registro
        insert_ocorrencia_query = """
        INSERT INTO ocorrencia (Bombeiro, guarnicao, endereco_ocorr, bairro_ocorr, municipio_ocorr, status, custodia_id_custodia, unid_saude_id_unid_saude, natureza_id_natureza, usuario_id_usuario, usuario_cadvit_pessoa_id, usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos, usuario_guarnicao_id_guarnicao)
        VALUES (%(Bombeiro)s, %(guarnicao)s, %(endereco_ocorr)s, %(bairro_ocorr)s, %(municipio_ocorr)s, %(status)s, %(custodia_id_custodia)s, %(unid_saude_id_unid_saude)s, %(natureza_id_natureza)s, %(usuario_id_usuario)s, %(usuario_cadvit_pessoa_id)s, %(usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos)s, %(usuario_guarnicao_id_guarnicao)s);
        """
        cursor.execute(insert_ocorrencia_query, data)
        connection.commit()
    except mysql.connector.Error as err:
        # Tratar a exceção de chave duplicada
        if err.errno == 1062:
            raise ValueError("Ocorrência já cadastrada para Bombeiro e Guarnição específicos.")
        else:
            raise
    finally:
        cursor.close()

def ocorrencia_existe(connection, bombeiro, guarnicao):
    cursor = connection.cursor()

    try:
        # Verificar se o registro já existe
        check_query = "SELECT EXISTS (SELECT 1 FROM ocorrencia WHERE Bombeiro = %s AND guarnicao = %s)"
        cursor.execute(check_query, (bombeiro, guarnicao))
        return cursor.fetchone()[0] > 0

    finally:
        cursor.close()

def get_naturezas(connection):
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, nome FROM natureza")
    naturezas = cursor.fetchall()
    cursor.close()
    return naturezas

# Exemplo de utilização
if __name__ == "__main__":
    # Conectar ao banco de dados
    db_connection = connect()

    # Criar tabelas
    create_tables(db_connection)

    # Exemplo de dados para inserção na tabela 'ocorrencia'
    ocorrencia_data = {
        'Bombeiro': 'Nome do Bombeiro',
        'guarnicao': 'Nome da Guarnição',
        'endereco_ocorr': 'Endereço da Ocorrência',
        'bairro_ocorr': 'Bairro da Ocorrência',
        'municipio_ocorr': 'Cidade da Ocorrência',
        'status': 'Em andamento',
        'custodia_id_custodia': 1,  # Substitua pelo ID válido da tabela custodia
        'unid_saude_id_unid_saude': 1,  # Substitua pelo ID válido da tabela unid_saude
        'natureza_id_natureza': 1,  # Substitua pelo ID válido da tabela natureza
        'usuario_id_usuario': 1,  # Substitua pelo ID válido da tabela usuario
        'usuario_cadvit_pessoa_id': 1,  # Substitua pelo ID válido da tabela cadvit_pessoa
        'usuario_cadvit_pessoa_envolvidos_ocorr_id_envolvidos': 1,  # Substitua pelo ID válido da tabela envolvidos_ocorr
        'usuario_guarnicao_id_guarnicao': 1  # Substitua pelo ID válido da tabela guarnicao
    }

    # Inserir dados na tabela 'ocorrencia'
    insert_ocorrencia(db_connection, ocorrencia_data)

    # Fechar a conexão com o banco de dados
    db_connection.close()

def insert_vitima(connection, data):
    cursor = connection.cursor()
    insert_vitima_query = """
    INSERT INTO vitima (nome, idade, endereco, telefone, sexo)
    VALUES (%(nome)s, %(idade)s, %(endereco)s, %(telefone)s, %(sexo)s);
    """
    cursor.execute(insert_vitima_query, data)
    connection.commit()
    cursor.close()

# Exemplo de utilização
if __name__ == "__main__":
    # Conectar ao banco de dados
    db_connection = connect()

    # Criar tabelas
    create_tables(db_connection)

    # Exemplo de dados para inserção na tabela 'custodia'
    custodia_data = {
        'name': 'Nome da Custódia',
        'cpf_cnpj': '12345678901',
        'orgao_expd': 'SSP',
        'telefone_cust': '123456789',
        'municipio_cust': 'Cidade',
        'bairrocust': 'Bairro',
        'estado_cust': 'UF'
    }

    # Inserir dados na tabela 'custodia'
    insert_custodia(db_connection, custodia_data)

    # Exemplo de dados para inserção na tabela 'unid_saude'
    unid_saude_data = {
        'unida_saude': 'Nome da Unidade de Saúde',
        'endereco': 'Endereço da Unidade de Saúde',
        'complemento': 'Complemento',
        'municipio': 'Cidade',
        'numero': '123',
        'uf_unid': 'UF',
        'bairro_unid': 'Bairro',
        'telefone_unid': '987654321'
    }

    # Inserir dados na tabela 'unid_saude'
    insert_unid_saude(db_connection, unid_saude_data)

    # Fechar a conexão com o banco de dados
    db_connection.close()

