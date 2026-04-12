<script setup lang="ts">
const { t } = useI18n()

const methodKeys = ['ikigai', 'level10life', 'grow', 'okrs', 'gtd', 's3', 'crm', 'scrum'] as const

const methodMeta = [
  { icon: 'lucide:compass', color: 'text-purple-500' },
  { icon: 'lucide:heart-pulse', color: 'text-green-500' },
  { icon: 'lucide:route', color: 'text-pink-500' },
  { icon: 'lucide:target', color: 'text-yellow-500' },
  { icon: 'lucide:inbox', color: 'text-cyan-500' },
  { icon: 'lucide:git-branch', color: 'text-blue-500' },
  { icon: 'lucide:users', color: 'text-orange-500' },
  { icon: 'lucide:list-checks', color: 'text-red-500' },
]
</script>

<template>
  <section class="py-20">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">{{ t('methodologies.title') }}</h2>
        <p class="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto">
          {{ t('methodologies.subtitle') }}
        </p>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div
          v-for="(key, index) in methodKeys"
          :key="key"
          class="bg-card border border-border rounded-xl p-5 hover:border-primary/30 transition-colors"
        >
          <Icon :name="methodMeta[index].icon" class="w-6 h-6 mb-3" :class="methodMeta[index].color" />
          <h3 class="font-semibold mb-1">{{ t(`methodologies.items.${key}.name`) }}</h3>
          <p class="text-xs text-muted-foreground">{{ t(`methodologies.items.${key}.description`) }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
