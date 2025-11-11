#!/usr/bin/env python3
import json

# Read the JSON file
with open('allposts.json', 'r', encoding='utf-8') as f:
    posts = json.load(f)

# Find and update post 26
for post in posts:
    if post['id'] == "26":
        # Fixed content with proper escaping
        post['content'] = """# 🏗️ Building a Static HTML Generator with Go

## 📋 Introduction

This guide explains how to generate **static HTML pages** using Go's standard `html/template` package.

**What you'll learn:**
- 📂 Setting up project structure
- 🔄 Reading JSON data
- 📝 Parsing HTML templates
- 💾 Writing individual HTML files
- 🚀 Running the generator

---

## 📁 Project Structure

```
.
├── templates/
│   ├── base.html
│   └── post.html
├── data/
│   └── allposts.json
├── generate.go
└── generated/
```

---

## 📊 JSON Data Example

### `data/allposts.json`

Your JSON data would contain an array of post objects with fields like id, title, subtitle, summary, readtime, tags, and content.

---

## 📄 Template Files

### `templates/base.html`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{ .Title }}</title>
    <link rel="stylesheet" href="/static/styles.css">
</head>
<body>
    <header>
        <h1>Go Static Site</h1>
    </header>
    <main>
        {{ block "content" . }}{{ end }}
    </main>
    <footer>
        <p>© 2025 Whaler Research</p>
    </footer>
</body>
</html>
```

### `templates/post.html`

```html
{{ define "content" }}
<article>
    <h2>{{ .Title }}</h2>
    <h3>{{ .Subtitle }}</h3>
    <p><em>{{ .ReadTime }} read</em></p>
    <div>{{ .Content }}</div>
</article>
{{ end }}
```

---

## 💻 Core Generator Script

### `generate.go`

```go
package main

import (
    "encoding/json"
    "html/template"
    "io/ioutil"
    "log"
    "os"
    "path/filepath"
)

// Post represents the structure of one blog post
type Post struct {
    ID       int      
    Title    string   
    Subtitle string   
    Summary  string   
    ReadTime string   
    Tags     []string 
    Content  string   
}

// loadPosts reads JSON file into a slice of Post structs
func loadPosts(filename string) ([]Post, error) {
    data, err := ioutil.ReadFile(filename)
    if err != nil {
        return nil, err
    }
    
    var posts []Post
    if err := json.Unmarshal(data, &posts); err != nil {
        return nil, err
    }
    
    return posts, nil
}

// renderTemplate applies data to templates and writes HTML output
func renderTemplate(post Post, tmpl *template.Template) error {
    outputDir := "generated"
    os.MkdirAll(outputDir, 0755)
    
    outputPath := filepath.Join(outputDir, 
        filepath.Base(post.Title)+".html")
    
    file, err := os.Create(outputPath)
    if err != nil {
        return err
    }
    defer file.Close()
    
    return tmpl.ExecuteTemplate(file, "base.html", post)
}

func main() {
    // 1. Load posts
    posts, err := loadPosts("data/allposts.json")
    if err != nil {
        log.Fatal("Error loading posts:", err)
    }
    
    // 2. Parse templates
    tmpl := template.Must(template.ParseFiles(
        "templates/base.html",
        "templates/post.html",
    ))
    
    // 3. Render each post
    for _, post := range posts {
        if err := renderTemplate(post, tmpl); err != nil {
            log.Printf("Error rendering %s: %v", post.Title, err)
        } else {
            log.Printf("✅ Generated page for: %s", post.Title)
        }
    }
    
    log.Println("🎉 All pages generated successfully.")
}
```

---

## 🔍 Explanation of Key Functions

### 1. `loadPosts(filename string) ([]Post, error)`

**Purpose:** Reads and parses the JSON data file

- 📖 Opens and reads the JSON file
- 🔄 Deserializes (unmarshals) JSON into Go structs
- ✅ Returns a slice of posts for processing
- ❌ Returns an error if file reading or parsing fails

### 2. `renderTemplate(post Post, tmpl *template.Template) error`

**Purpose:** Generates HTML file for each post

- 📝 Takes a post and the parsed template set
- 📁 Creates an output file under `/generated/`
- 🔄 Executes the base template, injecting the post data
- 🎨 The `{{ define "content" }}` block from `post.html` overrides the `{{ block "content" }}` in `base.html`

---

## 🚀 Running the Generator

### Execute the generator

```bash
go run generate.go
```

**Output:**
```
✅ Generated page for: Learning Go Templates
✅ Generated page for: Building a Static Site Generator
🎉 All pages generated successfully.
```

All static files are written to the `/generated` directory and can be served using any static web server.

---

## 🎨 Extending the Generator

You could enhance this with:

### 1. 📑 **Index Page**
- Generate a homepage listing all posts
- Add pagination for large post collections

### 2. 📝 **Markdown Support**
- Convert Markdown to HTML using `goldmark` or `blackfriday`
- Write posts in Markdown instead of HTML

### 3. ⚡ **Performance**
- Implement template caching
- Add incremental builds (only regenerate changed files)
- Parallelize rendering with goroutines

### 4. 📡 **RSS/Atom Feeds**
- Generate RSS/Atom feeds for blog subscriptions
- Include metadata and timestamps

### 5. 🎯 **Enhanced Features**
- Add syntax highlighting for code blocks
- Generate sitemaps for SEO
- Create tag/category pages

---

## 🔄 Auto-Regeneration with Air

For development, automatically regenerate on file changes:

### Install Air

```bash
go install github.com/air-verse/air@latest
```

### Create `.air.toml` configuration

```toml
root = "."
tmp_dir = "tmp"

[build]
  cmd = "go run generate.go"
  bin = ""
  include_ext = ["go", "json", "html"]
  exclude_dir = ["generated", "tmp"]
  delay = 1000
```

### Run Air

```bash
air
```

This will re-run `generate.go` on any change, making development instant! ⚡

---

## 📚 Additional Resources

- 📘 [Go html/template documentation](https://pkg.go.dev/html/template)
- 🌐 [Goldmark (Markdown parser)](https://github.com/yuin/goldmark)
- 🔥 [Air (Live reload)](https://github.com/air-verse/air)

---

## 🎯 Conclusion

You now have a working static site generator in Go! This is a great foundation for:

- 📝 Personal blogs
- 📚 Documentation sites
- 🌐 Marketing pages
- 📊 Portfolio websites

**Happy generating!** 🚀"""
        print(f"✅ Fixed post 26: {post['title']}")
        break

# Write back to file
with open('allposts.json', 'w', encoding='utf-8') as f:
    json.dump(posts, f, indent=2, ensure_ascii=False)

print("\n🎉 Post 26 fixed successfully!")
