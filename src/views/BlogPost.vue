<template>
  <div class="min-h-screen bg-gradient-to-b from-gray-900 via-gray-900 to-black">
    <!-- Loading State -->
    <div v-if="loading" class="text-center py-20">
      <div class="inline-block animate-spin rounded-full h-16 w-16 border-t-4 border-b-4 border-purple-500"></div>
      <p class="text-gray-400 mt-6 text-lg">Loading post...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="error" class="text-center py-20 px-4">
      <div class="max-w-md mx-auto">
        <p class="text-red-400 text-xl mb-6">{{ error }}</p>
        <router-link 
          to="/blog" 
          class="inline-flex items-center text-purple-400 hover:text-purple-300 text-lg transition-colors"
        >
          <ArrowLeftIcon class="w-5 h-5 mr-2" />
          Back to Blog
        </router-link>
      </div>
    </div>

    <!-- Blog Post Content -->
    <article v-else>
      <!-- Hero Section with Gradient Background -->
      <div class="relative bg-gradient-to-br from-purple-900/40 via-pink-900/40 to-blue-900/40 border-b border-gray-800">
        <div class="max-w-5xl mx-auto px-4 py-12">
          <!-- Back Button -->
          <router-link 
            to="/blog" 
            class="inline-flex items-center text-purple-400 hover:text-purple-300 mb-8 transition-colors group"
          >
            <ArrowLeftIcon class="w-5 h-5 mr-2 group-hover:-translate-x-1 transition-transform" />
            <span class="text-base">Back to Blog</span>
          </router-link>

          <!-- Header -->
          <header class="max-w-4xl">
            <h1 class="text-5xl md:text-6xl font-extrabold text-white mb-6 leading-tight">
              {{ post.title }}
            </h1>
            <p v-if="post.subtitle" class="text-2xl text-gray-300 mb-8 leading-relaxed">
              {{ post.subtitle }}
            </p>
            
            <!-- Meta Info -->
            <div class="flex items-center flex-wrap gap-6 text-sm text-gray-300 mb-6">
              <span class="flex items-center gap-2 bg-gray-800/60 px-4 py-2 rounded-full">
                <UserIcon class="w-4 h-4" />
                {{ post.author }}
              </span>
              <span class="flex items-center gap-2 bg-gray-800/60 px-4 py-2 rounded-full">
                <CalendarIcon class="w-4 h-4" />
                {{ formatDate(post.created_on) }}
              </span>
              <span class="flex items-center gap-2 bg-gray-800/60 px-4 py-2 rounded-full">
                <ClockIcon class="w-4 h-4" />
                {{ post.read_time }}
              </span>
            </div>

            <!-- Tags -->
            <div class="flex flex-wrap gap-2">
              <span 
                v-for="tag in post.tags.split(',').map(t => t.trim()).slice(0, 8)" 
                :key="tag"
                class="text-xs font-medium bg-purple-600/30 text-purple-200 px-4 py-1.5 rounded-full border border-purple-500/30 hover:bg-purple-600/40 transition-colors"
              >
                {{ tag }}
              </span>
            </div>
          </header>
        </div>
      </div>

      <!-- Main Content Area -->
      <div class="max-w-4xl mx-auto px-4 py-12">
        <div class="bg-gray-800/30 backdrop-blur-sm rounded-2xl shadow-2xl border border-gray-700/30 overflow-hidden">
          <div class="p-8 md:p-12">
            <!-- Content -->
            <div 
              class="article-content"
              v-html="renderedContent"
            ></div>
          </div>

          <!-- Footer -->
          <footer class="px-8 md:px-12 py-8 bg-gray-900/30 border-t border-gray-700/30">
            <div class="flex items-center justify-between flex-wrap gap-4">
              <div class="text-sm text-gray-400">
                <span class="inline-block mr-2">📁</span>
                <span>Category:</span>
                <span class="text-purple-400 font-medium ml-2">{{ post.category }}</span>
              </div>
              <div class="text-sm text-gray-500">
                Last updated: {{ formatDate(post.updated_on) }}
              </div>
            </div>
          </footer>
        </div>

        <!-- Back to Blog CTA -->
        <div class="text-center mt-12">
          <router-link 
            to="/blog"
            class="inline-flex items-center gap-2 bg-purple-600 hover:bg-purple-700 text-white px-8 py-3 rounded-lg font-medium transition-all duration-200 shadow-lg hover:shadow-purple-500/50"
          >
            <ArrowLeftIcon class="w-5 h-5" />
            View All Posts
          </router-link>
        </div>
      </div>
    </article>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { marked } from 'marked'
import { 
  ArrowLeftIcon, 
  UserIcon, 
  CalendarIcon, 
  ClockIcon 
} from '@heroicons/vue/24/outline'
import allPostsData from '../../allposts.json'

const route = useRoute()
const router = useRouter()
const loading = ref(true)
const error = ref(null)
const post = ref(null)

// Configure marked options
marked.setOptions({
  breaks: true,
  gfm: true,
  headerIds: true,
  mangle: false,
  sanitize: false,
  smartLists: true,
  smartypants: true
})

