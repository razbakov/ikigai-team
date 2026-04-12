<script setup lang="ts">
const { t } = useI18n()
</script>

<template>
  <section class="py-20">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="bg-card border border-border rounded-2xl p-8 sm:p-12">
        <div class="flex items-center gap-3 mb-6">
          <div class="w-10 h-10 rounded-full bg-primary/10 flex items-center justify-center">
            <Icon name="lucide:lightbulb" class="w-5 h-5 text-primary" />
          </div>
          <h2 class="text-2xl font-bold">{{ t('founderStory.title') }}</h2>
        </div>
        <div class="space-y-4 text-muted-foreground">
          <p>{{ t('founderStory.p1') }}</p>
          <p>{{ t('founderStory.p2') }}</p>
          <p>{{ t('founderStory.p3') }}</p>
          <p class="text-foreground font-medium">{{ t('founderStory.p4') }}</p>
        </div>
      </div>
    </div>
  </section>
</template>
