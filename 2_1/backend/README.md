# Backend Server

기본적인 Node.js + Express 백엔드 서버 템플릿입니다.

## 디렉토리 구조

```
backend/
├── src/
│   ├── app.js             # Express 앱 진입점
│   ├── config/            # 설정 파일 (DB 등)
│   ├── controllers/       # 요청 처리 컨트롤러
│   ├── models/            # 데이터 모델
│   ├── routes/            # 라우터 정의
│   ├── middleware/        # 미들웨어 (인증, 에러 등)
│   └── utils/             # 유틸리티 함수
├── .env.example           # 환경 변수 예시
├── .gitignore             # git 무시 파일
├── package.json           # 프로젝트 메타정보 및 의존성
└── README.md              # 이 문서
```

## 시작 방법

### 1. 의존성 설치
```bash
npm install
```

### 2. 환경 변수 설정
```bash
cp .env.example .env
# .env 파일을 열어 실제 값으로 수정하세요
```

### 3. 서버 실행

**개발 모드 (자동 재시작):**
```bash
npm run dev
```

**프로덕션 모드:**
```bash
npm start
```

서버는 기본적으로 `http://localhost:3000` 에서 실행됩니다.

## 주요 엔드포인트

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | / | 서버 상태 확인 |
| GET | /api/users | 사용자 목록 조회 |
| POST | /api/users | 사용자 생성 |
| GET | /api/users/:id | 사용자 상세 조회 |
| PUT | /api/users/:id | 사용자 수정 |
| DELETE | /api/users/:id | 사용자 삭제 |