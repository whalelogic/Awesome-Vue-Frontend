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
          class="post-card"
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
              <router-link 
                to="/blog" 
                class="inline-flex items-center text-purple-400 hover:text-purple-300 text-sm font-medium"
              >
                Read more
                <ArrowRightIcon class="w-4 h-4 ml-1" />
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { ArrowRightIcon } from '@heroicons/vue/24/outline'

const skills = [
  'Go', 'Rust', 'Python', 'System Design', 'Cloud Native', 'RAG Agents',
  'DevOps', 'Database Architecture', 'Security', 'API Design'
]

const posts = [
  {
    id: 1,
    date: 'June 22, 2025',
    title: 'Building RAG Agents with Golang and OpenAI',
    description: 'An engineering guide to developing retrieval augmented generation systems using Langchaingo, Weaviate, and Docker.',
    tags: ['RAG', 'Golang', 'Langchaingo', 'OpenAI'],
    image: 'https://images.pexels.com/photos/546819/pexels-photo-546819.jpeg?auto=compress&cs=tinysrgb&w=280&h=180&dpr=1'
  },
  {
    id: 2,
    date: 'May 14, 2025',
    title: 'Rust-Powered APIs with Rocket & PostgreSQL',
    description: 'A breakdown of how to architect secure and performant web APIs using Rust and PostgreSQL.',
    tags: ['Rust', 'PostgreSQL', 'WebAPI'],
    image: 'https://images.pexels.com/photos/1181675/pexels-photo-1181675.jpeg?auto=compress&cs=tinysrgb&w=280&h=180&dpr=1'
  }
]
</script>
