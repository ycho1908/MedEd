import React, { useState } from 'react';
import axios from 'axios';

function HealthAdvisor() {
  const [prompt, setPrompt] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleResponse = async () => {
    setIsLoading(true);
    try {
      const result = await axios.post('http://localhost:8000/medChatBot', { prompt });
      setResponse(result.data.response);
    } catch (error) {
      console.error('Error generating response', error);
    } finally {
      // after try and catch
      setIsLoading(false);
    }
  };

  return (
    <div>
      <h2>Health Advisor</h2>
      <h3>Feel free to ask any medical questions or concerns you have!</h3>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        rows="4"
        cols="50"
      ></textarea>
      <br/>
      <button class="button-4" onClick={handleResponse}>Get Response</button>
      <p style={{marginLeft: 150, marginRight: 150}}>{isLoading ? 'Loading...' : response}</p>
    </div>
  );
}


export default HealthAdvisor;