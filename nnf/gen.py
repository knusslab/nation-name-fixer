import random
from nnf import load_nations_name, decompose_korean_word
from nnf.unicode import join_jamos, CHARSET

typo_mapping = {
    'ㅂ': 'ㅈㄴㅁ',
    'ㅈ': 'ㅂㄷㅁㄴㅇ',
    'ㄷ': 'ㅈㄴㅇㄹㄱ',
    'ㄱ': 'ㄷㅇㄹㅎㅅ',
    'ㅅ': 'ㄱㄹㅎㅗㅛ',
    'ㅛ': 'ㅅㅎㅗㅓㅕ',
    'ㅕ': 'ㅛㅗㅓㅏㅑ',
    'ㅑ': 'ㅕㅓㅏㅣㅐ',
    'ㅐ': 'ㅑㅏㅣㅔ',
    'ㅔ': 'ㅐㅣ',
    'ㅁ': 'ㅂㅈㄴㅌㅋ',
    'ㄴ': 'ㅂㅈㄷㅁㅇㅋㅌㅊ',
    'ㅇ': 'ㅈㄷㄱㄴㄹㅌㅊㅍ',
    'ㄹ': 'ㄷㄱㅅㅇㅎㅊㅍㅠ',
    'ㅎ': 'ㄱㅅㅛㄹㅗㅍㅠㅜ',
    'ㅗ': 'ㅅㅛㅕㅎㅓㅠㅜㅡ',
    'ㅓ': 'ㅛㅕㅑㅗㅏㅜㅡ',
    'ㅏ': 'ㅕㅑㅐㅓㅣㅡ',
    'ㅣ': 'ㅑㅐㅔㅏㅡ',
    'ㅋ': 'ㅁㄴㅌ',
    'ㅌ': 'ㅋㅁㄴㅇㅊ',
    'ㅊ': 'ㅌㄴㅇㄹㅍ',
    'ㅍ': 'ㅊㅇㄹㅎㅠ',
    'ㅠ': 'ㅍㄹㅎㅗㅜ',
    'ㅜ': 'ㅠㅎㅗㅓㅡ',
    'ㅡ': 'ㅜㅗㅓㅏ',
}

def generate_typo(decomposed: str, degree: int):
    # Generate typo from decomposed nations name
    # 1. Change jamo
    # 2. Change order of jamo
    # 3. Remove jamo
    # 4. Add jamo
    original = list(decomposed)
    changed = []
    if degree == 0:
        return original
    if degree > len(decomposed):
        degree = len(decomposed)
    for i in range(degree):
        while True:
            pos = random.randrange(len(original))
            if pos not in changed:
                changed.append(pos)
                break
        target = original[pos]
        while True:
            try:
                new_jamo = random.choice(list(typo_mapping[target]))
                if new_jamo != target:
                    original[pos] = new_jamo
                    break
            except:
                changed.pop()
                break
                
    return "".join(original)