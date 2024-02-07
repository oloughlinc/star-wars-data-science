
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'

function App() {
  const [homeworldOptions, setHomeworldOptions] = useState([]);
  const [unitTypeOptions, setUnitTypeOptions] = useState([]);
  const [selectedHomeworld, setSelectedHomeworld] = useState('');
  const [selectedUnitType, setSelectedUnitType] = useState('');
  const [alignment, setAlignment] = useState('');

  const handleSubmit = () => {
    axios.post('http://localhost:5000/api/predict', {
      'homeworld': [selectedHomeworld],
      'unit_type': [selectedUnitType]
    })
    .then(response => {
      console.log(response.data);
      setAlignment(response.data[0])});
  }

  useEffect(() =>{
    const getHomeworld = async() => {
      let response = await axios('http://localhost:5000/api/homeworlds');
      console.log(response.data);
      setHomeworldOptions(response.data);
    }
    getHomeworld();
  }, [])

  useEffect(() =>{
    const getUnits = async() => {
      let response = await axios('http://localhost:5000/api/units');
      console.log(response.data);
      setUnitTypeOptions(response.data);
    }
    getUnits();
  }, [])

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
      <div id={'alignment'}>
        <h2>{alignment}</h2>
      </div>
    </>
  );
}

export default App
