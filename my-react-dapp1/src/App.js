import React, { useState } from 'react'
import {ethers} from 'ethers'
import Lock from './artifacts/contracts/Lock.sol/Lock.json'

const lockAddress = "0x9fE46736679d2D9a65F0992F2272dE9f3c7fa6e0"

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
