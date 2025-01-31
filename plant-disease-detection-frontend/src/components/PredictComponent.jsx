// import React, { useState } from 'react';
// import axios from 'axios';
// import UploadComponent from './UploadComponent';
// import ResultComponent from './ResultComponent';

// const PredictComponent = () => {
//   const [selectedFile, setSelectedFile] = useState(null);
//   const [prediction, setPrediction] = useState(null);
//   const [loading, setLoading] = useState(false);
//   const [error, setError] = useState(null);  // Added error state
//   const [preview, setPreview] = useState(null);  // Image preview state

//   const handleFileChange = (file) => {
//     setSelectedFile(file);
//     setPrediction(null);  // Reset previous prediction
//     setError(null);  // Reset error
//     setPreview(URL.createObjectURL(file));  // Preview the selected image
//   };

//   const handlePrediction = async () => {
//     if (!selectedFile) {
//       setError("Please select an image first!");
//       return;
//     }

//     // Check file size (Example: limit to 5MB)
//     if (selectedFile.size > 5 * 1024 * 1024) {
//       setError("File is too large. Please upload an image less than 5MB.");
//       return;
//     }

//     setLoading(true);
//     const formData = new FormData();
//     formData.append('file', selectedFile);

//     try {
//       const response = await axios.post('http://localhost:8000/predict', formData, {
//         headers: { 'Content-Type': 'multipart/form-data' },
//       });

//       if (response.data) {
//         setPrediction(response.data);
//       } else {
//         setError("Failed to get a valid response from the server.");
//       }
//     } catch (error) {
//       console.error("Error while predicting:", error);
//       setError("Error while making prediction. Please try again.");
//     } finally {
//       setLoading(false);
//     }
//   };

//   return (
//     <div className="predict-component">
//       <h2>Upload Image for Disease Prediction</h2>

//       {/* Upload Component */}
//       <UploadComponent onFileUpload={handleFileChange} />
      
//       {/* Image Preview */}
//       {preview && <img src={preview} alt="Selected preview" className="preview-img" />}
      
//       {/* Error Message */}
//       {error && <p className="error-message">{error}</p>}

//       {/* Predict Button */}
//       <button onClick={handlePrediction} disabled={!selectedFile || loading}>
//         {loading ? "Predicting..." : "Predict"}
//       </button>

//       {/* Show Results */}
//       {prediction && <ResultComponent prediction={prediction} />}
//     </div>
//   );
// };

// export default PredictComponent;
import React, { useState } from 'react';
import axios from 'axios';
import UploadComponent from './UploadComponent';
import ResultComponent from './ResultComponent';

const PredictComponent = () => {
  const [selectedFile, setSelectedFile] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [preview, setPreview] = useState(null);

  const handleFileChange = (file) => {
    setSelectedFile(file);
    setPrediction(null);
    setError(null);
    setPreview(URL.createObjectURL(file));
  };

  const handlePrediction = async () => {
    if (!selectedFile) {
      setError("Please select an image first!");
      return;
    }

    if (selectedFile.size > 5 * 1024 * 1024) {
      setError("File is too large. Please upload an image less than 5MB.");
      return;
    }

    setLoading(true);
    const formData = new FormData();
    formData.append('file', selectedFile);

    try {
      const response = await axios.post('http://localhost:8000/predict', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      if (response.data) {
        setPrediction(response.data);
      } else {
        setError("Failed to get a valid response from the server.");
      }
    } catch (error) {
      console.error("Error while predicting:", error);
      setError("Error while making prediction. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="predict-component">
      <h2>Upload Image for Disease Prediction</h2>

      {/* Upload Component */}
      <UploadComponent onFileUpload={handleFileChange} />

      {/* Container for Image Preview and Button */}
      <div className="preview-container">
        {preview && <img src={preview} alt="Selected preview" className="preview-img" />}
        <div className="button-container">
          <button onClick={handlePrediction} disabled={!selectedFile || loading}>
            {loading ? "Predicting..." : "Predict"}
          </button>
        </div>
      </div>

      {/* Error Message */}
      {error && <p className="error-message">{error}</p>}

      {/* Show Results */}
      {prediction && <ResultComponent prediction={prediction} />}
    </div>
  );
};

export default PredictComponent;
