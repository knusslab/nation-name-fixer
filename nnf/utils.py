from jamo import j2hcj, h2j, j2h

def load_nations_name(filepath: str = './resource/nations.txt') -> list:
    with open(filepath, 'r', encoding='utf-8') as f:
        nations = f.readlines()
    return [nation.strip() for nation in nations]


def load_decomposed_nations_name(filepath: str = './resource/nations_decomposed.txt') -> list:
    with open(filepath, 'r', encoding='utf-8') as f:
        nations = f.readlines()
    return [nation.strip() for nation in nations]

def decompose_korean_word(word: str) -> str:
    return j2hcj(h2j(word))

def compose_korean_jamo(jamo: str) -> str:
    return j2h(*jamo)

def load_code_mapping(filepath: str = './resource/code_to_plain.txt'):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    mapping = {}
    for line in lines:
        plain, code = line.strip().split('\t')
        if code not in mapping:
            mapping[code] = plain
    return mapping

def load_country_shp(filename='resource/ne_50m_admin_0_countries/ne_50m_admin_0_countries.shp'):
    """
    Since natural earth dataset does not have ISO_A3 code for some countries,
    we need to manually add ISO_A3 code for those countries.
    """
    import geopandas as gpd
    world =  gpd.read_file(filename)
    world.loc[world['ADMIN'] == 'France', 'ISO_A3'] = 'FRA'
    world.loc[world['ADMIN'] == 'Norway', 'ISO_A3'] = 'NOR'
    world.loc[world['ADMIN'] == 'Somaliland', 'ISO_A3'] = 'SOM'
    world.loc[world['ADMIN'] == 'Kosovo', 'ISO_A3'] = 'RKS'
    return world


__all__ = ['load_nations_name', 'decompose_korean_word', 'compose_korean_jamo',
           'load_code_mapping', 'load_country_shp', 'load_decomposed_nations_name']