import { mount } from '@vue/test-utils'
import { createPinia, setActivePinia, type Pinia } from 'pinia'
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest'

import { i18n } from '@/i18n'
import { useLocaleStore } from '@/stores/locale'
import HomeView from '@/views/HomeView.vue'

let pinia: Pinia

beforeEach(() => {
  pinia = createPinia()
  setActivePinia(pinia)
  localStorage.clear()
  useLocaleStore().setLocale('en')
  localStorage.clear()
})

afterEach(() => {
  vi.restoreAllMocks()
})

describe('locale store', () => {
  it('switches the document to Arabic, right to left', () => {
    useLocaleStore().setLocale('ar')

    expect(document.documentElement.lang).toBe('ar')
    expect(document.documentElement.dir).toBe('rtl')
    expect(i18n.global.locale.value).toBe('ar')
  })

  it('switches the document back to English, left to right', () => {
    const store = useLocaleStore()
    store.setLocale('ar')
    store.setLocale('en')

    expect(document.documentElement.lang).toBe('en')
    expect(document.documentElement.dir).toBe('ltr')
  })

  it('remembers the chosen language across visits', () => {
    useLocaleStore().setLocale('ar')

    setActivePinia(createPinia())
    useLocaleStore().initialise()

    expect(useLocaleStore().locale).toBe('ar')
  })

  it('follows an Arabic browser when nothing was chosen yet', () => {
    vi.spyOn(navigator, 'language', 'get').mockReturnValue('ar-JO')

    useLocaleStore().initialise()

    expect(useLocaleStore().locale).toBe('ar')
    expect(document.documentElement.dir).toBe('rtl')
  })

  it('falls back to English for unsupported browser languages', () => {
    vi.spyOn(navigator, 'language', 'get').mockReturnValue('fr-FR')

    useLocaleStore().initialise()

    expect(useLocaleStore().locale).toBe('en')
  })

  it('ignores an unsupported saved value', () => {
    localStorage.setItem('nasq.locale', 'xx')
    vi.spyOn(navigator, 'language', 'get').mockReturnValue('en-US')

    useLocaleStore().initialise()

    expect(useLocaleStore().locale).toBe('en')
  })
})

describe('home view', () => {
  it('shows the product name and an honest scaffold notice, with no engine controls', () => {
    const wrapper = mount(HomeView, { global: { plugins: [pinia, i18n] } })

    expect(wrapper.get('h1').text()).toBe('Nasq')
    expect(wrapper.get('[role="status"]').text()).toContain('No planning features')
    expect(wrapper.findAll('button')).toHaveLength(1)
  })

  it('toggles to Arabic from the language button', async () => {
    const wrapper = mount(HomeView, { global: { plugins: [pinia, i18n] } })

    await wrapper.get('button').trigger('click')

    expect(wrapper.get('h1').text()).toBe('نسق')
    expect(document.documentElement.dir).toBe('rtl')
    expect(wrapper.get('button').text()).toBe('English')
  })
})
