
import React, { useEffect, useState } from 'react';

export default function Fetch() {
    const [pokemans,setPokemans] = useState<unknown[]>([]);
    useEffect(()=>{
      async function fetchData() {
        let rawData = await (await fetch('https://pokeapi.co/api/v2/pokemon?limit=20&offset=0')).json();
        rawData = rawData.results;
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const data = await Promise.all(rawData.map(async (i:any)=>
        {const data= await (await fetch(i.url)).json();
        return {name:i.name,data:data}}));
        setPokemans(data);
      }
      fetchData();
    })
    return (
      <div className='App'>
        <h1>Hello React.</h1>
        <ul>
        {/* eslint-disable-next-line @typescript-eslint/no-explicit-any */}
        {pokemans.map((v:any,i)=>{
          return(
            <li key={i}>
            <a href={v.data}>{v.name}</a>
            </li>
          )
        })}
        </ul>
      </div>
    );
  }
  