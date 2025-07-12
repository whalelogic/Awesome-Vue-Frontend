import express from "express";
import cors from "cors";
import mariadb from "mariadb";

const pool = mariadb.createPool({
  host: "127.0.0.1",
  user: "root",
  password: "Sophia",
  database: "content",
  port: 3306,
  connectionLimit: 5,
});

const app = express();
app.use(cors());

app.get("/api/posts", async (req, res) => {
  let conn;
  try {
    conn = await pool.getConnection();
    const rows = await conn.query(
      "SELECT id, slug, title, subtitle, author, summary, read_time, tags, category, created_on, updated_on, published, featured FROM posts WHERE published=1 ORDER BY created_on DESC"
    );
    res.json(rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  } finally {
    if (conn) conn.release();
  }
});

app.get("/api/posts/:slug", async (req, res) => {
  let conn;
  try {
    conn = await pool.getConnection();
    const rows = await conn.query(
      "SELECT * FROM posts WHERE slug = ? AND published=1",
      [req.params.slug]
    );
    if (rows.length === 0) return res.status(404).json({ error: "Not found" });
    res.json(rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  } finally {
    if (conn) conn.release();
  }
});

app.listen(3001, () => {
  console.log("API server on http://localhost:3001");
});
