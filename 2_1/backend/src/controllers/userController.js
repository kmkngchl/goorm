const userModel = require('../models/userModel');

// 사용자 목록 조회
const getAllUsers = async (req, res, next) => {
  try {
    const users = await userModel.findAll();
    res.status(200).json({ success: true, data: users });
  } catch (error) {
    next(error);
  }
};

// 사용자 상세 조회
const getUserById = async (req, res, next) => {
  try {
    const { id } = req.params;
    const user = await userModel.findById(id);

    if (!user) {
      return res.status(404).json({ success: false, message: '사용자를 찾을 수 없습니다.' });
    }

    res.status(200).json({ success: true, data: user });
  } catch (error) {
    next(error);
  }
};

// 사용자 생성
const createUser = async (req, res, next) => {
  try {
    const { name, email } = req.body;

    if (!name || !email) {
      return res.status(400).json({ success: false, message: '이름과 이메일은 필수입니다.' });
    }

    const newUser = await userModel.create({ name, email });
    res.status(201).json({ success: true, data: newUser });
  } catch (error) {
    next(error);
  }
};

// 사용자 수정
const updateUser = async (req, res, next) => {
  try {
    const { id } = req.params;
    const { name, email } = req.body;

    const updatedUser = await userModel.update(id, { name, email });

    if (!updatedUser) {
      return res.status(404).json({ success: false, message: '사용자를 찾을 수 없습니다.' });
    }

    res.status(200).json({ success: true, data: updatedUser });
  } catch (error) {
    next(error);
  }
};

// 사용자 삭제
const deleteUser = async (req, res, next) => {
  try {
    const { id } = req.params;
    const deleted = await userModel.remove(id);

    if (!deleted) {
      return res.status(404).json({ success: false, message: '사용자를 찾을 수 없습니다.' });
    }

    res.status(200).json({ success: true, message: '사용자가 삭제되었습니다.' });
  } catch (error) {
    next(error);
  }
};

module.exports = {
  getAllUsers,
  getUserById,
  createUser,
  updateUser,
  deleteUser,
};