import geopandas as gpd
import matplotlib.pyplot as plt
from shapely import Point
from nnf.utils import load_code_mapping, load_country_shp

COUNTRIES_SHAPE_FILE = 'resource/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp'
EEZS_SHAPE_FILE = 'resource/World_EEZ_v11_20191118/eez_v11.shp'

mapping = load_code_mapping()

# ADMIN is country name
boundaries = load_country_shp(COUNTRIES_SHAPE_FILE)

# GEONAME is country name
eews = gpd.read_file(EEZS_SHAPE_FILE)

LAT = 37.5665
LON = 126.9780

data = {
    'lat': [40.7128, 34.0522, 51.5074, 48.8566, -33.8679, 37.5665],
    'lon': [-74.0060, -118.2437, -0.1278, 2.3522, 151.2093, 126.9780],
}

EEZs_data = {
    'lat': [32.5, 12.0, -33.0, 5.0, 27.5],
    'lon': [126.0, 132.5, -179.0, 169.0, 45.0],
}

def get_mapping(code):
    return mapping.get(code, "데이터 없음")

def check_point_within_country(lat, lon):
    """
    Return country, code pair that contains given point
    """
    point = gpd.GeoSeries([Point(lon, lat)])
    for i in range(len(boundaries)):
        if boundaries.iloc[i].geometry.contains(point[0]):
            return boundaries.iloc[i].ADMIN, boundaries.iloc[i].ISO_A3
    return None, None

def check_nearest_country(lat, lon):
    """
    Return country, code pair that is nearest to given point
    """
    nearest_country, nearest_code = None, None
    nearest_distance = float('inf')
    point = gpd.GeoSeries([Point(lon, lat)])
    for i in range(len(boundaries)):
        distance = boundaries.iloc[i].geometry.distance(point[0])
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_country = boundaries.iloc[i].ADMIN
            nearest_code = boundaries.iloc[i].ISO_A3
    return nearest_country, nearest_code

print()

def check_point_within_EEZ(lat, lon):
    """
    Return country, code pair that contains given point from EEZs
    """
    point = gpd.GeoSeries([Point(lon, lat)])
    for i in range(len(eews)):
        if eews.iloc[i].geometry.contains(point[0]):
            return eews.iloc[i].GEONAME, eews.iloc[i].ISO_TER1
    return None, None

def check_nearest_EEZ(lat, lon):
    """
    Return country, code pair that is nearest to given point from EEZs
    """
    nearest_country, nearest_code = None, None
    nearest_distance = float('inf')
    point = gpd.GeoSeries([Point(lon, lat)])
    for i in range(len(eews)):
        distance = eews.iloc[i].geometry.distance(point[0])
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_country = eews.iloc[i].GEONAME
            nearest_code = eews.iloc[i].ISO_TER1
    return nearest_country, nearest_code

print("====================================")
for i in range(len(data['lat'])):
    geoname, code = check_point_within_country(data['lat'][i], data['lon'][i])
    print(f"Country, Within, geoname: {geoname}, code: {code}, country: {get_mapping(code)}")
    geoname, code = check_nearest_country(data['lat'][i], data['lon'][i])
    print(f"Country, Nearest, geoname: {geoname}, code: {code}, country: {get_mapping(code)}")


print("====================================")
for i in range(len(EEZs_data['lat'])):
    geoname, code = check_point_within_country(EEZs_data['lat'][i], EEZs_data['lon'][i])
    print(f"Country, geoname: {geoname}, code: {code}, country: {get_mapping(code)}")

    geoname, code = check_point_within_EEZ(EEZs_data['lat'][i], EEZs_data['lon'][i])
    print(f"EEZs, Within, geoname: {geoname}, code: {code}, country: {get_mapping(code)}")

    geoname, code = check_nearest_EEZ(EEZs_data['lat'][i], EEZs_data['lon'][i])
    print(f"EEZs, Nearest, geoname: {geoname}, code: {code}, country: {get_mapping(code)}")
    print()


ax = boundaries.plot()
eews.plot(ax=ax, alpha=0.5)

for i in range(len(data['lat'])):
    plt.scatter(data['lon'][i], data['lat'][i], c='red')

for i in range(len(EEZs_data['lat'])):
    plt.scatter(EEZs_data['lon'][i], EEZs_data['lat'][i], c='blue')

plt.show()