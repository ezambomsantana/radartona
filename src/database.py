import psycopg2 as db


db_user = 'postgres'
db_passwd=''
db_host='localhost'
db_port='5432'
db_name='postgres_db'

try:
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port)#,database=db_name)
    cursor = connection.cursor()
    
    print(connection.get_dsn_parameters(),'\n')
    
    cursor.execute('SELECT version();')
    
    record = cursor.fetchone()
    print('Connected to', record,'\n')
    
except (Exception, db.Error) as error:
    print('Error while connecting to database ',error)
    
finally:
    if(connection):
        cursor.close()
        connection.close()
        print('Db connection is closed')