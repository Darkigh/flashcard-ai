import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [flashcards, setFlashcards] = useState([]);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return alert("Please select a file.");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/upload", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      if (data.flashcards) {
        setFlashcards(data.flashcards);
      } else {
        alert("Error generating flashcards.");
      }
    } catch (err) {
      console.error(err);
      alert("Upload failed. Is the backend running?");
    }
  };

  return (
    <div className="App">
      <h2>AI Flashcard Generator</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload}>Upload & Generate</button>

      <div className="flashcards">
        {flashcards.map((card, index) => (
          <div className="card" key={index}>
            <div className="front"><strong>Q:</strong> {card.question}</div>
            <div className="back"><strong>A:</strong> {card.answer}</div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
