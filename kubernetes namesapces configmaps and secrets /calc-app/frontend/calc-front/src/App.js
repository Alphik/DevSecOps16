import React, { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [formula, setFormula] = useState("");
  const [result, setResult] = useState(null);
  const [history, setHistory] = useState([]);

  const handleInputChange = (e) => {
    setFormula(e.target.value);
  };

  const handleCalculate = async () => {
    try {
      const response = await axios.post(
        `${process.env.REACT_APP_API_URL}/calculate`,
        { formula }
      );
      setResult(response.data.result);
      fetchHistory();
    } catch (error) {
      console.log(formula);
      console.error("Error calculating:", error);
      alert("Invalid formula!");
    }
  };

  const fetchHistory = async () => {
    const response = await axios.get(
      `${process.env.REACT_APP_API_URL}/history`
    );
    setHistory(response.data);
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Calculator</h1>
      <input
        type='text'
        value={formula}
        onChange={handleInputChange}
        placeholder='Enter calculation'
      />
      <button onClick={handleCalculate}>give it to</button>
      {result !== null && (
        <div>
          <h3>Result: {result}</h3>
        </div>
      )}
      <h2>Calculation History</h2>
      <ul>
        {history.map((item, index) => (
          <li key={index}>
            {item[0]} = {item[1]}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
