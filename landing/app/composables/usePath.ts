export type PathType = 'personal' | 'work'

const selectedPath = ref<PathType>('personal')

export function usePath() {
  return {
    path: selectedPath,
    isPersonal: computed(() => selectedPath.value === 'personal'),
    isWork: computed(() => selectedPath.value === 'work'),
  }
}
