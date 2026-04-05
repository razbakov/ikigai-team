import { defineContentConfig, defineCollection, z } from '@nuxt/content'

export default defineContentConfig({
  collections: {
    guide: defineCollection({
      type: 'page',
      source: 'guide/**',
      schema: z.object({
        title: z.string(),
        description: z.string().optional(),
      }),
    }),
    skills: defineCollection({
      type: 'page',
      source: 'skills/**',
      schema: z.object({
        title: z.string(),
        description: z.string().optional(),
        category: z.string().optional(),
        agent: z.string().optional(),
        complexity: z.string().optional(),
      }),
    }),
    data: defineCollection({
      type: 'data',
      source: 'data/**',
    }),
  },
})
