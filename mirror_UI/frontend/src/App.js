import React from 'react';
import './App.css';
import Home from "./components/Home/Home"
import User from "./components/User/User"
import {BrowserRouter, Routes, Route} from "react-router-dom"
import Register from './components/Register/Register';

function App() {

  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/users/:user' element={<User/>} />
        <Route path='/register' element={<Register />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
