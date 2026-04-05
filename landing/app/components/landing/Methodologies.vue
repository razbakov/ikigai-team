<script setup lang="ts">
const methods = [
  {
    name: 'Ikigai',
    description: 'Find your purpose. Delegate everything else. The team exists so you can focus on what only you can do.',
    icon: 'lucide:compass',
    color: 'text-purple-500',
  },
  {
    name: 'Level 10 Life',
    description: 'Score 10 life areas, track trends over time, catch burnout before it hits. Sage runs assessments regularly.',
    icon: 'lucide:heart-pulse',
    color: 'text-green-500',
  },
  {
    name: 'GROW',
    description: 'Goal, Reality, Options, Way Forward. The coaching framework that turns reflection into action.',
    icon: 'lucide:route',
    color: 'text-pink-500',
  },
  {
    name: 'OKRs',
    description: 'Quarterly objectives cascade to every agent. Marco tracks progress and challenges anything that does not move the needle.',
    icon: 'lucide:target',
    color: 'text-yellow-500',
  },
  {
    name: 'GTD',
    description: 'Inbox processing, next actions, weekly reviews. Maya runs Getting Things Done so nothing slips through.',
    icon: 'lucide:inbox',
    color: 'text-cyan-500',
  },
  {
    name: 'Sociocracy 3.0',
    description: 'Clear domains, consent-based decisions, decision authority matrix. Every agent knows their boundaries.',
    icon: 'lucide:git-branch',
    color: 'text-blue-500',
  },
  {
    name: 'CRM',
    description: 'Meet someone, send a screenshot. Kai researches them, enriches the profile, and tracks follow-ups.',
    icon: 'lucide:users',
    color: 'text-orange-500',
  },
  {
    name: 'Scrum',
    description: 'Daily standups, sprint planning, retrospectives. Maya reports what each agent accomplished and flags blockers.',
    icon: 'lucide:list-checks',
    color: 'text-red-500',
  },
]
</script>

<template>
  <section class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">Everything Built In</h2>
        <p class="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto">
          You do not have to learn these methodologies first. The team teaches you as you go.
        </p>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div
          v-for="method in methods"
          :key="method.name"
          class="bg-card border border-border rounded-xl p-5 hover:border-primary/30 transition-colors"
        >
          <Icon :name="method.icon" class="w-6 h-6 mb-3" :class="method.color" />
          <h3 class="font-semibold mb-1">{{ method.name }}</h3>
          <p class="text-xs text-muted-foreground">{{ method.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
