import logo from './logo.svg';
import './App.css';
import Counter from './components/Counter.js';
import StateLift from './components/StateLift.js';
function App() {
  return (
    <div className="App">
      <div className = "border">
          <h3>Assignment 1</h3>
          <Counter/>

      </div>
      <div className ="border">
        <h3>Assignment 2</h3>
        <StateLift/>
      </div>
    </div>
    
  );
}

export default App;
