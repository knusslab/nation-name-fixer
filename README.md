# 국가 이름 오타 생성 및 수정 프로그램
## 설치
1. 파이선 설치 (Miniconda 설치 추천)
2. 현재 디렉토리에서 miniconda cmd창 실행 후 `pip install -r requirements.txt` 입력

## 사용법
### 오타 생성
입력된 단어를 자모음으로 분리 한 뒤, 무작위로 n 개의 자모음을 선택하여 해당 자모음을 키보드 자판상에서 인접한 자모음으로 변경하는 방식으로 m개의 오타를 생성

n, m의 변경을 위해선 gen.py 파일의 DEGREE 및 NUM_SAMPLE 변수를 수정
```python
# gen.py
from nnf.gen import generate_typo
from nnf import load_nations_name, decompose_korean_word
from nnf.unicode import join_jamos, CHARSET

decomposed = [decompose_korean_word(nation) for nation in load_nations_name()]

DEGREE = 1 # 단어 내의 오타 갯수
NUM_SAMPLE = 10 # 생성할 오타 갯수
```

예시: 가나 => ㄱㅏㄴㅏ => ㄱ 선택 => ㄱ와 인접한 자모음인 ㄷㅇㄹㅎㅅ 중 1개 선택 => ㄷㅏㄴㅏ => 다나
#### 실행 방법
1. `python gen.py` 입력


### 오타 교정
오타 교정의 경우 입력된 단어를 자모음으로 분리 한 뒤, 해당 자모음 묶음에서 가장 짧은 편집 거리를 가지는 단어를 선택하여 교정. Symspell 및 Fuzzing 방식 두 개의 구현체가 존재

#### 실행 방법
1. `python fixer.py` 입력

### 실행 예제 파일
`resource/typo_1.txt` 및 `resource/typo_2.txt` 생성 예시 존재. typo_1은 단어 내의 오타가 한 글자, typo_2는 단어 내의 오타가 두 글자인 예시
