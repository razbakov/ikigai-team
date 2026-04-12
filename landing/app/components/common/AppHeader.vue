<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()
const mobileMenuOpen = ref(false)
</script>

<template>
  <header class="border-b border-border bg-background/80 backdrop-blur-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <NuxtLink :to="localePath('/')" class="flex items-center gap-2">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32" class="w-7 h-7">
            <circle cx="13.5" cy="13.5" r="5" fill="none" stroke="currentColor" stroke-width="1.2" class="text-primary/50" />
            <circle cx="18.5" cy="13.5" r="5" fill="none" stroke="currentColor" stroke-width="1.2" class="text-primary/50" />
            <circle cx="13.5" cy="18.5" r="5" fill="none" stroke="currentColor" stroke-width="1.2" class="text-primary/50" />
            <circle cx="18.5" cy="18.5" r="5" fill="none" stroke="currentColor" stroke-width="1.2" class="text-primary/50" />
            <circle cx="16" cy="16" r="2" fill="currentColor" class="text-primary" />
          </svg>
          <span class="text-lg font-bold">Ikigai Team</span>
        </NuxtLink>

        <nav class="hidden md:flex items-center gap-6">
          <NuxtLink
            :to="localePath('/')"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
            active-class="text-foreground font-medium"
          >
            {{ t('nav.home') }}
          </NuxtLink>
          <NuxtLink
            :to="localePath('/guide')"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
            active-class="text-foreground font-medium"
          >
            {{ t('nav.guide') }}
          </NuxtLink>
          <NuxtLink
            :to="localePath('/skills')"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
            active-class="text-foreground font-medium"
          >
            {{ t('nav.skills') }}
          </NuxtLink>
          <CommonLanguagePicker />
          <CommonThemeToggle />
          <NuxtLink
            :to="localePath('/guide/getting-started')"
            class="inline-flex items-center gap-2 px-4 py-2 rounded-md bg-primary text-primary-foreground text-sm font-medium hover:opacity-90 transition-opacity"
          >
            <Icon name="lucide:rocket" class="w-4 h-4" />
            {{ t('nav.getStarted') }}
          </NuxtLink>
        </nav>

        <button
          class="md:hidden p-2"
          @click="mobileMenuOpen = !mobileMenuOpen"
        >
          <Icon :name="mobileMenuOpen ? 'lucide:x' : 'lucide:menu'" class="w-6 h-6" />
        </button>
      </div>

      <div v-if="mobileMenuOpen" class="md:hidden pb-4 space-y-2">
        <NuxtLink
          :to="localePath('/')"
          class="block px-3 py-2 text-sm hover:bg-muted rounded-md"
          @click="mobileMenuOpen = false"
        >
          {{ t('nav.home') }}
        </NuxtLink>
        <NuxtLink
          :to="localePath('/guide')"
          class="block px-3 py-2 text-sm hover:bg-muted rounded-md"
          @click="mobileMenuOpen = false"
        >
          {{ t('nav.guide') }}
        </NuxtLink>
        <NuxtLink
          :to="localePath('/skills')"
          class="block px-3 py-2 text-sm hover:bg-muted rounded-md"
          @click="mobileMenuOpen = false"
        >
          {{ t('nav.skills') }}
        </NuxtLink>
        <div class="flex items-center gap-3 px-3 py-2">
          <CommonLanguagePicker />
          <CommonThemeToggle />
          <NuxtLink
            :to="localePath('/guide/getting-started')"
            class="inline-flex items-center gap-2 px-4 py-2 rounded-md bg-primary text-primary-foreground text-sm font-medium"
            @click="mobileMenuOpen = false"
          >
            {{ t('nav.getStarted') }}
          </NuxtLink>
        </div>
      </div>
    </div>
  </header>
</template>
