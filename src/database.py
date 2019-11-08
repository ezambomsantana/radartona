import psycopg2 as db
import pandas as pd
import pandas.io.sql as psql

db_user = 'postgres'
db_passwd=''
db_host='localhost'
db_port='5432'
db_name='postgres_db'


def connect_table():
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port)#,database=db_name)
    #df = psql.frame_query("SELECT * FROM test WHERE id > 0", connection)
    df = pd.read_sql_query("SELECT * FROM test WHERE id > 0", con=connection)
    print(df)
        
if __name__ == '__main__':
    connect_table()