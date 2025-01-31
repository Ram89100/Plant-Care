import React from 'react';
import '../styles/result.css';

const ResultComponent = ({ prediction }) => {
  return (
    <div className="result-component">
      <h2>Prediction Result</h2>
      <p><strong>Prediction:</strong> {prediction.disease}</p>

      {/* Display the description using dangerouslySetInnerHTML */}
      <div
        className="description"
        dangerouslySetInnerHTML={{ __html: prediction.description }}
      />

     
    </div>
  );
};

export default ResultComponent;
