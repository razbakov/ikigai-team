<script setup lang="ts">
const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()

const allLocales = computed(() =>
  locales.value as Array<{ code: string; name: string }>
)
</script>

<template>
  <div class="relative">
    <div class="pointer-events-none absolute inset-y-0 left-0 w-4 bg-gradient-to-r from-background via-background/85 to-transparent z-10" />
    <div class="pointer-events-none absolute inset-y-0 right-0 w-4 bg-gradient-to-l from-background via-background/85 to-transparent z-10" />
    <div
      class="overflow-x-auto px-2 [scrollbar-width:none] [-ms-overflow-style:none] [&::-webkit-scrollbar]:hidden"
      aria-label="Language selector"
    >
      <div class="flex min-w-max flex-nowrap gap-1.5">
        <NuxtLink
          v-for="loc in allLocales"
          :key="loc.code"
          :to="switchLocalePath(loc.code)"
          class="inline-flex shrink-0 items-center whitespace-nowrap rounded-full border px-2.5 py-1 text-xs font-medium transition-colors"
          :class="locale === loc.code
            ? 'border-primary bg-primary text-primary-foreground'
            : 'border-border bg-card/80 text-foreground hover:border-primary/50'"
        >
          <span class="uppercase">{{ loc.code }}</span>
        </NuxtLink>
      </div>
    </div>
  </div>
</template>
