import React from 'react';
import {useParams} from "react-router-dom"
import "./User.css"
import Weather from "../Widgets/Weather/current-weather.js"
import Clock from '../Widgets/Clock/Clock.js';

function User() {

  const {user} = useParams()
  const city = "23.2156 72.6369";

  return (
    <div className="App">
      <h1 className='userName'>Welcome {user}!</h1>
      <div className='fullscreen-container'>
        <div className='horizontal-container'>
          <Weather city={city}/>
          <Clock />
        </div>
        <div className='vertical-container-div'>
          <div className='vertical-container'>

          </div>
          <div className='vertical-container'>
            
          </div>
        </div>
      </div>

    </div>
  );
}

export default User;
