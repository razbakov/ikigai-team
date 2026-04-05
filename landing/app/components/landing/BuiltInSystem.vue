<script setup lang="ts">
const journey = [
  {
    step: '01',
    name: 'Reflect',
    agent: 'Sage',
    description: 'Start with yourself. Level 10 Life assessment — score 10 areas of your life honestly. Where are you right now?',
    methodology: 'Level 10 Life',
    icon: 'lucide:heart-pulse',
    color: 'text-[var(--color-sage)]',
  },
  {
    step: '02',
    name: 'Find Direction',
    agent: 'Sage',
    description: 'Define your mission and vision. Use the GROW framework: Goal (mission), Reality (L10L scores), Options, Way Forward.',
    methodology: 'GROW + Ikigai',
    icon: 'lucide:compass',
    color: 'text-[var(--color-sage)]',
  },
  {
    step: '03',
    name: 'Set Strategy',
    agent: 'Marco',
    description: 'Turn your Way Forward into OKRs. Measurable objectives for this quarter. Challenge assumptions. Focus.',
    methodology: 'OKRs',
    icon: 'lucide:target',
    color: 'text-[var(--color-marco)]',
  },
  {
    step: '04',
    name: 'Build the Rhythm',
    agent: 'Maya',
    description: 'Daily reviews, inbox processing, weekly planning. The GTD system that turns strategy into daily action.',
    methodology: 'GTD',
    icon: 'lucide:inbox',
    color: 'text-[var(--color-maya)]',
  },
  {
    step: '05',
    name: 'Execute',
    agent: 'The Team',
    description: 'Viktor builds. Luna creates content. Kai handles community. Sage checks in. Maya keeps it all running. You focus on your ikigai.',
    methodology: 'S3 Governance',
    icon: 'lucide:users',
    color: 'text-primary',
  },
]
</script>

<template>
  <section class="py-20 bg-muted/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">Not Just Agents. A Journey.</h2>
        <p class="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto">
          It starts with you — not with configuration files. Every methodology is built in.
          You do not have to learn it first. The team teaches you as you go.
        </p>
      </div>
      <div class="space-y-6 max-w-3xl mx-auto">
        <div
          v-for="(item, index) in journey"
          :key="item.step"
          class="flex gap-6 items-start"
        >
          <div class="flex flex-col items-center shrink-0">
            <div class="w-12 h-12 rounded-full bg-card border border-border flex items-center justify-center">
              <Icon :name="item.icon" class="w-6 h-6" :class="item.color" />
            </div>
            <div v-if="index < journey.length - 1" class="w-px h-full min-h-[40px] bg-border mt-2" />
          </div>
          <div class="pb-8">
            <div class="flex items-center gap-2 mb-1">
              <span class="text-xs font-mono text-muted-foreground">STEP {{ item.step }}</span>
              <span class="text-xs px-2 py-0.5 rounded-full bg-muted text-muted-foreground">{{ item.methodology }}</span>
            </div>
            <h3 class="text-lg font-semibold mb-1">{{ item.name }} <span class="text-sm font-normal text-muted-foreground">with {{ item.agent }}</span></h3>
            <p class="text-sm text-muted-foreground">{{ item.description }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
