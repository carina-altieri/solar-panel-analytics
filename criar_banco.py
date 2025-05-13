from db_connection import get_connection

def criar_bd():
    cnx = get_connection()
    cursor = cnx.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS upx")
    cursor.close()
    cnx.close()

    cnx = get_connection(database='upx')
    cursor = cnx.cursor()

    create_table = """
    CREATE TABLE IF NOT EXISTS monitoramento_solar (
        id INT AUTO_INCREMENT PRIMARY KEY, 
        data DATE NOT NULL, 
        hora TIME NOT NULL,
        irradiacao_solar FLOAT, 
        temp_painel FLOAT, 
        temp_ambiente FLOAT, 
        status_painel VARCHAR(50),
        UNIQUE(data, hora)
    )
    """
    cursor.execute(create_table)

    print("Sucesso!")

    cursor.close()
    cnx.close()
