
import React, { useState, useEffect } from 'react';
import './App.css'

function App() {
  const [homeworldOptions, setHomeworldOptions] = useState([]);
  const [unitTypeOptions, setUnitTypeOptions] = useState([]);
  const [selectedHomeworld, setSelectedHomeworld] = useState('');
  const [selectedUnitType, setSelectedUnitType] = useState('');

  const handleSubmit = () => {
    console.log('submit!');
  }

  return (
    <>
    <h1>Star Wars Alignment Predict</h1>
    <p style={{'marginBottom': '50px'}}>powered by SciKit Learn</p>
      <label>Homeworld:</label>
      <select value={selectedHomeworld} onChange={e => setSelectedHomeworld(e.target.value)}>
        <option value="">Select Homeworld</option>
        {homeworldOptions.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>
      <br />
      <label>Unit Type:</label>
      <select value={selectedUnitType} onChange={e => setSelectedUnitType(e.target.value)}>
        <option value="">Select Unit Type</option>
        {unitTypeOptions.map(option => (
          <option key={option} value={option}>{option}</option>
        ))}
      </select>
      <br />
      <button onClick={handleSubmit}>Submit</button>
    </>
  );
}

export default App
