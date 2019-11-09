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

import seaborn as sns
import matplotlib.pyplot as plt

radares = pd.read_csv("radares.csv", header=0,delimiter=",", low_memory=False) 
acidentes = pd.read_csv("../incidentes/acidentes-por-radar.csv", header=0,delimiter=",", low_memory=False) 

final = acidentes.merge(radares, left_on='id_radar',right_on='id')

f = final[['autuacoes', 'contagem','n_acidentes500','velocidade']].sort_values(by=['n_acidentes500'], ascending=False)
print(f.corr())