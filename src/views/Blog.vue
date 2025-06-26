<template>
  <div class="max-w-4xl mx-auto px-4 py-10">
    <div class="text-center mb-10">
      <h1 class="text-3xl font-bold text-white mb-4">Blog</h1>
      <p class="text-gray-400 max-w-2xl mx-auto">
        Technical insights, tutorials, and thoughts on software development, 
        system design, and emerging technologies.
      </p>
    </div>

    <!-- Featured Post -->
    <div class="bg-gradient-to-r from-purple-900/50 to-pink-900/50 rounded-lg p-8 mb-12">
      <div class="flex items-center space-x-2 mb-3">
        <StarIcon class="w-5 h-5 text-yellow-400" />
        <span class="text-yellow-400 text-sm font-medium">Featured Post</span>
      </div>
      <h2 class="text-2xl font-bold text-white mb-3">{{ featuredPost.title }}</h2>
      <p class="text-gray-300 mb-4">{{ featuredPost.description }}</p>
      <div class="flex items-center justify-between">
        <div class="flex flex-wrap gap-2">
          <span 
            v-for="tag in featuredPost.tags" 
            :key="tag"
            class="text-xs bg-white/10 text-white px-2 py-1 rounded-full"
          >
            {{ tag }}
          </span>
        </div>
        <span class="text-gray-400 text-sm">{{ featuredPost.date }}</span>
      </div>
    </div>

    <!-- Search and Filter -->
    <div class="flex flex-col sm:flex-row gap-4 mb-8">
      <div class="flex-1">
        <div class="relative">
          <MagnifyingGlassIcon class="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" />
          <input
            v-model="searchQuery"
            type="text"
            placeholder="Search articles..."
            class="w-full pl-10 pr-4 py-2 bg-gray-800 border border-gray-700 rounded-lg text-white placeholder-gray-400 focus:outline-none focus:border-purple-500"
          />
        </div>
      </div>
      <select 
        v-model="selectedCategory"
        class="px-4 py-2 bg-gray-800 border border-gray-700 rounded-lg text-white focus:outline-none focus:border-purple-500"
      >
        <option value="">All Categories</option>
        <option v-for="category in categories" :key="category" :value="category">
          {{ category }}
        </option>
      </select>
    </div>

    <!-- Blog Posts -->
    <div class="space-y-8">
      <article 
        v-for="post in filteredPosts" 
        :key="post.id"
        class="bg-gray-800 rounded-lg p-6 hover:bg-gray-750 transition-colors duration-200"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h2 class="text-xl font-semibold text-white mb-2 hover:text-purple-400 cursor-pointer">
              {{ post.title }}
            </h2>
            <p class="text-gray-400 mb-3">{{ post.excerpt }}</p>
            <div class="flex items-center space-x-4 text-sm text-gray-500">
              <span class="flex items-center">
                <CalendarIcon class="w-4 h-4 mr-1" />
                {{ post.date }}
              </span>
              <span class="flex items-center">
                <ClockIcon class="w-4 h-4 mr-1" />
                {{ post.readTime }} min read
              </span>
            </div>
          </div>
          <img 
            :src="post.image" 
            :alt="post.title"
            class="w-24 h-24 rounded-lg object-cover ml-6"
          />
        </div>
        
        <div class="flex items-center justify-between">
          <div class="flex flex-wrap gap-2">
            <span 
              v-for="tag in post.tags" 
              :key="tag"
              class="text-xs bg-purple-700/20 text-purple-300 px-2 py-1 rounded-full"
            >
              {{ tag }}
            </span>
          </div>
          <button class="text-purple-400 hover:text-purple-300 text-sm font-medium flex items-center">
            Read more
            <ArrowRightIcon class="w-4 h-4 ml-1" />
          </button>
        </div>
      </article>
    </div>

    <!-- Load More -->
    <div class="text-center mt-12">
      <button class="bg-purple-600 hover:bg-purple-700 text-white px-6 py-3 rounded-lg font-medium transition-colors duration-200">
        Load More Articles
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { 
  StarIcon, 
  MagnifyingGlassIcon, 
  CalendarIcon, 
  ClockIcon, 
  ArrowRightIcon 
} from '@heroicons/vue/24/outline'

const searchQuery = ref('')
const selectedCategory = ref('')

const featuredPost = {
  title: 'Building Production-Ready RAG Systems: A Complete Guide',
  description: 'Learn how to build, deploy, and scale retrieval-augmented generation systems in production environments with real-world examples and best practices.',
  tags: ['RAG', 'Production', 'AI', 'System Design'],
  date: 'July 15, 2025'
}

const categories = ['System Design', 'Go', 'Rust', 'Python', 'AI/ML', 'DevOps', 'Database']

const blogPosts = [
  {
    id: 1,
    title: 'Building RAG Agents with Golang and OpenAI',
    excerpt: 'An engineering guide to developing retrieval augmented generation systems using Langchaingo, Weaviate, and Docker.',
    date: 'June 22, 2025',
    readTime: 12,
    tags: ['RAG', 'Golang', 'Langchaingo', 'OpenAI'],
    category: 'AI/ML',
    image: 'https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=100&h=100&dpr=1'
  },
  {
    id: 2,
    title: 'Rust-Powered APIs with Rocket & PostgreSQL',
    excerpt: 'A breakdown of how to architect secure and performant web APIs using Rust and PostgreSQL.',
    date: 'May 14, 2025',
    readTime: 8,
    tags: ['Rust', 'PostgreSQL', 'WebAPI'],
    category: 'Rust',
    image: 'https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=100&h=100&dpr=1'
  },
  {
    id: 3,
    title: 'Microservices Communication Patterns in Go',
    excerpt: 'Exploring different communication patterns for microservices including gRPC, message queues, and event-driven architectures.',
    date: 'April 28, 2025',
    readTime: 15,
    tags: ['Go', 'Microservices', 'gRPC', 'Architecture'],
    category: 'System Design',
    image: 'https://images.pexels.com/photos/1181677/pexels-photo-1181677.jpeg?auto=compress&cs=tinysrgb&w=100&h=100&dpr=1'
  },
  {
    id: 4,
    title: 'Optimizing Database Performance for High-Traffic Applications',
    excerpt: 'Practical strategies for database optimization, indexing, and query performance in production environments.',
    date: 'April 10, 2025',
    readTime: 10,
    tags: ['Database', 'Performance', 'PostgreSQL', 'Optimization'],
    category: 'Database',
    image: 'https://images.pexels.com/photos/1181298/pexels-photo-1181298.jpeg?auto=compress&cs=tinysrgb&w=100&h=100&dpr=1'
  },
  {
    id: 5,
    title: 'Container Orchestration with Kubernetes: Best Practices',
    excerpt: 'A comprehensive guide to deploying and managing containerized applications with Kubernetes in production.',
    date: 'March 22, 2025',
    readTime: 18,
    tags: ['Kubernetes', 'Docker', 'DevOps', 'Container'],
    category: 'DevOps',
    image: 'https://images.pexels.com/photos/1181271/pexels-photo-1181271.jpeg?auto=compress&cs=tinysrgb&w=100&h=100&dpr=1'
  }
]

const filteredPosts = computed(() => {
  let filtered = blogPosts

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    filtered = filtered.filter(post => 
      post.title.toLowerCase().includes(query) ||
      post.excerpt.toLowerCase().includes(query) ||
      post.tags.some(tag => tag.toLowerCase().includes(query))
    )
  }

  if (selectedCategory.value) {
    filtered = filtered.filter(post => post.category === selectedCategory.value)
  }

  return filtered
})
</script>