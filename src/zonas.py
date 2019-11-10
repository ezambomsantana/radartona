import pandas as pd
from shapely.geometry import Point
from functools import partial
import pyproj
from shapely.ops import transform
import geopandas as gpd
import csv
import unidecode

proj_wgs84 = pyproj.Proj(init='epsg:4326')
crs = {'init': 'epsg:4326'}

def point_from_tuple_str(tuple_str):
    try:
        tuple_float = list(map(lambda s: float(s.strip()), tuple_str[1:-1].split(' ')))
        if tuple_float[0] < tuple_float[1]:
            return Point(tuple_float[0], tuple_float[1])
        else:
            return Point(tuple_float[1], tuple_float[0])
    except:
        return None

def point_from_lat_long(linha):
    try:
        return Point(linha['longitude'], linha['latitude'])
    except:
        return None

def calculate_weighted_mean(data):
    data['FE_VIA'] = data['FE_VIA'].apply(lambda x: 1 if math.isnan(x) else x)
    data['FE_VIA'] = data['FE_VIA'].apply(lambda x: 1 if int(x) == 0 else x)
    data['MP'] = data['FE_VIA'] * data['DURACAO']
    data['MP_DIST'] = data['FE_VIA'] * data['DISTANCE']
    return data

radares = pd.read_csv('radares.csv')
radares = radares[radares['contagem'] > 0]
pontos_radares = radares.latitude_l.apply(lambda l: point_from_tuple_str(l))
radares_geodf = gpd.GeoDataFrame(data=radares, geometry=pontos_radares, crs=crs)
radares_geodf = radares_geodf[~radares_geodf.geometry.isnull()]

acidentes = gpd.GeoDataFrame.from_file("../incidentes/SIRGAS_SHP_acidentecet/SIRGAS_SHP_acidentecet.shp", encoding='latin-1')
acidentes.crs = {'init' :'epsg:22523'}
acidentes = acidentes.to_crs({"init": "epsg:4326"})
acidentes_geodf = acidentes[~acidentes.geometry.isnull()]

zonas = gpd.GeoDataFrame.from_file("../data/shapes/Zonas_2017_region.shp", encoding='latin-1')
zonas = zonas.to_crs({"init": "epsg:4326"}) 
zonas['NomeDistri'] = zonas['NomeDistri'].apply(lambda x: unidecode.unidecode(x))
zonas['NomeZona'] = zonas['NomeZona'].apply(lambda x: unidecode.unidecode(x))

sjoin = gpd.sjoin(zonas, radares_geodf, op='contains')
sjoin_zonas = gpd.sjoin(zonas, acidentes_geodf, op='contains')

print(sjoin)
print(sjoin_zonas)




folder_data = "../data/"
arq17 = "dados17_distance.csv"

data17 = pd.read_csv(folder_data + arq17, dtype={'ZONA_O': str, 'ZONA_D': str}, header=0,delimiter=",", low_memory=False) 
data17 = data17.dropna(subset=['CO_O_X'])

data17 = data17.drop(['ID_DOM', 'FE_DOM', 'VIA_BICI','TP_ESTBICI','F_FAM','FE_FAM','FAMILIA','NO_MORAF',
                      'CONDMORA','QT_BANHO','QT_EMPRE','QT_AUTO','QT_MICRO','QT_LAVALOU','QT_GEL1'], axis=1)

csv_file = folder_data + "regioes17.csv"
mydict = []
with open(csv_file, mode='r') as infile:
    reader = csv.reader(infile, delimiter=";")
    mydict = {rows[0]:rows[1] for rows in reader}

csv_file = folder_data + "zonas17.csv"
zonas_nomes = []
with open(csv_file, mode='r') as infile:
    reader = csv.reader(infile, delimiter=";")
    zonas_nomes = {rows[0]:rows[1] for rows in reader}

data17['NOME_O'] = data17['ZONA_O'].apply(lambda x: '' if pd.isnull(x) else mydict[x])
data17['NOME_D'] = data17['ZONA_D'].apply(lambda x: '' if pd.isnull(x) else mydict[x])

data17['ZONA_O'] = data17['ZONA_O'].apply(lambda x: '' if pd.isnull(x) else zonas_nomes[x])
data17['ZONA_D'] = data17['ZONA_D'].apply(lambda x: '' if pd.isnull(x) else zonas_nomes[x])

data17['NUM_TRANS'] = data17[['MODO1', 'MODO2','MODO3','MODO4']].count(axis=1)

data17 = data17[data17['MODOPRIN'] == 13] 
data_renda = data17[['ZONA_O','FE_VIA']].groupby(['ZONA_O']).sum()


count = sjoin.groupby('NomeZona', as_index=True).agg({'contagem': 'sum', 'autuacoes': 'sum'})
count2 = sjoin_zonas.groupby('NomeZona', as_index=True).agg({'NomeDistri': 'count'})


final = count.join(count2).join(data_renda)


final['media'] = final['autuacoes']  / final['contagem'] * 100
final = final.fillna(0)
print(final.sort_values(by='NomeDistri', ascending=False))

print(final.corr())