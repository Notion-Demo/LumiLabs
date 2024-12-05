import React, { useEffect, useState } from 'react';
import taskService from '../services/taskService';
import TaskItem from '../components/TaskItem';

const TasksPage = () => {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    const fetchTasks = async () => {
      const data = await taskService.getTasks();
      setTasks(data);
    };
    fetchTasks();
  }, []);

  return (
    <div className="tasks-page">
      <h2>Tasks</h2>
      {tasks.map((task) => (
        <TaskItem key={task.id} task={task} />
      ))}
    </div>
  );
};

export default TasksPage;
