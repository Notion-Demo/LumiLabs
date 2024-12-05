import axios from 'axios';

const login = async (username, password) => {
  const response = await axios.post('/api/auth/login', { username, password });
  localStorage.setItem('token', response.data.token);
};

const logout = () => {
  localStorage.removeItem('token');
};

export default { login, logout };
