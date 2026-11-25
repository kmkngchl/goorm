# Python Backend Server (Flask)

기본적인 Python + Flask 백엔드 서버 템플릿입니다.

## 디렉토리 구조

```
python_backend/
├── src/
│   ├── app.py                  # Flask 앱 진입점
│   ├── config/
│   │   └── db.py               # DB 연결 설정
│   ├── controllers/
│   │   └── user_controller.py  # 사용자 컨트롤러
│   ├── models/
│   │   └── user_model.py       # 사용자 데이터 모델
│   ├── routes/
│   │   └── user_routes.py      # 사용자 라우터
│   ├── middleware/
│   │   ├── auth_middleware.py  # JWT 인증 미들웨어
│   │   └── error_middleware.py # 전역 에러 처리
│   └── utils/
│       └── logger.py           # 로거 유틸리티
├── requirements.txt            # Python 의존성
├── .env.example                # 환경 변수 예시
├── .gitignore                  # Git 무시 파일
└── README.md                   # 이 문서
```

## 시작 방법

### 1. 가상환경 생성 및 활성화 (권장)
```bash
python -m venv venv
venv\Scripts\activate      # Windows
```

### 2. 의존성 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
```bash
copy .env.example .env
```

### 4. 서버 실행
```bash
python src/app.py
```

서버는 `http://localhost:5000` 에서 실행됩니다.

## 주요 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | / | 서버 상태 확인 |
| GET | /api/users | 사용자 목록 조회 |
| POST | /api/users | 사용자 생성 |
| GET | /api/users/<id> | 사용자 상세 조회 |
| PUT | /api/users/<id> | 사용자 수정 |
| DELETE | /api/users/<id> | 사용자 삭제 |