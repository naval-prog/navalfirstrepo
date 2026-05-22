import { useEffect, useState } from "react";
import Card from "./components/Card";
import "./App.css";

function App() {
  const [posts, setPosts] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    async function fetchPosts() {
      try {
        const response = await fetch(
          "http://127.0.0.1:8000/posts"
        );

        const result = await response.json();

        if (!result.success) {
          throw new Error(result.error);
        }

        setPosts(result.data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }

    fetchPosts();
  }, []);

  const filteredPosts = posts.filter((post) =>
    post.title
      .toLowerCase()
      .includes(search.toLowerCase())
  );

  if (loading) return <h2>Loading...</h2>;

  if (error) return <h2>Error: {error}</h2>;

  return (
    <div className="container">
      <h1>Public API Explorer</h1>

      <input
        type="text"
        placeholder="Search posts..."
        value={search}
        onChange={(e) =>
          setSearch(e.target.value)
        }
      />

      <div className="grid">
        {filteredPosts.map((post) => (
          <Card
            key={post.id}
            title={post.title}
            body={post.body}
          />
        ))}
      </div>
    </div>
  );
}

export default App;