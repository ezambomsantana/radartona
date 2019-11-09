import psycopg2 as db
import pandas as pd
import pandas.io.sql as psql

db_user = 'mobilab'
db_passwd='mobilab'
db_host='192.168.167.44'
db_port='5432'
db_name='hackatona'

def count_fluxos():
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_name)
    #df = psql.frame_query("SELECT * FROM test WHERE id > 0", connection)
    df = pd.read_sql_query("SELECT * FROM base_radares", con=connection)
    autuacoes = []
    contagens = []
    for index, row in df.iterrows():

        codigo = row['codigo']
        codigos = codigo.replace(" ","").split("-")

        sum = 0
        for c in codigos:
            df2 = pd.read_sql_query("select sum(contagem) from radar.contagens where localidade = " + c, con=connection)
            
            for index, row in df2.iterrows():
                aut = row['sum']
                if aut is not None:
                    sum = sum + aut

        print('total cont: ' + str(sum))
        autuacoes.append(sum)

        sum = 0
        for c in codigos:
            df2 = pd.read_sql_query("select sum(autuacoes) from radar.contagens where localidade = " + c, con=connection)
            
            for index, row in df2.iterrows():
                aut = row['sum']
                if aut is not None:
                    sum = sum + aut

        print('total aut: ' + str(sum))
        contagens.append(sum)

    df['autuacoes'] = autuacoes
    df['contagem'] = contagens
    df.to_csv('radares.csv',index=False)


def save_contagem():
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_name)
    #df = psql.frame_query("SELECT * FROM contagens", connection)
    df = pd.read_sql_query("SELECT * FROM radar.contagens", con=connection)
    df.to_csv('contagens.csv',index=False)

if __name__ == '__main__':
    count_fluxos()

def get_radares():
    connection = db.connect(user=db_user,password=db_passwd,host=db_host,port=db_port,database=db_name)
    df = pd.read_sql_query("SELECT * FROM base_radares where latitude_l is not null and ligado = 1", con=connection)
    df.to_csv('radares.csv')
    return df

