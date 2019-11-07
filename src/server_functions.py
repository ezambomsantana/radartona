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

def load_acidentes():
    return acidentes