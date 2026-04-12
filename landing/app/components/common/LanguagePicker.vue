<script setup lang="ts">
const { locale, locales } = useI18n()
const switchLocalePath = useSwitchLocalePath()
const open = ref(false)

const availableLocales = computed(() =>
  (locales.value as Array<{ code: string; name: string }>).filter(l => l.code !== locale.value)
)

const currentLocale = computed(() =>
  (locales.value as Array<{ code: string; name: string }>).find(l => l.code === locale.value)
)

function close() {
  open.value = false
}
</script>

<template>
  <div class="relative">
    <button
      type="button"
      class="inline-flex items-center gap-1.5 px-2 py-1.5 rounded-md text-sm text-muted-foreground hover:text-foreground hover:bg-muted transition-colors"
      @click="open = !open"
    >
      <Icon name="lucide:globe" class="w-4 h-4" />
      <span class="uppercase text-xs font-medium">{{ locale }}</span>
      <Icon name="lucide:chevron-down" class="w-3 h-3" />
    </button>

    <Transition
      enter-active-class="transition ease-out duration-100"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        v-if="open"
        class="absolute right-0 mt-2 w-44 rounded-lg border border-border bg-background shadow-lg z-50"
      >
        <div class="py-1">
          <div class="px-3 py-2 text-xs text-muted-foreground font-medium border-b border-border">
            {{ currentLocale?.name }}
          </div>
          <NuxtLink
            v-for="loc in availableLocales"
            :key="loc.code"
            :to="switchLocalePath(loc.code)"
            class="flex items-center gap-2 px-3 py-2 text-sm hover:bg-muted transition-colors"
            @click="close"
          >
            <span class="uppercase text-xs font-mono w-5 text-muted-foreground">{{ loc.code }}</span>
            <span>{{ loc.name }}</span>
          </NuxtLink>
        </div>
      </div>
    </Transition>

    <div
      v-if="open"
      class="fixed inset-0 z-40"
      @click="close"
    />
  </div>
</template>
