<template>
  <div class="max-w-4xl mx-auto px-4 py-10">
    <div class="text-center mb-10">
      <h1 class="text-3xl font-bold text-white mb-4">About Me</h1>
      <p class="text-gray-400 text-lg">
        Full Stack Developer & System Architect
      </p>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
      <div class="lg:col-span-2 space-y-6">
        <div class="bg-gray-800 rounded-lg p-6">
          <h2 class="text-xl font-semibold text-white mb-4 flex items-center">
            <UserIcon class="w-6 h-6 mr-2 text-purple-400" />
            Background
          </h2>
          <p class="text-gray-400 leading-relaxed mb-4">
  I’m Keith Thomson — a former Army Squad Leader and entrenenpuer talented in designing and scaling efficient systems. The passion I found in Computer Science was like nothing I've encountered before. It's challenging and ever-changing environment is what drives me to keep learning and enhancing my skills. After serving on active duty (2007–2011) and contracting in financial analysis for the U.S. Navy, I used my G.I. Bill and earned an AS in Computer Science followed by a BS in Information Systems with a minor in Philosphy. 
  <br>
  <br>Since then I’ve designed and delivered mission-critical web and API solutions—spanning Flask, Django, FastAPI and Gin—with MariaDB, PostgreSQL, and cloud-native infrastructures on DigitalOcean and AWS. I specialize in architecting, deploying, and administering cloud infrastructures—ensuring they are scalable, reliable, and secure.

</p>
<p class="text-gray-400 leading-relaxed">
  Today I specialize in high-performance back-ends and modern front-ends, leveraging Go, Rust, and Python to build microservices, business-intelligence pipelines, and RAG-powered agents. My passion lies at the intersection of traditional software engineering and AI/ML—designing scalable systems, retrieval-augmented workflows, and intelligent agents that drive real-world impact.
</p>

        </div>

        <div class="bg-gray-800 rounded-lg p-6">
          <h2 class="text-xl font-semibold text-white mb-4 flex items-center">
            <BriefcaseIcon class="w-6 h-6 mr-2 text-purple-400" />
            Experience
          </h2>
          <div class="space-y-4">
            <div v-for="job in experience" :key="job.id" class="border-l-2 border-purple-600 pl-4">
              <h3 class="text-white font-semibold">{{ job.title }}</h3>
              <p class="text-purple-400 text-sm">{{ job.company }} • {{ job.period }}</p>
              <p class="text-gray-400 text-sm mt-2">{{ job.description }}</p>
            </div>
          </div>
        </div>
      </div>

      <div class="space-y-6">
        <div class="bg-gray-800 rounded-lg p-6">
          <h2 class="text-xl font-semibold text-white mb-4 flex items-center">
            <WrenchScrewdriverIcon class="w-6 h-6 mr-2 text-purple-400" />
            Skills
          </h2>
          <div class="space-y-4">
            <div v-for="category in skillCategories" :key="category.name">
              <h3 class="text-white font-medium mb-2">{{ category.name }}</h3>
              <div class="flex flex-wrap gap-2">
                <span 
                  v-for="skill in category.skills" 
                  :key="skill"
                  class="text-xs bg-purple-700/20 text-purple-300 px-2 py-1 rounded-full"
                >
                  {{ skill }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <div class="bg-gray-800 rounded-lg p-6">
          <h2 class="text-xl font-semibold text-white mb-4 flex items-center">
            <EnvelopeIcon class="w-6 h-6 mr-2 text-purple-400" />
            Contact
          </h2>
          <div class="space-y-3">
            <a 
              v-for="contact in contacts" 
              :key="contact.label"
              :href="contact.href" 
              class="flex items-center text-gray-400 hover:text-white transition-colors"
            >
              <component :is="contact.icon" class="w-5 h-5 mr-3" />
              {{ contact.label }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { 
  UserIcon, 
  BriefcaseIcon, 
  WrenchScrewdriverIcon, 
  EnvelopeIcon,
  AtSymbolIcon,
  DevicePhoneMobileIcon
} from '@heroicons/vue/24/outline'

const experience = [
  {
    id: 1,
    title: 'Product QA & Web Content Manager',
    company: 'PennyBorne Development (Remote – Detroit, MI)',
    period: '2023 – Present',
    description: 'Oversee QA processes, manage and curate website content, source and structure business data, administer internal databases, and coordinate directly with clients to align digital strategy with operational goals.'
  },
  {
    id: 2,
    title: 'Assistant Manager',
    company: 'The Spice & Tea Exchange – Mystic, CT',
    period: '2017 – 2021',
    description: 'Managed daily retail operations, optimized inventory control, and led a sales team to increase store revenue by over 25%. Developed customer loyalty initiatives and trained staff in product knowledge and service excellence.'
  },
  {
    id: 3,
    title: 'Financial Accounting Clerk II',
    company: 'The Magetti Group / Various Federal Contracts',
    period: '2012 – 2016',
    description: 'Provided data analytics and financial systems support for U.S. Navy contracts. Delivered operational insights and managed backend data systems for logistics and accounting functions.'
  },
  {
    id: 4,
    title: 'Infantry Squad Leader (NCO)',
    company: 'U.S. Army – Active Duty',
    period: '2007 – 2011',
    description: 'Led combat infantry operations, coordinated mission-critical logistics, and managed team training and field execution under high-stakes conditions.'
  }
]


const skillCategories = [
  {
    name: 'Languages',
    skills: ['Go', 'Rust', 'Python', 'C++', 'TypeScript']
  },
  {
    name: 'Backend',
    skills: ['gRPC', 'REST APIs', 'GraphQL', 'Microservices', 'JSON Web Tokens', 'oAuth']
  },
  {
    name: 'Databases',
    skills: ['PostgreSQL', 'Redis', 'MongoDB', 'Weaviate']
  },
  {
    name: 'Cloud & DevOps',
    skills: ['Docker', 'Kubernetes', 'AWS', 'IAM/Auth', 'AWS S3', 'DynamoDB', 'ELB']
  },
  {
    name: 'AI/ML',
    skills: ['OpenAI', 'Langchain', 'RAG', 'Vector Databases', 'Embedding Models', 'Inferencing', 'Data Labeling']
  }
]

const contacts = [
  {
    label: 'thomsonk2@southernct.edu',
    href: 'mailto:thomsonk2@southernct.edu',
    icon: AtSymbolIcon
  },
  {
    label: 'thomsonk930@gmail.com',
    href: 'mailto:thomsonk930@gmail.com',
    icon: AtSymbolIcon
  },
  {
    label: '+1 (860) 405-7837',
    href: 'tel:+18604057837',
    icon: DevicePhoneMobileIcon
  }
]
</script>
