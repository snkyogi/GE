import React from 'react';
import { useParams } from 'react-router-dom';

const ProjectDetails = ({ project }) => {
  const { id } = useParams();
  return (
    <div>
      <h2>{id} Details</h2>
      
    </div>
  );
};

export default ProjectDetails;