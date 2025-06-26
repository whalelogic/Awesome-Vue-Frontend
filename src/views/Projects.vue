<template>
  <div class="max-w-5xl mx-auto px-4 py-10">
    <div class="text-center mb-10">
      <h1 class="text-3xl font-bold text-white mb-4">Projects</h1>
      <p class="text-gray-400 max-w-2xl mx-auto">
        A collection of projects showcasing my expertise in full-stack development, 
        system architecture, and cutting-edge technologies.
      </p>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <div 
        v-for="project in projects" 
        :key="project.id"
        class="project-card"
      >
        <div class="flex items-start justify-between mb-4">
          <div class="flex items-center space-x-3">
            <component :is="project.icon" class="w-8 h-8 text-purple-400" />
            <h3 class="text-xl font-semibold text-white">{{ project.title }}</h3>
          </div>
          <div class="flex space-x-2">
            <a 
              v-if="project.github"
              :href="project.github" 
              target="_blank"
              class="text-gray-400 hover:text-white transition-colors"
            >
              <CodeBracketIcon class="w-5 h-5" />
            </a>
            <a 
              v-if="project.demo"
              :href="project.demo" 
              target="_blank"
              class="text-gray-400 hover:text-white transition-colors"
            >
              <ArrowTopRightOnSquareIcon class="w-5 h-5" />
            </a>
          </div>
        </div>
        
        <p class="text-gray-400 mb-4">{{ project.description }}</p>
        
        <div class="flex flex-wrap gap-2 mb-4">
          <span 
            v-for="tech in project.technologies" 
            :key="tech"
            class="text-xs bg-gray-700 text-gray-300 px-2 py-1 rounded-full"
          >
            {{ tech }}
          </span>
        </div>
        
        <div class="text-sm text-gray-500">
          {{ project.status }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { 
  CodeBracketIcon, 
  ArrowTopRightOnSquareIcon,
  CpuChipIcon,
  CloudIcon,
  ShieldCheckIcon,
  ChartBarIcon,
  CubeIcon,
  ServerIcon
} from '@heroicons/vue/24/outline'

const projects = [
  {
    id: 1,
    title: 'RAG Agent Platform',
    description: 'A comprehensive platform for building and deploying retrieval-augmented generation agents with vector databases and LLM integration.',
    technologies: ['Go', 'Langchaingo', 'Weaviate', 'OpenAI', 'Docker'],
    status: 'Production Ready',
    github: 'https://github.com',
    demo: 'https://demo.com',
    icon: CpuChipIcon
  },
  {
    id: 2,
    title: 'Cloud Native Microservices',
    description: 'Scalable microservices architecture built with Go and deployed on Kubernetes with advanced monitoring and observability.',
    technologies: ['Go', 'Kubernetes', 'gRPC', 'Prometheus', 'Grafana'],
    status: 'Active Development',
    github: 'https://github.com',
    icon: CloudIcon
  },
  {
    id: 3,
    title: 'Secure API Gateway',
    description: 'High-performance API gateway with authentication, rate limiting, and request/response transformation capabilities.',
    technologies: ['Rust', 'Actix-web', 'Redis', 'JWT', 'PostgreSQL'],
    status: 'Production Ready',
    github: 'https://github.com',
    demo: 'https://demo.com',
    icon: ShieldCheckIcon
  },
  {
    id: 4,
    title: 'Real-time Analytics Dashboard',
    description: 'Interactive dashboard for real-time data visualization with WebSocket connections and streaming data processing.',
    technologies: ['Python', 'FastAPI', 'WebSockets', 'React', 'D3.js'],
    status: 'Completed',
    github: 'https://github.com',
    demo: 'https://demo.com',
    icon: ChartBarIcon
  },
  {
    id: 5,
    title: 'Blockchain Data Indexer',
    description: 'High-throughput blockchain data indexer and API for querying transaction history and smart contract events.',
    technologies: ['Go', 'PostgreSQL', 'GraphQL', 'Docker', 'Redis'],
    status: 'Active Development',
    github: 'https://github.com',
    icon: CubeIcon
  },
  {
    id: 6,
    title: 'Distributed Cache System',
    description: 'Custom distributed caching solution with consistent hashing, replication, and automatic failover mechanisms.',
    technologies: ['Rust', 'gRPC', 'Raft Consensus', 'Docker', 'Kubernetes'],
    status: 'Research Phase',
    github: 'https://github.com',
    icon: ServerIcon
  }
]
</script>