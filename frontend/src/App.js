import React, { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [response, setResponse] = useState("");

  const uploadResume = async () => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post("http://127.0.0.1:5000/upload", formData);
      setResponse(res.data);
    } catch (err) {
      console.error("Error uploading file", err);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>Resume Analyzer</h1>
      <input
        type="file"
        onChange={(e) => setFile(e.target.files[0])}
        accept=".txt"
      />
      <button onClick={uploadResume}>Upload</button>
      {response && (
        <div>
          <h3>Feedback:</h3>
          <p>Score: {response.score.toFixed(2)}</p>
          <p>{response.feedback}</p>
        </div>
      )}
    </div>
  );
}

export default App;
