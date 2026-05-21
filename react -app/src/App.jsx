import Card from './componenets/Card.jsx'
import "./componenets/Card.css"
function App(){
  const profile=[
    {
      id:1,
      name:"cat",
      role:"Meuoo",
      image:"https://static.vecteezy.com/system/resources/thumbnails/072/228/448/small/a-charming-white-kitten-with-orange-and-black-patches-and-bright-green-eyes-rests-among-lush-green-leaves-photo.jpg"
    },
    {
      id:2,
      name:"dog",
      role:"barking",
      image:"https://images.rawpixel.com/image_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDI0LTA0L2Z0LTE0MDMyNC1mcmVlc3R5bGUxLXBvci0wMDdhLXN0b3J5LmpwZw.jpg"
    },
    {
      id:3,
      name:"cow",
      role:"uhhh",
      image:"https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8yNl8zZF9jaGFyYWN0ZXJfb2ZfYV9jdXRlX21pbGtfY293X29uX3doaXRlX2JhY182MDJiMGI0OS02NTQ2LTRiYzEtYTA5NS1lMzg2MDg4MjkxYzQucG5n.png"
    }
  ]
  return (
   <div className='gallery'>
    {
      profile.map((user)=>(
        <Card
          key={user.id}
          name={user.name}
          role={user.role}
          image={user.image}
        />
      ))
    }

   </div>
  );
}
export default App;