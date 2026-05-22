import Badge from "./components/Badge.jsx";

function App() {
  return (
    <div>
      <h2>Badge Example</h2>

      <Badge label="New" color="green" />
      <Badge label="Premium" color="#1F3864" />
      <Badge label="Default" />
    </div>
  );
}

export default App;