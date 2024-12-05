import React from 'react';

const TaskItem = ({ task }) => {
  return (
    <div className="task-item">
      <h3>{task.title}</h3>
      <p>{task.description}</p>
      <span>Assigned to: {task.assigned_to}</span>
    </div>
  );
};

export default TaskItem;
