"""
Decompose nations name into jamo
"""
from nnf import load_nations_name, decompose_korean_word

nations = load_nations_name()

decomposed = [decompose_korean_word(nation) for nation in nations]

with open('./resource/nations_decomposed.txt', 'w', encoding='utf-8') as f:
    for nation in decomposed:
        f.write(nation + '\n')

