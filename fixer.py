from symspellpy import SymSpell, Verbosity
from nnf import load_nations_name, decompose_korean_word, compose_korean_jamo
from nnf.unicode import join_jamos

TEST_SAMPLES = ["기나", "마키도니아공화국", "미키도니아공화국", "맥시코", "몬태네그로", "세이셜", "아프카니스탄", "저지섬", "포란드", 
                "코트트리크", "파푸아 뉴가나", "콩고 밎주 공아훅", "도미니카연방", "도미니카연방국", "터키", "튀르키에", "터1키", "텅거", "톤기", "폴ㄹ란드", "도길", "몬트렛ㅅ"]

def create_symspell_fixer(filepath: str=  './resource/nations_decomposed.txt') -> SymSpell:
    symspell = SymSpell()
    symspell.create_dictionary(filepath)
    return symspell

decomposed = [decompose_korean_word(nation) for nation in load_nations_name()]

symspell = create_symspell_fixer()

targets = [decompose_korean_word(sample) for sample in TEST_SAMPLES]

for target in targets:
    target = decompose_korean_word(target)

    try:
        suggestions = symspell.lookup(target, Verbosity.ALL, max_edit_distance=2)
        print("Target: ", join_jamos(target))
        for i, sug in enumerate(suggestions):
            sug_nation = sug.term
            print(f"제안 {i + 1}: {join_jamos(sug_nation)}")
        print()
    except:
        print("No suggestion")


print("====================================")
print("Fuzzing based fixer test")
print("====================================")
# Fuzzing based fixer
from thefuzz import process, fuzz
for target in targets:
    target = decompose_korean_word(target)
    suggestion = process.extractOne(target, decomposed, scorer=fuzz.ratio)
    print("Target: ", join_jamos(target))
    print(f"제안: {join_jamos(suggestion[0])}")
    print()

