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


__all__ = ['load_nations_name', 'decompose_korean_word', 'compose_korean_jamo']