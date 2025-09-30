import React, { useState } from "react";
import Preview from "./Preview";
import ImageSelector from "./ImageSelector";

export default function App() {
  const [topic, setTopic] = useState("");
  const [tone, setTone] = useState("professional");
  const [audience, setAudience] = useState("tech professionals");
  const [product, setProduct] = useState("");
  const [post, setPost] = useState(null);
  const [loading, setLoading] = useState(false);

  async function handleGenerate(e) {
    e.preventDefault();
    setLoading(true);
    setPost("");

    try {
      const res = await fetch("http://localhost:4000/api/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ topic, tone, audience, product }),
      });
      const data = await res.json();
      setPost(data);
    } catch (err) {
      setPost("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-6">
      <div className="max-w-2xl w-full bg-white p-8 rounded-2xl shadow-md">
        <h1 className="text-2xl font-bold mb-6">LinkedIn Post Generator</h1>

        <form onSubmit={handleGenerate} className="space-y-4">
          <input
            className="w-full border rounded-lg p-3"
            placeholder="Enter a topic..."
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
          />
        <input
            className="w-full border rounded-lg p-3"
            placeholder="Product (e.g. Books)"
            value={product}
            onChange={(e) => setProduct(e.target.value)}
          />
          <select
            className="w-full border rounded-lg p-3"
            value={tone}
            onChange={(e) => setTone(e.target.value)}
          >
            <option value="professional">Professional</option>
            <option value="inspirational">Inspirational</option>
            <option value="casual">Casual</option>
          </select>

          <input
            className="w-full border rounded-lg p-3"
            placeholder="Audience (e.g. startup founders)"
            value={audience}
            onChange={(e) => setAudience(e.target.value)}
          />

          <button
            type="submit"
            className="px-4 py-2 rounded-lg bg-indigo-600 text-white w-full"
            disabled={loading}
          >
            {loading ? "Generating..." : "Generate Post"}
          </button>
        </form>

        {post && (
          <div className="mt-6 p-4 bg-gray-50 rounded-lg whitespace-pre-wrap">
            <h2 className="font-semibold mb-2">Generated Post:</h2>
            <>
          <Preview content={post.content} />
          <ImageSelector images={post.images} />
          {/* Add confirmation/post logic here */}
        </>
          </div>
        )}
      </div>
    </div>
  );
}
