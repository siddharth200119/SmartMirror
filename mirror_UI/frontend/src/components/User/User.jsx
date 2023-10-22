import React from 'react';
import {useParams} from "react-router-dom"
import "./User.css"

function User() {

  const {user} = useParams()

  return (
    <div className="App">
      <h1 className='userName'>Welcome {user}!</h1>
      <div className='fullscreen-container'>
        <div className='horizontal-container'>

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
