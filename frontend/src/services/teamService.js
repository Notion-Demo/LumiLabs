import axios from 'axios';

const getTeams = async () => {
  const response = await axios.get('/api/teams');
  return response.data;
};

const createTeam = async (name) => {
  const response = await axios.post('/api/teams', { name });
  return response.data;
};

export default { getTeams, createTeam };
