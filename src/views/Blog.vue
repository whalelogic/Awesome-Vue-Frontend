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
    <div 
      class="bg-gradient-to-r from-purple-900/50 to-pink-900/50 rounded-lg p-8 mb-12 cursor-pointer hover:from-purple-900/60 hover:to-pink-900/60 transition-all duration-200"
      @click="$router.push(`/blog/${featuredPost.slug}`)"
    >
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
        class="bg-gray-800 rounded-lg p-6 hover:bg-gray-750 transition-colors duration-200 cursor-pointer"
        @click="$router.push(`/blog/${post.slug}`)"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="flex-1">
            <h2 class="text-xl font-semibold text-white mb-2 hover:text-purple-400">
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
import allPostsData from '../../allposts.json'

const searchQuery = ref('')
const selectedCategory = ref('')

// Colorful images from Unsplash
const colorfulImages = [
  'https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=400&h=300&fit=crop', // Abstract colorful
  'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=300&fit=crop', // Colorful gradient
  'https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?w=400&h=300&fit=crop', // Tech abstract
  'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400&h=300&fit=crop', // Colorful tech
  'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&h=300&fit=crop', // Earth tech
  'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=400&h=300&fit=crop', // Neon
  'https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=400&h=300&fit=crop', // Purple abstract
  'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=400&h=300&fit=crop', // Abstract art
]

// Process posts from JSON
const blogPosts = allPostsData
  .filter(post => post.published === "1")
  .map((post, index) => ({
    id: post.id,
    title: post.title,
    excerpt: post.summary || post.subtitle,
    date: new Date(post.created_on).toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    }),
    readTime: parseInt(post.read_time) || 5,
    tags: post.tags.split(',').map(tag => tag.trim()).slice(0, 4),
    category: post.category,
    image: colorfulImages[index % colorfulImages.length],
    slug: post.slug,
    content: post.content
  }))

// Get featured post
const featuredPost = computed(() => {
  const featured = allPostsData.find(post => post.featured === "1" && post.published === "1")
  if (featured) {
    return {
      title: featured.title,
      description: featured.summary || featured.subtitle,
      tags: featured.tags.split(',').map(tag => tag.trim()).slice(0, 4),
      date: new Date(featured.created_on).toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
      }),
      slug: featured.slug
    }
  }
  return {
    title: blogPosts[0]?.title || 'No posts available',
    description: blogPosts[0]?.excerpt || '',
    tags: blogPosts[0]?.tags || [],
    date: blogPosts[0]?.date || '',
    slug: blogPosts[0]?.slug || ''
  }
})

// Extract unique categories
const categories = computed(() => {
  const cats = new Set()
  allPostsData.forEach(post => {
    if (post.published === "1" && post.category) {
      post.category.split(',').forEach(cat => cats.add(cat.trim()))
    }
  })
  return Array.from(cats).sort()
})

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
    filtered = filtered.filter(post => 
      post.category.toLowerCase().includes(selectedCategory.value.toLowerCase())
    )
  }

  return filtered
})
</script>