Keith Thomson – Portfolio Blog
This is the official portfolio and blog site of Keith Thomson, a full-stack developer and systems analyst. Built with Go (Gin Gonic), Vue, and TailwindCSS, the site showcases blog posts, projects, and professional experience. Content is served from a MariaDB backend and dynamically rendered with Markdown and HTML templates.

🔧 Features
📰 Blog rendering with Markdown support

🗂️ Dynamic project listing from GitHub API

📘 Vue-powered frontend with responsive TailwindCSS UI

🧠 RAG/AI Engineering project highlights

📇 Profile card with live status and skills

🔒 Secure routing and scalable Go backend

🛢️ MariaDB integration for content storage

📁 Project Structure
php
Copy
Edit
.
├── main.go                 # Gin Gonic entry point
├── templates/              # HTML templates (index, base, posts, about, etc.)
├── static/                 # Static assets (CSS, images, icons)
├── handlers/               # Route handlers for each page
├── models/                 # DB models for posts and metadata
├── views/ (if Vue SPA)     # Vue components (for hybrid rendering)
└── README.md               # You are here
🚀 Running the App
1. Prerequisites:

Go 1.20+

Node.js (for Vue build, if used)

MariaDB with a database named content containing tables like all_posts

2. Environment Setup:

bash
Copy
Edit
cp .env.example .env  # if using env for DB credentials
3. Run the server:

bash
Copy
Edit
go run main.go
4. Access via:
http://localhost:8080

📦 Deployment
Reverse proxy with Caddy or Nginx recommended

Set GIN_MODE=release in production

Optional: Use Docker for containerized deployment

👨‍💻 About Me
Keith Thomson is a U.S. Army veteran turned software engineer with expertise in Go, Rust, Python, cloud systems, and AI integrations. This site is both a resume and a publication space for original technical writing and applied research.

☕ Support
If you enjoy the content or find the guides helpful:

Buy Me a Coffee
