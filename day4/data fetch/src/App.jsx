import { useState, useEffect } from "react";
import Navbar from "./components/Navbar.jsx";
import SearchBar from "./components/SearchBar.jsx";
import ProductList from "./components/ProductList.jsx";
import "./App.css"

function App(){
  const[products,setProducts]=useState([]);
  const[filteredProducts,setFilteredProducts]=useState([]);
  const[loading ,setLoading]=useState(true);
  const[error,setError]=useState("");
  const [search,setSearch]= useState("");
  useEffect(()=>{
    fetchProducts();
  },[]);
  async function fetchProducts(){
    try{
      setLoading(true);
      const res= await fetch("https://fakestoreapi.com/products");
      if(!res.ok)throw new Error("Failed to fetch");
      const data =await res.json();
      setProducts(data);
      setFilteredProducts(data);
    }
    catch(err){
      setError(err.message);
    }
    finally{
      setLoading(false);
    }
    useEffect(()=>{
      const filtered=products.filter((product)=>product.titlle.toLowerCase().includes(search.toLowerCase()));
      setFilteredProducts(filtered);
    },[search,products]);
    return (
      <div>
        <Navbar></Navbar>
        <SearchBar
        search={search}
        setSearch={setSearch}></SearchBar>
         {loading && <h2>Loading...</h2>}
          {error && <h2>{error}</h2>}
          {!loading && !error && (
        <ProductList
          products={filteredProducts}
        />
      )}
      </div>
    )
  }
}
export default App;