require('dotenv').config();

const express = require('express');
const cors = require('cors');
const helmet = require('helmet');
const morgan = require('morgan');

const userRoutes = require('./routes/userRoutes');
const errorMiddleware = require('./middleware/errorMiddleware');
const logger = require('./utils/logger');

const app = express();
const PORT = process.env.PORT || 3000;

// 미들웨어
app.use(helmet()); // 보안 헤더
app.use(cors()); // CORS 처리
app.use(morgan('dev')); // HTTP 요청 로깅
app.use(express.json()); // JSON 바디 파싱
app.use(express.urlencoded({ extended: true })); // URL-encoded 바디 파싱

// 라우트
app.get('/', (req, res) => {
  res.json({ message: 'Backend 서버가 정상적으로 실행 중입니다.', status: 'ok' });
});

app.use('/api/users', userRoutes);

// 404 핸들러
app.use((req, res, next) => {
  res.status(404).json({ message: '요청한 리소스를 찾을 수 없습니다.' });
});

// 에러 처리 미들웨어 (마지막에 등록)
app.use(errorMiddleware);

// 서버 시작
app.listen(PORT, () => {
  logger.info(`서버가 http://localhost:${PORT} 에서 실행 중입니다.`);
});

module.exports = app;