import React from 'react';

const TeamCard = ({ team }) => {
  return (
    <div className="team-card">
      <h3>{team.name}</h3>
      <p>Team ID: {team.id}</p>
    </div>
  );
};

export default TeamCard;
