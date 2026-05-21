import { useState } from "react";
function ControlledForm(){
  const[name,setName]=useState("");
  const handleSubmit=(e)=>{
    e.preventDefault();
    alert("submitted"+name);
  }
  return (
    <div>
      <h2>
        Controled form 
      </h2>
      <form onSubmit={handleSubmit}>
        <input type="text"
        placeholder="enter name"
        value={name}
        onChange={(e)=>setName(e.target.value)}/>
        <button type="submit"> Submit</button>

      </form>
      <p>Name:{name}</p>
    </div>
  );
}
export default ControlledForm;