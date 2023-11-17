import React from 'react';
import {useParams} from "react-router-dom"
import "./User.css"
import Weather from "../Widgets/Weather/current-weather.js"
import Clock from '../Widgets/Clock/Clock.js';
import News from '../Widgets/News/News.jsx';

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
          <News preferences = {"tesla"}/>
        </div>
        <div className='vertical-container-div'>
          <div className='vertical-container'>
            <News preferences = {"tesla"}/>
          </div>
          <div className='vertical-container'>
            
          </div>
        </div>
      </div>

    </div>
  );
}

export default User;
