<script setup lang="ts">
const { t } = useI18n()
const { path } = usePath()

const personalJourneyKeys = ['reflect', 'findDirection', 'setStrategy', 'buildRhythm', 'execute'] as const
const personalMeta = [
  { step: '01', agent: 'Sage', icon: 'lucide:heart-pulse', color: 'text-[var(--color-sage)]' },
  { step: '02', agent: 'Sage', icon: 'lucide:compass', color: 'text-[var(--color-sage)]' },
  { step: '03', agent: 'Marco', icon: 'lucide:target', color: 'text-[var(--color-marco)]' },
  { step: '04', agent: 'Maya', icon: 'lucide:inbox', color: 'text-[var(--color-maya)]' },
  { step: '05', agent: 'The Team', icon: 'lucide:users', color: 'text-primary' },
]

const workJourneyKeys = ['install', 'configure', 'onboard', 'workflows', 'scale'] as const
const workMeta = [
  { step: '01', agent: 'Admin', icon: 'lucide:download', color: 'text-[var(--color-viktor)]' },
  { step: '02', agent: 'Admin', icon: 'lucide:settings', color: 'text-[var(--color-marco)]' },
  { step: '03', agent: 'Maya', icon: 'lucide:user-plus', color: 'text-[var(--color-maya)]' },
  { step: '04', agent: 'The Team', icon: 'lucide:workflow', color: 'text-[var(--color-kai)]' },
  { step: '05', agent: 'The Team', icon: 'lucide:trending-up', color: 'text-primary' },
]

const journeyKeys = computed(() => path.value === 'work' ? workJourneyKeys : personalJourneyKeys)
const journeyMeta = computed(() => path.value === 'work' ? workMeta : personalMeta)
const stepsPrefix = computed(() => path.value === 'work' ? 'journey.workSteps' : 'journey.personalSteps')
</script>

<template>
  <section class="py-20 bg-muted/30">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="text-center mb-16">
        <h2 class="text-3xl font-bold">{{ t(`journey.${path}.title`) }}</h2>
        <p class="mt-3 text-lg text-muted-foreground max-w-2xl mx-auto">
          {{ t(`journey.${path}.subtitle`) }}
        </p>
      </div>
      <div class="space-y-6 max-w-3xl mx-auto">
        <div
          v-for="(key, index) in journeyKeys"
          :key="key"
          class="flex gap-6 items-start"
        >
          <div class="flex flex-col items-center shrink-0">
            <div class="w-12 h-12 rounded-full bg-card border border-border flex items-center justify-center">
              <Icon :name="journeyMeta[index].icon" class="w-6 h-6" :class="journeyMeta[index].color" />
            </div>
            <div v-if="index < journeyKeys.length - 1" class="w-px h-full min-h-[40px] bg-border mt-2" />
          </div>
          <div class="pb-8">
            <div class="flex items-center gap-2 mb-1">
              <span class="text-xs font-mono text-muted-foreground">{{ t('journey.step') }} {{ journeyMeta[index].step }}</span>
              <span class="text-xs px-2 py-0.5 rounded-full bg-muted text-muted-foreground">{{ t(`${stepsPrefix}.${key}.methodology`) }}</span>
            </div>
            <h3 class="text-lg font-semibold mb-1">{{ t(`${stepsPrefix}.${key}.name`) }} <span class="text-sm font-normal text-muted-foreground">{{ t('journey.with') }} {{ journeyMeta[index].agent }}</span></h3>
            <p class="text-sm text-muted-foreground">{{ t(`${stepsPrefix}.${key}.description`) }}</p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
