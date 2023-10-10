from nnf.gen import generate_typo
from nnf import load_nations_name, decompose_korean_word
from nnf.unicode import join_jamos, CHARSET

decomposed = [decompose_korean_word(nation) for nation in load_nations_name()]

DEGREE = 1
NUM_SAMPLE = 10

tots = []
with open(f"./resource/typo_{DEGREE}.txt", "w") as f:
    for nation in decomposed:
        results = []
        while len(results) < NUM_SAMPLE:
            typo = generate_typo(nation, DEGREE)
            if typo not in results and typo not in tots:
                results.append(typo)
                tots.append(typo)
        f.write(join_jamos(nation, True) + '\n')
        f.write("====================================\n")
        for typo in results:
            f.write(join_jamos(typo, True) + '\n')
        f.write('\n')

