import React, { useEffect, useState } from 'react';
import teamService from '../services/teamService';
import TeamCard from '../components/TeamCard';

const TeamsPage = () => {
  const [teams, setTeams] = useState([]);
  const [teamName, setTeamName] = useState('');

  useEffect(() => {
    const fetchTeams = async () => {
      const data = await teamService.getTeams();
      setTeams(data);
    };
    fetchTeams();
  }, []);

  const handleCreateTeam = async () => {
    if (!teamName) return;
    const newTeam = await teamService.createTeam(teamName);
    setTeams((prevTeams) => [...prevTeams, newTeam]);
    setTeamName('');
  };

  return (
    <div className="teams-page">
      <h2>Teams</h2>
      <input
        type="text"
        placeholder="Team Name"
        value={teamName}
        onChange={(e) => setTeamName(e.target.value)}
      />
      <button onClick={handleCreateTeam}>Create Team</button>
      <div className="team-list">
        {teams.map((team) => (
          <TeamCard key={team.id} team={team} />
        ))}
      </div>
    </div>
  );
};

export default TeamsPage;
