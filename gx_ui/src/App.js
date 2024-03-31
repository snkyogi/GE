import './App.css';
import React from 'react';
import Card from './components/Card';

const projects = [
  {
    id: 1,
    name: 'Project 1',
    userCount: 10,
    dbCount: 3,
    tableCount: 20,
    testCaseSuites: 5,
    postTestingActions: 2,
    runStatus: "Success"
  },
  {
    id: 2,
    name: 'Project 2',
    userCount: 10,
    dbCount: 3,
    tableCount: 20,
    testCaseSuites: 5,
    postTestingActions: 2,
    runStatus: "Success"
  },
  // Add more projects as needed
];

const pastelColors = [
  '#B19CD9', // Purple
  '#A7C5EB', // Blue
  '#E8BB97', // Orange
  '#9CC4C4', // Teal
  '#B5EAD7', // Green
  '#F5E1DA', // Peach
  '#FFD3B6', // Salmon
  '#F8B195', // Apricot
];

function App() {
  return (
    <div className="App">
      <h1>Project Dashboard</h1>
      <div className="card-container">
        {projects.map((project, index) => (
          <Card key={project.id} project={project} color={pastelColors[index % pastelColors.length]} />
        ))}
      </div>
    </div>
  );
}

export default App;
