import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='102030',
        database='avatar_rpg_db'
    )
    return conn
