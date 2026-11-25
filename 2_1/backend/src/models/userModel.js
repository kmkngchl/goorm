// 인메모리 저장소 (예시). 실제 프로젝트에서는 DB를 사용하세요.
let users = [
  { id: 1, name: '홍길동', email: 'hong@example.com', createdAt: new Date().toISOString() },
  { id: 2, name: '김철수', email: 'kim@example.com', createdAt: new Date().toISOString() },
];
let nextId = 3;

const findAll = () => {
  return users;
};

const findById = (id) => {
  const userId = parseInt(id, 10);
  return users.find(u => u.id === userId) || null;
};

const create = (userData) => {
  const newUser = {
    id: nextId++,
    name: userData.name,
    email: userData.email,
    createdAt: new Date().toISOString(),
  };
  users.push(newUser);
  return newUser;
};

const update = (id, userData) => {
  const userId = parseInt(id, 10);
  const index = users.findIndex(u => u.id === userId);

  if (index === -1) {
    return null;
  }

  users[index] = {
    ...users[index],
    ...(userData.name !== undefined && { name: userData.name }),
    ...(userData.email !== undefined && { email: userData.email }),
    updatedAt: new Date().toISOString(),
  };

  return users[index];
};

const remove = (id) => {
  const userId = parseInt(id, 10);
  const index = users.findIndex(u => u.id === userId);

  if (index === -1) {
    return false;
  }

  users.splice(index, 1);
  return true;
};

module.exports = {
  findAll,
  findById,
  create,
  update,
  remove,
};