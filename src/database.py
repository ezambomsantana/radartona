import psycopg2 as db
import

username = 'postgres'
password=''
host='localhost'
port='5432'
database=''

try:
    connection = db.connect(user,password,host,port,database)
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