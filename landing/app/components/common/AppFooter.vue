<script setup lang="ts">
const { t } = useI18n()
const localePath = useLocalePath()
</script>

<template>
  <footer class="border-t border-border bg-background py-8 mt-auto">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex flex-col sm:flex-row items-center justify-between gap-4">
        <div class="flex items-center gap-2 text-sm text-muted-foreground">
          <span>{{ t('footer.madeBy') }} <a href="https://razbakov.com" target="_blank" rel="noopener noreferrer" class="hover:text-foreground transition-colors">Alosha</a></span>
        </div>
        <div class="flex items-center gap-4">
          <a
            href="https://github.com/razbakov/ikigai-team"
            target="_blank"
            rel="noopener noreferrer"
            class="text-muted-foreground hover:text-foreground transition-colors"
          >
            <Icon name="lucide:github" class="w-5 h-5" />
          </a>
          <NuxtLink
            :to="localePath('/guide')"
            class="text-sm text-muted-foreground hover:text-foreground transition-colors"
          >
            {{ t('nav.documentation') }}
          </NuxtLink>
        </div>
      </div>
    </div>
  </footer>
</template>
