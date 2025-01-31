import React, { useState } from 'react';

const UploadComponent = ({ onFileUpload }) => {
  const [fileName, setFileName] = useState('');

  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setFileName(file.name);
      onFileUpload(file); // Pass file to parent component
    }
  };

  return (
    <div className="upload-component">
      <input type="file" accept="image/*" onChange={handleFileChange} />
      {fileName && <p>Selected: {fileName}</p>}
    </div>
  );
};

export default UploadComponent;
