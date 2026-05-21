import ProductCard from "./ProductCard.jsx";
function ProductList({Products}){
  return (
    <div className="products">
      {Products.map((product)=>{
        <ProductCard key={product.id} product={product}/>
      })}
    </div>
  );
}
export default ProductList;