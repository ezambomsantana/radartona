# -*- coding: utf-8 -*-
import geopandas as gpd
import numpy as np
import pandas as pd
import csv
import unidecode
import math
import shapefile
import utm
from shapely.geometry import shape, LineString, Polygon
import math


csv_incidentes = "../incidentes/acidentes.csv"

acidentes = pd.read_csv(csv_incidentes, header=0,delimiter=";", low_memory=False) 

def load_radares():
    df = pd.read_csv('radares.csv', header=0,delimiter=",", low_memory=False) 
    df = gpd.GeoDataFrame(df)
    df = df.dropna(subset=['latitude_l'])

    print(df)

    lats = []
    longs = []
    descs = []
    for index, row in df.iterrows():
        coords = row['latitude_l']

        codigo = row['codigo']
        velocidade = row['velocidade']
        endereco = row['endereco']
        sentido = row['sentido']
        autuacoes = row['autuacoes']
        contagens = row['contagem']

        desc =  str(codigo) + ' ; ' + str(velocidade) + ' ; ' +  str(endereco) + ' ; ' +  str(sentido) + ' ; ' + str(autuacoes) + ' ; ' + str(contagens)

        if coords != 'None':
            coords = coords.replace("(","").replace(")","").split(" ")
            if len(coords) > 1:
                lats.append(coords[0])
                longs.append(coords[1])
                descs.append(desc)

    df = pd.DataFrame(list(zip(lats, longs, descs)), columns =['lat', 'lon','desc'])
    return df

def load_acidentes(tipos):

  #  acidentes_bike = acidentes[acidentes['bicicleta'] != 0]
  #  acidentes_pedestre = acidentes[acidentes['TipoAcidente'] != 'Atropelamento']

    acidentes_copy = acidentes

    tipos_filtros = []
    if tipos != "0":
        tipos = tipos.split(",")
        acidentes_copy = acidentes_copy[acidentes_copy['Tipo de Acidente'] == tipos[0].encode('utf-8')] 
    acidentes_copy = acidentes_copy[~acidentes_copy.latitude.isnull() & ~acidentes_copy.longitude.isnull()]
    return acidentes_copy

def load_corredores():
    corredores = gpd.GeoDataFrame.from_file("../corredores/corredores/SIRGAS_SHP_corredoronibus.shp", encoding='latin-1')
    corredores.crs = {'init' :'epsg:22523'}
    corredores = corredores.to_crs({"init": "epsg:4326"})
    return corredores

def load_ciclovias():
    corredores = gpd.GeoDataFrame.from_file("../corredores/bicicletas/SIRGAS_SHP_redecicloviaria.shp", encoding='latin-1')
    corredores.crs = {'init' :'epsg:22523'}
    corredores = corredores.to_crs({"init": "epsg:4326"})
    return corredores

def load_faixas():
    sf = shapefile.Reader("../corredores/faixas/SAD69_faixa_onibus.shp", encoding='latin-1')
    fields = [x[0] for x in sf.fields][1:]
    print(fields)
    records =[list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]

    #write into a dataframe
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)

    lines = []
    nomes = []
    for index, row in df.iterrows():
        list_coords = row['coords']

        if len(list_coords) > 1:
            line = LineString(list_coords)
            lines.append(line)
            nomes.append(row['nome'])
    frame = pd.DataFrame(list(zip(lines, nomes)), columns =['geometry', 'FE_VIA'])
    faixas = gpd.GeoDataFrame(frame)
    faixas.crs = {'init' :'epsg:22523'}
    faixas = faixas.to_crs({"init": "epsg:4326"})
    return faixas