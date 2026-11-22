import { createI18n } from 'vue-i18n'

import ar from './locales/ar.json'
import en from './locales/en.json'

export const SUPPORTED_LOCALES = ['en', 'ar'] as const
export type Locale = (typeof SUPPORTED_LOCALES)[number]
export const DEFAULT_LOCALE: Locale = 'en'

type MessageSchema = typeof en

export const i18n = createI18n<[MessageSchema], Locale, false>({
  legacy: false,
  locale: DEFAULT_LOCALE,
  fallbackLocale: DEFAULT_LOCALE,
  messages: { en, ar },
})

export function isLocale(value: string): value is Locale {
  return (SUPPORTED_LOCALES as readonly string[]).includes(value)
}

export function directionOf(locale: Locale): 'rtl' | 'ltr' {
  return locale === 'ar' ? 'rtl' : 'ltr'
}
