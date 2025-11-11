# Awesome Vue Front-end using Vite Bundler

This is the official portfolio and blog site of Keith Thomson. Built with Go (Gin Gonic), Vue, and TailwindCSS, the site showcases blog posts, projects, and professional experience. Content is served from a MariaDB backend and dynamically rendered with Markdown and HTML templates.



## 🔧 Features

- 📰 Blog rendering with Markdown support

- 🗂️ Dynamic project listing from GitHub API

- 📘 Vue-powered frontend with responsive TailwindCSS UI

- 🧠 RAG/AI Engineering project highlights

- 📇 Profile card with live status and skills

- 🔒 Secure routing and scalable Go backend

- 🛢️ MariaDB integration for content storage

- 📁 Project Structure

# 📁 Project Structure

| Path | Type | Description |
|------|------|-------------|
| `/` | Root | awesomeVueBlog project root |
| `/src/` | Directory | Vue.js source files |
| `/src/App.vue` | File | Main application component |
| `/src/main.js` | File | Application entry point with router configuration |
| `/src/style.css` | File | Global styles and markdown rendering CSS |
| `/src/views/` | Directory | Vue page components |
| `/src/views/About.vue` | File | About page component |
| `/src/views/Blog.vue` | File | Blog listing page with search and filters |
| `/src/views/BlogPost.vue` | File | Individual blog post detail view with markdown rendering |
| `/src/views/Home.vue` | File | Homepage with featured posts |
| `/src/views/Projects.vue` | File | Projects page with GitHub API integration |
| `/allposts.json` | File | Blog posts data with content in markdown format |
| `/package.json` | File | Node.js dependencies and scripts |
| `/vite.config.js` | File | Vite build configuration |
| `/index.html` | File | HTML entry point |

## 📊 Key Features by Component

| Component | Features |
|-----------|----------|
| **App.vue** | Navigation header, router view, responsive layout |
| **Home.vue** | Featured posts carousel, blog card grid, colorful images from Unsplash |
| **Blog.vue** | Search functionality, tag filtering, featured post section, all posts listing |
| **BlogPost.vue** | Markdown-to-HTML rendering with `marked`, custom prose styling, back navigation |
| **Projects.vue** | GitHub API integration, live repo data, language icons, star/fork counts |
| **allposts.json** | 13 formatted posts with emojis, tables, code blocks, and structured content |

## 🎨 Styling Highlights

- Gradient backgrounds (purple/pink/blue theme)
- Frosted glass effects with backdrop blur
- Custom code block styling with language badges
- Responsive grid layouts
- Custom markdown prose styling


<table>
  <tr>
    <td>
      <img width="724" height="617" alt="image" src="https://github.com/user-attachments/assets/f0bfd884-1299-491a-9d0b-4d6a848a32d9" />
    </td>
    <td>
      <img width="724" height="617" alt="image" src="https://github.com/user-attachments/assets/6ae6c849-cd28-48be-9ddb-da3268d81b45" />
    </td>
  </tr>
</table>


## 🚀 Running the App

1. Prerequisites:

`Go 1.20+`

`Node.js` (for Vue build, if used)


2. Environment Setup:

```
cp .env.example .env  # if using env for DB credentials
```

> Optionally, you may use a JSON file containing the fields specified in allposts.json.
> You can create your own fields, but remember to modify the .vue templates if that is the case.  

3. Run the server:

`go run main.go`

4. Access via:

`http://localhost:8080`

## 📦 Deployment

- Reverse proxy with Caddy or Nginx recommended
- Optional: Use Docker for containerized deployment

## Build and run with docker-compose

`docker-compose up -d`

## Or build and run with docker directly

`docker build -t awesomevueblog .`

#### Serve HTTPS-enabled App with Nginx Configuration (provided)

`docker run -p 80:80 awesomevueblog`

Access Dev server at `http://localhost:5173 or localhost:8080`
Access API @ `localhost:3000/localhost:3001`

## 👨‍💻 About Me

Keith Thomson is a U.S. Army veteran turned software engineer with expertise in Go, Rust, Python, cloud systems, and AI integrations. This site is both a resume and a publication space for original technical writing and applied research.


