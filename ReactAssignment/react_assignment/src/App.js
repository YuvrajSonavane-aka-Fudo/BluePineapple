import logo from './logo.svg';
import './App.css';
import Counter from './components/Counter.js';
import StateLift from './components/StateLift.js';
import TodoList from './components/TodoList.js';
import FocusInput from './components/FocusInput.js';
import ApiCall from './components/ApiCall.js';

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

      <div className = "border">
        <h3>Assignment 3</h3>
        <TodoList/>

      </div>

      <div className = "border">
        <h3>Assignment 4</h3>
        <FocusInput/>

      </div>

      <div className = "border">
        <h3>Assignment 5</h3>
        <ApiCall/>

      </div>


    </div>
    
  );
}

export default App;
