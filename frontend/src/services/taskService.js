import axios from 'axios';

const getTasks = async () => {
  const response = await axios.get('/api/tasks');
  return response.data;
};

export default { getTasks };
