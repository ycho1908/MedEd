import logo from './medEd.png';
import './App.css';
import HealthAdvisor from './healthAdvisor';

function App() {
  return (
    <div className="App">
      <img src={logo} className="App-logo" style={{marginTop: 0}} alt="logo" />
      <h1 style={{marginTop: 0}}>MedEd</h1>
      <p>Keep your inquisitive self going!</p>
      <hr/>
      <HealthAdvisor />
    </div>
  );
}

export default App;
