import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import Point
from nnf.utils import load_code_mapping, load_country_shp

COUNTRIES_SHAPE_FILE = 'resource/ne_10m_admin_0_countries/ne_50m_admin_0_countries.shp'

mapping = load_code_mapping()

# ADMIN is country name
boundaries = load_country_shp(COUNTRIES_SHAPE_FILE)

print(boundaries.columns)
print(boundaries[['ADMIN', 'ISO_A3', 'ISO_A2']])

# print all boundaries that ISO_A3 is -99
code_not_exist = boundaries[boundaries['ISO_A3'] == '-99']

print(code_not_exist[['ADMIN', 'ISO_A3', 'ISO_A2']])
