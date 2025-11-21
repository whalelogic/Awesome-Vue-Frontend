import express from "express";
import cors from "cors";
import fs from "fs/promises";
import path from "path";

const app = express();
app.use(cors());

// Helper function to read the JSON file
const readPosts = async () => {
  const filePath = path.resolve(process.cwd(), "allposts.json");
  const data = await fs.readFile(filePath, "utf-8");
  return JSON.parse(data);
};

// --- Database code (kept for reference, but not used) ---
/*
import mariadb from "mariadb";

const pool = mariadb.createPool({
  host: "127.0.0.1",
  user: "root",
  password: "",
  database: "content",
  port: 3306,
  connectionLimit: 5,
});

app.get("/api/posts/db", async (req, res) => {
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

app.get("/api/posts/db/:slug", async (req, res) => {
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
*/

// --- New endpoints using allposts.json ---

app.get("/api/posts", async (req, res) => {
  try {
    const posts = await readPosts();
    // Filter for published posts and return a subset of fields
    const publishedPosts = posts
      .filter(p => p.published === "1")
      .map(({ id, slug, title, subtitle, author, summary, read_time, tags, category, created_on, updated_on, published, featured }) => ({
        id,
        slug,
        title,
        subtitle,
        author,
        summary,
        read_time,
        tags,
        category,
        created_on,
        updated_on,
        published,
        featured
      }))
      .sort((a, b) => new Date(b.created_on) - new Date(a.created_on));
    res.json(publishedPosts);
  } catch (err) {
    res.status(500).json({ error: `Failed to read posts: ${err.message}` });
  }
});

app.get("/api/posts/:slug", async (req, res) => {
  try {
    const posts = await readPosts();
    const post = posts.find(p => p.slug === req.params.slug && p.published === "1");
    if (!post) {
      return res.status(404).json({ error: "Post not found" });
    }
    res.json(post);
  } catch (err) {
    res.status(500).json({ error: `Failed to read posts: ${err.message}` });
  }
});

app.listen(3001, () => {
  console.log("API server running on http://localhost:3001");
});