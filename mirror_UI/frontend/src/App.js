import React from 'react';
import './App.css'; // Import the CSS file you created

function App() {
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
        <button className='fullScreenBtn' onClick={requestFullScreen}>Go Full Screen</button>
      </div>
      
      {/* Your app content */}
    </div>
  );
}

export default App;
