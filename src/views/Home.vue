<template>
  <div class="max-w-5xl mx-auto px-4 py-10">
    <!-- Header -->
    <div class="text-center mb-10">
      <!-- Fixed horizontal alignment of profile info -->
      <div class="flex items-center justify-center space-x-6 mb-6">
        <img 
          src="/meandsophia.jpeg" 
          class="w-24 h-24 rounded-full border-4 border-pink-600 object-cover" 
          :style="{ transform: 'rotate(180deg)' }"
          alt="Keith Thomson Profile" 
        />
        <div class="text-left">
          <h1 class="text-3xl font-bold text-white">Keith Thomson</h1>
          <div class="flex items-center space-x-2 mt-1">
            <div class="w-3 h-3 bg-green-400 rounded-full animate-pulse"></div>
            <span class="text-sm text-green-400 font-semibold">Available</span>
          </div>
        </div>
      </div>
      
      <h2 class="text-xl font-semibold text-white mb-3">Full Stack Developer</h2>
      <p class="text-gray-400 max-w-2xl mx-auto mb-6">
        I'm a dedicated developer focused on building scalable systems, RAG agents, and performant full-stack apps. 
        I specialize in Go, Rust, and Python integrations.
      </p>
      
      <div class="flex flex-wrap justify-center gap-2">
        <span 
          v-for="skill in skills" 
          :key="skill" 
          class="skill-tag"
        >
          {{ skill }}
        </span>
      </div>
    </div>

    <!-- Latest Posts -->
    <section>
      <h2 class="text-2xl font-bold mb-2">Latest</h2>
      <p class="text-gray-400 mb-6">
        Insights, guides, and articles on cutting-edge tech, systems design, and modern APIs.
      </p>

      <div class="space-y-6">
        <div 
          v-for="post in posts" 
          :key="post.id" 
          class="post-card cursor-pointer"
          @click="$router.push(`/blog/${post.slug}`)"
        >
          <div class="flex flex-col md:flex-row gap-6">
            <img 
              :src="post.image" 
              class="w-full md:w-60 h-48 md:h-36 rounded-lg object-cover" 
              :alt="post.title" 
            />
            <div class="flex-1">
              <div class="text-sm text-gray-400 mb-1">{{ post.date }}</div>
              <h3 class="text-white text-lg font-semibold mb-2">{{ post.title }}</h3>
              <p class="text-gray-400 mb-3">{{ post.description }}</p>
              <div class="flex flex-wrap gap-2 mb-3">
                <span 
                  v-for="tag in post.tags" 
                  :key="tag" 
                  class="text-xs bg-purple-700/20 text-purple-300 px-2 py-1 rounded-full"
                >
                  {{ tag }}
                </span>
              </div>
              <div class="inline-flex items-center text-purple-400 hover:text-purple-300 text-sm font-medium">
                Read more
                <ArrowRightIcon class="w-4 h-4 ml-1" />
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ArrowRightIcon } from '@heroicons/vue/24/outline'
import allPostsData from '../../allposts.json'

const skills = [
  'Go', 'Rust', 'Python', 'System Design', 'Cloud Native', 'RAG Agents',
  'DevOps', 'Database Architecture', 'Security', 'API Design'
]

// Colorful images from Unsplash
const colorfulImages = [
  'https://images.unsplash.com/photo-1557672172-298e090bd0f1?w=400&h=300&fit=crop', // Abstract colorful
  'https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&h=300&fit=crop', // Colorful gradient
  'https://images.unsplash.com/photo-1567095761054-7a02e69e5c43?w=400&h=300&fit=crop', // Tech abstract
  'https://images.unsplash.com/photo-1550745165-9bc0b252726f?w=400&h=300&fit=crop', // Colorful tech
  'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=400&h=300&fit=crop', // Earth tech
  'https://images.unsplash.com/photo-1558494949-ef010cbdcc31?w=400&h=300&fit=crop', // Neon
]

// Process posts from JSON - show latest 3 posts
const posts = allPostsData
  .filter(post => post.published === "1")
  .sort((a, b) => new Date(b.created_on) - new Date(a.created_on))
  .slice(0, 3)
  .map((post, index) => ({
    id: post.id,
    date: new Date(post.created_on).toLocaleDateString('en-US', { 
      year: 'numeric', 
      month: 'long', 
      day: 'numeric' 
    }),
    title: post.title,
    description: post.summary || post.subtitle,
    tags: post.tags.split(',').map(tag => tag.trim()).slice(0, 4),
    image: colorfulImages[index % colorfulImages.length],
    slug: post.slug
  }))
</script>
