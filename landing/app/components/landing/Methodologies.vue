<script setup lang="ts">
const { t } = useI18n()
const { path } = usePath()

const personalMethods = [
  { key: 'ikigai', icon: 'lucide:compass', color: 'text-purple-500' },
  { key: 'level10life', icon: 'lucide:heart-pulse', color: 'text-green-500' },
  { key: 'grow', icon: 'lucide:route', color: 'text-pink-500' },
  { key: 'okrs', icon: 'lucide:target', color: 'text-yellow-500' },
  { key: 'gtd', icon: 'lucide:inbox', color: 'text-cyan-500' },
  { key: 's3', icon: 'lucide:git-branch', color: 'text-blue-500' },
  { key: 'crm', icon: 'lucide:users', color: 'text-orange-500' },
  { key: 'scrum', icon: 'lucide:list-checks', color: 'text-red-500' },
]

const workMethods = [
  { key: 'onboarding', icon: 'lucide:user-plus', color: 'text-purple-500' },
  { key: 'roles', icon: 'lucide:shield', color: 'text-green-500' },
  { key: 'knowledge', icon: 'lucide:book-open', color: 'text-pink-500' },
  { key: 'okrs', icon: 'lucide:target', color: 'text-yellow-500' },
  { key: 'gtd', icon: 'lucide:inbox', color: 'text-cyan-500' },
  { key: 's3', icon: 'lucide:git-branch', color: 'text-blue-500' },
  { key: 'crm', icon: 'lucide:users', color: 'text-orange-500' },
  { key: 'scrum', icon: 'lucide:list-checks', color: 'text-red-500' },
]

const methods = computed(() => path.value === 'work' ? workMethods : personalMethods)
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
          v-for="method in methods"
          :key="method.key"
          class="bg-card border border-border rounded-xl p-5 hover:border-primary/30 transition-colors"
        >
          <Icon :name="method.icon" class="w-6 h-6 mb-3" :class="method.color" />
          <h3 class="font-semibold mb-1">{{ t(`methodologies.items.${method.key}.name`) }}</h3>
          <p class="text-xs text-muted-foreground">{{ t(`methodologies.items.${method.key}.description`) }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
