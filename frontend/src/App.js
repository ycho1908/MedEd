import logo from './logo.svg';
import './App.css';
import HealthAdvisor from './healthAdvisor';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Medical Assistant</h1>
        <HealthAdvisor />
      </header>
    </div>
  );
}

export default App;
