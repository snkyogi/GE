import React from 'react';
import { Link } from 'react-router-dom';


const Card = ({ project, color }) => {


  return (
    <Link to={`/project/${project.id}`} style={{ textDecoration: 'none' }}>
      <div className="card" style={{ backgroundColor: color }} >
        <h2 className="title">{project.name}</h2>
        <div className="info-container">
          <div className="info-item">
            <div className="info-value">{project.userCount}</div>
            <div className="info-description">Users Count</div>
          </div>
          <div className="info-item">
            <div className="info-value">{project.dbCount}</div>
            <div className="info-description">DBs Connected</div>
          </div>
          <div className="info-item">
            <div className="info-value">{project.tableCount}</div>
            <div className="info-description">Tables Used</div>
          </div>
          <div className="info-item">
            <div className="info-value">{project.testCaseSuites}</div>
            <div className="info-description">Test Case Suites</div>
          </div>
          <div className="info-item">
            <div className="info-value">{project.postTestingActions}</div>
            <div className="info-description">Post Testing Actions</div>
          </div>
          <div className="info-item">
            <div className={`run-status ${project.runStatus.toLowerCase()}`}>{project.runStatus}</div>
            <div className="info-description">Run Status</div>
          </div>
        </div>
      </div>
    </Link>
  );
};

export default Card;
