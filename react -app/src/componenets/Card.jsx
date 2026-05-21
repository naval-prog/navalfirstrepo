import "./Card.css"
function Card({name,role,image}){
  return (
    <div className="card">
     <img
     src={image}
     alt={name}
     className="card-img"
     />
     <h2>{name}</h2>
     <p>{role}</p>
    </div>
  );
}
export default Card;