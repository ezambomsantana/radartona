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

radares = pd.read_csv('radares_moto.csv')
radares = radares[radares['contagem'] > 0]
pontos_radares = radares.latitude_l.apply(lambda l: point_from_tuple_str(l))
radares_geodf = gpd.GeoDataFrame(data=radares, geometry=pontos_radares, crs=crs)
radares_geodf = radares_geodf[~radares_geodf.geometry.isnull()]

acidentes = gpd.GeoDataFrame.from_file("../incidentes/SIRGAS_SHP_acidentecet/SIRGAS_SHP_acidentecet.shp", encoding='latin-1')
acidentes = acidentes[acidentes['aci_data'].str.contains('2018', regex=True)]
acidentes.crs = {'init' :'epsg:22523'}
acidentes = acidentes.to_crs({"init": "epsg:4326"})
acidentes_geodf = acidentes[~acidentes.geometry.isnull()]

zonas = gpd.GeoDataFrame.from_file("../data/shapes/Distritos_2017_region.shp", encoding='latin-1')
zonas = zonas.to_crs({"init": "epsg:4326"}) 
zonas['NomeDistri'] = zonas['NomeDistri'].apply(lambda x: unidecode.unidecode(x))

sjoin = gpd.sjoin(zonas, radares_geodf, op='contains')
sjoin_zonas = gpd.sjoin(zonas, acidentes_geodf, op='contains')

print(sjoin)
print(sjoin_zonas)

count = sjoin.groupby('NomeDistri', as_index=True).agg({'cont_motos': 'sum', 'cont_carros': 'sum', 'cont_onibus': 'sum', 'cont_caminhao': 'sum'})
count2 = sjoin_zonas.groupby('NomeDistri', as_index=True).agg({'NomeDistri': 'count'})
count2.columns = ['acidentes']

final = count.join(count2)
print(final)

final = final.fillna(0)
print(final.sort_values(by='acidentes', ascending=False))

print(final.corr())