import Counter from "./components/Counter.jsx";
import ControlledForm from "./components/ControlledForm.jsx";
import Toggle from "./components/Toggle.jsx";
import FetchData from "./components/FecthData.jsx";

function App() {
  return (
    <div>
      <Counter />
      <hr />

      <ControlledForm />
      <hr />

      <Toggle />
      <hr />

      <FetchData />
    </div>
  );
}

export default App;