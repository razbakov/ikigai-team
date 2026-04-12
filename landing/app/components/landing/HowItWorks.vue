<script setup lang="ts">
const { t } = useI18n()
const { path } = usePath()

const stepKeys = ['startWithSage', 'buildStrategy', 'focusOnIkigai'] as const

const stepMeta = [
  { number: '01', icon: 'lucide:heart-pulse' },
  { number: '02', icon: 'lucide:target' },
  { number: '03', icon: 'lucide:compass' },
]
</script>

<template>
  <section class="py-20 bg-muted/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">{{ t(`howItWorks.${path}.title`) }}</h2>
        <p class="mt-3 text-lg text-muted-foreground">
          {{ t(`howItWorks.${path}.subtitle`) }}
        </p>
      </div>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div
          v-for="(key, index) in stepKeys"
          :key="key"
          class="relative text-center"
        >
          <div v-if="index < stepKeys.length - 1" class="hidden md:block absolute top-12 left-[60%] w-[80%] h-px bg-border" />
          <div class="w-24 h-24 mx-auto rounded-2xl bg-primary/10 flex items-center justify-center mb-6">
            <Icon :name="stepMeta[index].icon" class="w-10 h-10 text-primary" />
          </div>
          <span class="text-xs font-mono text-muted-foreground">{{ t('howItWorks.step') }} {{ stepMeta[index].number }}</span>
          <h3 class="text-xl font-semibold mt-2 mb-3">{{ t(`howItWorks.${path}.steps.${key}.title`) }}</h3>
          <p class="text-sm text-muted-foreground max-w-xs mx-auto">{{ t(`howItWorks.${path}.steps.${key}.description`) }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
