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

#### 오타 후보군 수정
nnf/gen.py 의 `type_mapping` 변수에서 오타 후보군을 수정할 수 있음
```python
# nnf/gen.py
# 만약 ㅂ의 오타 후보군을 변경하고 싶을 경우
typo_mapping = {
    'ㅂ': 'ㅈㄴㅁ', => 'ㅂ': 'ㅈㄴㅁㅅ', # ㅅ 추가
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
```


### 오타 교정
오타 교정의 경우 입력된 단어를 자모음으로 분리 한 뒤, 해당 자모음 묶음에서 가장 짧은 편집 거리를 가지는 단어를 선택하여 교정. Symspell 및 Fuzzing 방식 두 개의 구현체가 존재

#### 실행 방법
1. `python fixer.py` 입력

### 실행 예제 파일
`resource/typo_1.txt` 및 `resource/typo_2.txt` 생성 예시 존재. typo_1은 단어 내의 오타가 한 글자, typo_2는 단어 내의 오타가 두 글자인 예시

### 위경도 기반 인접 국가 확인

#### 사용 데이터 파일
국가 경계의 경우 [Natural Earth](https://www.naturalearthdata.com/downloads/50m-cultural-vectors/50m-admin-0-countries-2/) 1:50m 사용하였음. 해역의 경우에는 적합한 데이터를 찾지 못해 포함하지 않음. 변경시에는 resource/ne_50m_admin_0_countries 폴더를 참조하여 변경. 베타 경제적 수역의 경우에는 [Marineregions](https://www.marineregions.org/downloads.php) 의 World EEZ v11을 사용하였음.

##### 주의사항
1. 베타적 경계 수역 바깥에서 발생한 지진의 경우엔 처리가 되지 않음.
2. 하기 4개 국가는 Natural Earth 데이터셋에서 ISO 코드가 누락되어 있어 이를 보정할 필요 존재
```text
                           ADMIN ISO_A3 ISO_A2
185              Northern Cyprus    -99    -99
226     Indian Ocean Territories    -99    -99
229  Ashmore and Cartier Islands    -99    -99
238              Siachen Glacier    -99    -99
```

#### 위경도 기반 국가 탐색
추천 사용 방법은 다음과 같음
1. 먼저 진원지가 내륙 경계 안에 있을 경우 해당 국가를 반환
2. 1번에 해당되지 않을 경우, 베타적 경계수역을 기준으로 진원지가 수역 안에 있을 경우 해당 국가를 반환

이를 위해 4개의 함수, 각각
```python
def check_point_within_country(lat, lon):
    """
    Return country, code pair that contains given point
    """
    pass

def check_nearest_country(lat, lon):
    """
    Return country, code pair that is nearest to given point
    """
    pass

def check_point_within_EEZ(lat, lon):
    """
    Return country, code pair that contains given point from EEZs
    """
    pass

def check_nearest_EEZ(lat, lon):
    """
    Return country, code pair that is nearest to given point from EEZs
    """
    pass
```
를 제공함. 실 사용시에는 4개의 함수를 상위에서 하위 순으로 호출하여 사용할 필요 존재

% *주의* 베타적 경제 수역 기반 검색은 국가 경계 기반 검색에서 아무 결과가 나오지 않았을 때 사용해야 함. 이는 베타적 경제 수역은 국가 경계를 포함하지 않아 결과가 다르게 나타날 수 있기 때문임
```text
# 예시
Country, geoname: Saudi Arabia, code: SAU, country: 사우디아라비아
EEZs, Within, geoname: None, code: None, country: 데이터 없음
EEZs, Nearest, geoname: Kuwaiti Exclusive Economic Zone, code: KWT, country: 쿠웨이트
```

#### 실행 예제
1. `python find_nearest_country.py` 입력