import mysql.connector

def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='avatar_rpg_db'
    )
    return conn