const renderedContent = computed(() => {
  if (!post.value || !post.value.content) return ''
  
  // Clean up content before rendering
  let content = post.value.content
  
  // Fix common markdown issues
  content = content.replace(/\$\$/g, '') // Remove double dollar signs if they exist
  content = content.replace(/\\"/g, '"') // Fix escaped quotes
  content = content.replace(/\\'/g, "'") // Fix escaped apostrophes
  
  try {
    return marked(content)
  } catch (err) {
    console.error('Error rendering markdown:', err)
    return '<p>Error rendering content</p>'
  }
})

const formatDate = (dateString) => {
  return new Date(dateString).toLocaleDateString('en-US', {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

onMounted(() => {
  try {
    const slug = route.params.slug
    console.log('Looking for slug:', slug)
    console.log('Available posts:', allPostsData.length)
    
    const foundPost = allPostsData.find(p => p.slug === slug && p.published === "1")
    
    if (foundPost) {
      console.log('Found post:', foundPost.title)
      post.value = foundPost
      loading.value = false
    } else {
      console.log('Post not found')
      error.value = 'Blog post not found'
      loading.value = false
    }
  } catch (err) {
    console.error('Error loading post:', err)
    error.value = 'Failed to load blog post'
    loading.value = false
  }
})
</script>

<style scoped>
/* Article Content Styling - Enhanced Typography */
.article-content {
  color: #e5e7eb;
  font-size: 1.125rem;
  line-height: 1.8;
}

/* Headings */
.article-content :deep(h1) {
  color: #ffffff;
  font-size: 2.5rem;
  font-weight: 800;
  margin-top: 3rem;
  margin-bottom: 1.5rem;
  line-height: 1.2;
  letter-spacing: -0.02em;
  background: linear-gradient(135deg, #a78bfa 0%, #ec4899 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.article-content :deep(h1:first-child) {
  margin-top: 0;
}

.article-content :deep(h2) {
  color: #ffffff;
  font-size: 2rem;
  font-weight: 700;
  margin-top: 2.5rem;
  margin-bottom: 1.25rem;
  padding-bottom: 0.75rem;
  border-bottom: 2px solid #4b5563;
  line-height: 1.3;
  letter-spacing: -0.01em;
}

.article-content :deep(h3) {
  color: #f3f4f6;
  font-size: 1.5rem;
  font-weight: 600;
  margin-top: 2rem;
  margin-bottom: 1rem;
  line-height: 1.4;
}

.article-content :deep(h4) {
  color: #f3f4f6;
  font-size: 1.25rem;
  font-weight: 600;
  margin-top: 1.75rem;
  margin-bottom: 0.875rem;
  line-height: 1.4;
}

.article-content :deep(h5) {
  color: #f3f4f6;
  font-size: 1.125rem;
  font-weight: 600;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

.article-content :deep(h6) {
  color: #d1d5db;
  font-size: 1rem;
  font-weight: 600;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

/* Paragraphs */
.article-content :deep(p) {
  margin-bottom: 1.5rem;
  line-height: 1.8;
  color: #d1d5db;
}

/* Links */
.article-content :deep(a) {
  color: #a78bfa;
  text-decoration: none;
  font-weight: 500;
  border-bottom: 1px solid #a78bfa;
  transition: all 0.2s ease;
}

.article-content :deep(a:hover) {
  color: #c4b5fd;
  border-bottom-color: #c4b5fd;
  background-color: #a78bfa10;
}

/* Inline Code */
.article-content :deep(code) {
  background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
  color: #f472b6;
  padding: 0.25rem 0.5rem;
  border-radius: 0.375rem;
  font-size: 0.9em;
  font-family: 'Monaco', 'Menlo', 'Ubuntu Mono', monospace;
  border: 1px solid #374151;
  font-weight: 500;
}

/* Code Blocks */
.article-content :deep(.code-block-wrapper) {
  margin: 2rem 0;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  border: 1px solid #334155;
}

.article-content :deep(.code-block-header) {
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  padding: 0.75rem 1.5rem;
  border-bottom: 1px solid #334155;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.article-content :deep(.code-language) {
  color: #a78bfa;
  font-size: 0.75rem;
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.article-content :deep(.code-block-wrapper pre) {
  margin: 0;
  border: none;
  border-radius: 0;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
}

.article-content :deep(pre) {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  border: 1px solid #334155;
  border-radius: 0.75rem;
  padding: 1.5rem;
  overflow-x: auto;
  margin: 2rem 0;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
  position: relative;
}

.article-content :deep(pre code) {
  background: transparent;
  color: #e2e8f0;
  padding: 0;
  border: none;
  font-size: 0.95rem;
  line-height: 1.6;
  display: block;
}

/* Scrollbar for code blocks */
.article-content :deep(pre::-webkit-scrollbar) {
  height: 8px;
}

.article-content :deep(pre::-webkit-scrollbar-track) {
  background: #1e293b;
  border-radius: 4px;
}

.article-content :deep(pre::-webkit-scrollbar-thumb) {
  background: #475569;
  border-radius: 4px;
}

.article-content :deep(pre::-webkit-scrollbar-thumb:hover) {
  background: #64748b;
}

/* Lists */
.article-content :deep(ul),
.article-content :deep(ol) {
  margin-bottom: 1.5rem;
  padding-left: 0.5rem;
  color: #d1d5db;
}

.article-content :deep(ul) {
  list-style-type: none;
}

.article-content :deep(ul li) {
  position: relative;
  margin-bottom: 0.75rem;
  padding-left: 0;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}

.article-content :deep(ul li::before) {
  content: "●";
  color: #a78bfa;
  font-size: 1.2em;
  line-height: 1.4;
  flex-shrink: 0;
  margin-top: 0.1em;
}

.article-content :deep(ol) {
  list-style-type: decimal;
  list-style-position: outside;
  padding-left: 1.5rem;
}

.article-content :deep(ol li) {
  margin-bottom: 0.75rem;
  padding-left: 0.5rem;
}

.article-content :deep(li) {
  line-height: 1.7;
}

.article-content :deep(li > ul),
.article-content :deep(li > ol) {
  margin-top: 0.75rem;
  margin-bottom: 0.5rem;
  padding-left: 1.5rem;
}

.article-content :deep(li > ul li) {
  margin-bottom: 0.5rem;
}

/* Blockquotes */
.article-content :deep(blockquote) {
  border-left: 4px solid #a78bfa;
  background: linear-gradient(90deg, #a78bfa15 0%, transparent 100%);
  padding: 1rem 1.5rem;
  margin: 2rem 0;
  border-radius: 0 0.5rem 0.5rem 0;
  color: #d1d5db;
  font-style: italic;
  position: relative;
}

.article-content :deep(blockquote p) {
  margin-bottom: 0.5rem;
}

.article-content :deep(blockquote p:last-child) {
  margin-bottom: 0;
}

/* Tables */
.article-content :deep(table) {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin: 2rem 0;
  font-size: 0.95rem;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
}

.article-content :deep(thead) {
  background: linear-gradient(135deg, #1f2937 0%, #111827 100%);
}

.article-content :deep(th) {
  color: #ffffff;
  font-weight: 600;
  padding: 1rem;
  text-align: left;
  border-bottom: 2px solid #374151;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.article-content :deep(td) {
  padding: 1rem;
  border-bottom: 1px solid #374151;
  color: #d1d5db;
}

.article-content :deep(tbody tr) {
  background-color: #1f2937;
  transition: background-color 0.2s ease;
}

.article-content :deep(tbody tr:hover) {
  background-color: #374151;
}

.article-content :deep(tbody tr:nth-child(even)) {
  background-color: #111827;
}

.article-content :deep(tbody tr:nth-child(even):hover) {
  background-color: #374151;
}

/* Images */
.article-content :deep(img) {
  border-radius: 0.75rem;
  margin: 2rem auto;
  max-width: 100%;
  height: auto;
  display: block;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.4);
  border: 1px solid #374151;
}

/* Horizontal Rules */
.article-content :deep(hr) {
  border: 0;
  height: 2px;
  background: linear-gradient(90deg, transparent, #4b5563, transparent);
  margin: 3rem 0;
}

/* Strong and Emphasis */
.article-content :deep(strong) {
  color: #ffffff;
  font-weight: 700;
}

.article-content :deep(em) {
  font-style: italic;
  color: #e5e7eb;
}

.article-content :deep(mark) {
  background-color: #fbbf24;
  color: #000000;
  padding: 0.1rem 0.3rem;
  border-radius: 0.25rem;
}

/* Keyboard keys */
.article-content :deep(kbd) {
  background-color: #1f2937;
  color: #e5e7eb;
  padding: 0.2rem 0.5rem;
  border-radius: 0.25rem;
  border: 1px solid #374151;
  font-family: monospace;
  font-size: 0.9em;
  box-shadow: 0 2px 0 #374151;
}

/* Subscript and Superscript */
.article-content :deep(sub),
.article-content :deep(sup) {
  font-size: 0.75em;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}

.article-content :deep(sup) {
  top: -0.5em;
}

.article-content :deep(sub) {
  bottom: -0.25em;
}

/* Definition Lists */
.article-content :deep(dl) {
  margin: 1.5rem 0;
}

.article-content :deep(dt) {
  color: #ffffff;
  font-weight: 600;
  margin-top: 1rem;
}

.article-content :deep(dd) {
  margin-left: 2rem;
  margin-bottom: 0.5rem;
  color: #d1d5db;
}

/* Abbreviations */
.article-content :deep(abbr) {
  text-decoration: underline dotted;
  cursor: help;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .article-content {
    font-size: 1rem;
  }
  
  .article-content :deep(h1) {
    font-size: 2rem;
  }
  
  .article-content :deep(h2) {
    font-size: 1.75rem;
  }
  
  .article-content :deep(h3) {
    font-size: 1.375rem;
  }
  
  .article-content :deep(pre) {
    padding: 1rem;
    font-size: 0.85rem;
  }
  
  .article-content :deep(table) {
    font-size: 0.875rem;
  }
  
  .article-content :deep(th),
  .article-content :deep(td) {
    padding: 0.75rem;
  }
}
</style>
