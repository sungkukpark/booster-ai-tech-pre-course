# Python 기초 학습 예제 저장소

이 저장소는 Python 프로그래밍의 기초 개념을 학습하기 위한 예제 코드 모음입니다. 변수, 함수, 리스트, 문자열 포맷팅 등 Python의 핵심 개념들을 실제 예제를 통해 학습할 수 있습니다.

## 🎯 프로젝트 목적

- Python 기초 문법과 개념 학습
- 실습을 통한 프로그래밍 능력 향상
- Jupyter Notebook을 활용한 대화형 학습
- 테스트 코드 작성 방법 학습

## 📋 사전 요구사항

- Python 3.8 이상
- uv (Python 패키지 관리자)

### uv 설치

macOS/Linux:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Windows:
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## 🚀 설치 및 설정

### 1. 저장소 클론
```bash
git clone <repository-url>
cd booster-ai-tech-pre-course
```

### 2. uv를 사용한 가상환경 생성
```bash
# 가상환경 생성
uv venv

# 가상환경 활성화
# macOS/Linux:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate
```

### 3. 패키지 설치
```bash
# requirements.txt의 모든 패키지 설치
uv pip install -r requirements.txt
```

### 4. 설치 확인
```bash
# Python 버전 확인
python --version

# 설치된 패키지 확인
uv pip list
```

## 📁 프로젝트 구조

```
booster-ai-tech-pre-course/
├── README.md                 # 프로젝트 설명서
├── requirements.txt          # Python 패키지 의존성
├── notes.ipynb              # Jupyter Notebook 학습 노트
├── variables.py             # 변수 예제
├── function.py              # 함수 예제
├── input.py                 # 입력 처리 예제
├── format.py                # 문자열 포맷팅 예제
├── example.py               # 함수 조합 예제
├── fahrenheit_converter.py  # 화씨 변환기
├── test_fahrenheit-converter.py  # 화씨 변환기 테스트
├── score.py                 # 점수 채점 시스템
├── score.txt                # 원본 점수 데이터
├── score_graded.txt         # 채점 결과
├── age.py                   # 나이 계산 예제
└── school.py                # 학교 관련 예제
```

## 💻 사용법

### Jupyter Notebook 실행
```bash
# Jupyter Notebook 시작
uv run jupyter notebook

# 또는 Jupyter Lab 시작
uv run jupyter lab
```

### Python 스크립트 실행
```bash
# 개별 스크립트 실행
uv run python fahrenheit_converter.py
uv run python score.py
uv run python example.py
```

### 테스트 실행
```bash
# pytest를 사용한 테스트 실행
uv run pytest test_fahrenheit-converter.py -v
```

## 📚 예제 설명

### 1. 기초 개념 학습
- **variables.py**: 변수 선언과 사용법
- **function.py**: 함수 정의와 호출
- **input.py**: 사용자 입력 처리
- **format.py**: 문자열 포맷팅 방법

### 2. 실습 예제
- **fahrenheit_converter.py**: 섭씨와 화씨 온도 변환 프로그램
  - 사용자 입력 처리
  - 예외 처리
  - 함수 정의와 호출
  
- **score.py**: 점수 채점 시스템
  - 파일 입출력
  - 데이터 처리
  - 학점 계산 로직

- **example.py**: 함수 조합 예제
  - 함수의 조합과 합성
  - 변수 스코프 이해

### 3. Jupyter Notebook
- **notes.ipynb**: 대화형 Python 학습 노트
  - 리스트 조작
  - 문자열 포맷팅
  - 기본 함수 사용법

## 🛠️ 개발 환경

### 권장 IDE/에디터
- **VS Code**: Python 확장 설치 권장
- **PyCharm**: 전문 Python IDE
- **Jupyter Lab**: 대화형 개발 환경

### 코드 포맷팅
```bash
# Black을 사용한 코드 포맷팅
uv run black *.py
```

### 타입 체크
```bash
# mypy를 사용한 타입 체크 (설치된 경우)
uv run mypy *.py
```

## 📝 학습 가이드

1. **기초 개념부터 시작**: `variables.py` → `function.py` → `input.py` 순서로 학습
2. **실습 예제 진행**: `fahrenheit_converter.py`로 실제 프로그램 작성법 학습
3. **Jupyter Notebook 활용**: `notes.ipynb`로 대화형 학습
4. **테스트 코드 작성**: `test_fahrenheit-converter.py` 참고하여 테스트 작성법 학습

## 🤝 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.

## 📞 문의

프로젝트에 대한 질문이나 제안사항이 있으시면 이슈를 생성해 주세요.
