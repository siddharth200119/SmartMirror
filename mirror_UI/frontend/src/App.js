import React from 'react';
import './App.css';

function App() {

  //for full screen

  const requestFullScreen = () => {
    const rootElement = document.documentElement;

    if (rootElement.requestFullscreen) {
      rootElement.requestFullscreen();
    } else if (rootElement.mozRequestFullScreen) {
      rootElement.mozRequestFullScreen();
    } else if (rootElement.webkitRequestFullscreen) {
      rootElement.webkitRequestFullscreen();
    } else if (rootElement.msRequestFullscreen) {
      rootElement.msRequestFullscreen();
    }
  };

  return (
    <div className="App">
      <div className='fullscreen-container'>
        <div className='horizontal-container'>
          
        </div>
        <div className='vertical-container-div'>
          <div className='vertical-container'>

          </div>
          <button className='fullScreenBtn' onClick={requestFullScreen}>Go Full Screen</button>
          <div className='vertical-container'>
            
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
