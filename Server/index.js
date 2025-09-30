const express = require("express");
const cors = require("cors");
const axios = require("axios");

const app = express();
app.use(cors());
app.use(express.json());

// Proxy endpoint: React -> Node -> Python
app.post("/api/generate", async (req, res) => {
  try {
    const { topic, audience, tone, product } = req.body;
    const response = await axios.post("http://localhost:8000/generate", {
      topic,
      audience,
      tone,
      product
    });
    res.json(response.data);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const port = process.env.PORT || 4000;
app.listen(port, () => console.log(`Node server running on http://localhost:${port}`));
