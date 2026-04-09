import posthog from 'posthog-js'

export default defineNuxtPlugin(() => {
  const config = useRuntimeConfig()
  const key = config.public.posthogPublicKey as string

  if (!key) return

  const client = posthog.init(key, {
    api_host: config.public.posthogHost as string,
    person_profiles: 'identified_only',
    capture_pageview: false,
  })!

  const router = useRouter()
  router.afterEach((to) => {
    nextTick(() => {
      posthog.capture('$pageview', { current_url: to.fullPath })
    })
  })

  return { provide: { posthog: () => client } }
})
