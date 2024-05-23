//import { useState } from 'react'

import './App.css'

function App() {
  

  return (
    <>
    <div className='header'>width: 0px; margin: 0 40px;</div>
    <div className='container'>
      <div className='tile'> Tile 1 </div>
      <div className='tile'> Tile 2 </div>
      <div className='tile'> Tile 3 </div>
    </div>
    <div className='header'>width: 200px; margin: 0;</div>
    <div className='container'>
      <div className='tile2'> Tile 1 </div>
      <div className='tile2'> Tile 2 </div>
      <div className='tile2'> Tile 3 </div>
    </div>
    <div className='header'>width: 160px; margin: 0 20px;</div>
    <div className='container'>
      <div className='tile3'> Tile 1 </div>
      <div className='tile3'> Tile 2 </div>
      <div className='tile3'> Tile 3 </div>
    </div>
    <div className='header'>width 180px; margin: 0 10px;</div>
    <div className='container'>
      <div className='tile4'> Tile 1 </div>
      <div className='tile4'> Tile 2 </div>
      <div className='tile4'> Tile 3 </div>
    </div>
    {/* <div className='grid-container'>
        <div className='tile2'> Tile 1 </div>
        <div className='tile2'> Tile 2 </div>
        <div className='tile2'> Tile 3 </div>
      </div> */}
    </>
  )
}

export default App
