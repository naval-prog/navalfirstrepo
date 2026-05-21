import { useState } from "react";

function Toggle(){
  const[is,setIs]=useState(false);
  return (
    <div>
      <h2>Toggle</h2>
      <button onClick={()=>setIs(!is)}>
        {is?"On":"Off"}
      </button>
    </div>
  );
}
export default Toggle;