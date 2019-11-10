# -*- coding: utf-8 -*-
import geopandas as gpd
import numpy as np
import pandas as pd
import csv
import unidecode
import math
import shapefile
import utm
from shapely.geometry import shape, LineString, Polygon, Point
import math

import seaborn as sns
import matplotlib.pyplot as plt


def load_faixas():
    sf = shapefile.Reader("../incidentes/SIRGAS_SHP_acidentecet/SIRGAS_SHP_acidentecet.shp", encoding='latin-1')
    fields = [x[0] for x in sf.fields][1:]
    print(fields)
    records =[list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]

    #write into a dataframe
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)

    df = df[df['aci_data'].str.contains('201902', regex=True)]

    lines = []
    nomes = []
    for index, row in df.iterrows():
        list_coords = row['coords'][0]
        print(list_coords)

        if len(list_coords) > 1:
            line = Point(list_coords)
            lines.append(line)
            nomes.append(row['aci_logrda'])
    frame = pd.DataFrame(list(zip(lines, nomes)), columns =['geometry', 'rua'])
    print(frame)
    faixas = gpd.GeoDataFrame(frame)
    faixas.crs = {'init' :'epsg:22523'}
    faixas = faixas.to_crs({"init": "epsg:4326"})
    faixas.to_csv('acidentes_fev_2019.csv')
    return faixas

load_faixas()

radares = pd.read_csv("radares.csv", header=0,delimiter=",", low_memory=False) 
acidentes = pd.read_csv("../incidentes/acidentes-por-radar.csv", header=0,delimiter=",", low_memory=False) 

final = acidentes.merge(radares, left_on='id_radar',right_on='id')

f = final[['autuacoes', 'contagem','n_acidentes500','velocidade']].sort_values(by=['n_acidentes500'], ascending=False)
print(f.corr())