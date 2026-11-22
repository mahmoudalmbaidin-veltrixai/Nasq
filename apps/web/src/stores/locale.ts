import { defineStore } from 'pinia'
import { ref } from 'vue'

import { DEFAULT_LOCALE, directionOf, i18n, isLocale, type Locale } from '@/i18n'

const STORAGE_KEY = 'nasq.locale'

export const useLocaleStore = defineStore('locale', () => {
  const locale = ref<Locale>(DEFAULT_LOCALE)

  function apply(next: Locale): void {
    locale.value = next
    i18n.global.locale.value = next
    document.documentElement.lang = next
    document.documentElement.dir = directionOf(next)
  }

  function setLocale(next: Locale): void {
    apply(next)
    localStorage.setItem(STORAGE_KEY, next)
  }

  function initialise(): void {
    const saved = localStorage.getItem(STORAGE_KEY)
    if (saved !== null && isLocale(saved)) {
      apply(saved)
      return
    }
    const browser = navigator.language.toLowerCase().split('-')[0] ?? ''
    apply(isLocale(browser) ? browser : DEFAULT_LOCALE)
  }

  function toggle(): void {
    setLocale(locale.value === 'ar' ? 'en' : 'ar')
  }

  return { locale, setLocale, initialise, toggle }
})
