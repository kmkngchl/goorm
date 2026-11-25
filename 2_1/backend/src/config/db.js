const { Pool } = require('pg');

const pool = new Pool({
  host: process.env.DB_HOST || 'localhost',
  port: process.env.DB_PORT || 5432,
  user: process.env.DB_USER || 'postgres',
  password: process.env.DB_PASSWORD || 'password',
  database: process.env.DB_NAME || 'backend_db',
});

pool.connect()
  .then(() => console.log('데이터베이스에 연결되었습니다.'))
  .catch(err => console.error('데이터베이스 연결 실패:', err));

module.exports = pool;