import { useState,useEffect } from "react";

function FetchData(){
  const[users,setUsers]=useState([]);

  useEffect(()=>{
    fetch("https://jsonplaceholder.typicode.com/users").then
    ((res)=>res.json()).then
    ((data)=>setUsers(data));
  },[]);
  return (
    <div>
      <h2>Fecthed data</h2>
      {users.map((user)=>(
        <p key={user.id}>{user.name}</p>
      ))}
    </div>
  )
}
export default FetchData;