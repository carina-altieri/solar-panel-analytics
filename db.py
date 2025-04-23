import mysql.connector
from config import MYSQL_PASSWORD

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1", 
        user="root", 
        password=MYSQL_PASSWORD,
        database="upx"
    )