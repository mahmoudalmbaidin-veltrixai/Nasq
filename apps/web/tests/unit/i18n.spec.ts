import { describe, expect, it } from 'vitest'

import { directionOf, isLocale, SUPPORTED_LOCALES } from '@/i18n'
import ar from '@/i18n/locales/ar.json'
import en from '@/i18n/locales/en.json'

type Tree = { [key: string]: string | Tree }

function flatten(tree: Tree, prefix = ''): Record<string, string> {
  return Object.entries(tree).reduce<Record<string, string>>((flat, [key, value]) => {
    const path = prefix ? `${prefix}.${key}` : key
    return typeof value === 'string' ? { ...flat, [path]: value } : { ...flat, ...flatten(value, path) }
  }, {})
}

describe('translations', () => {
  it('has exactly the same keys in Arabic and English', () => {
    expect(Object.keys(flatten(ar)).sort()).toEqual(Object.keys(flatten(en)).sort())
  })

  it('has no empty strings in either language', () => {
    for (const messages of [en, ar]) {
      for (const [key, value] of Object.entries(flatten(messages))) {
        expect(value.trim(), key).not.toBe('')
      }
    }
  })

  it('names the product Nasq in English and نسق in Arabic', () => {
    expect(en.app.name).toBe('Nasq')
    expect(ar.app.name).toBe('نسق')
  })
})

describe('locales', () => {
  it('supports Arabic and English only', () => {
    expect([...SUPPORTED_LOCALES].sort()).toEqual(['ar', 'en'])
    expect(isLocale('ar')).toBe(true)
    expect(isLocale('fr')).toBe(false)
  })

  it('writes Arabic right to left and English left to right', () => {
    expect(directionOf('ar')).toBe('rtl')
    expect(directionOf('en')).toBe('ltr')
  })
})
