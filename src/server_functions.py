# -*- coding: utf-8 -*-
import geopandas as gpd
import numpy as np
import pandas as pd
import csv
import unidecode
import math
import utm
from shapely.geometry import shape, LineString, Polygon

csv_incidentes = "../incidentes/records.csv"

acidentes = pd.read_csv(csv_incidentes, header=0,delimiter=",", low_memory=False) 

def load_acidentes(tipos):

    acidentes_copy = acidentes

    tipos_filtros = []
    if tipos != "0":
        tipos = tipos.split(",")
        acidentes_copy = acidentes_copy[acidentes_copy['Tipo de Acidente'] == tipos[0].encode('utf-8')] 

    return acidentes_copy