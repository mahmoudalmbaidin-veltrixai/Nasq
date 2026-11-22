<script setup lang="ts">
import { useI18n } from 'vue-i18n'

import { useLocaleStore } from '@/stores/locale'

const { t } = useI18n()
const localeStore = useLocaleStore()
</script>

<template>
  <main class="home">
    <header class="home__header">
      <h1>{{ t('app.name') }}</h1>
      <button
        type="button"
        class="home__language"
        :lang="t('language.switchToCode')"
        @click="localeStore.toggle()"
      >
        {{ t('language.switchTo') }}
      </button>
    </header>
    <p>{{ t('app.tagline') }}</p>
    <p role="status" class="home__notice">{{ t('home.scaffoldNotice') }}</p>
  </main>
</template>

<style scoped>
.home {
  max-inline-size: 48rem;
  margin-inline: auto;
  padding: 2rem 1.5rem;
  font-family: system-ui, sans-serif;
}

.home__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
}

.home__notice {
  padding-block: 0.75rem;
  padding-inline: 1rem;
  border-inline-start: 4px solid currentcolor;
}
</style>
