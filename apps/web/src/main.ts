import { createPinia } from 'pinia'
import { createApp } from 'vue'

import App from './App.vue'
import { i18n } from './i18n'
import { router } from './router'
import { useLocaleStore } from './stores/locale'

const pinia = createPinia()
const app = createApp(App).use(pinia).use(i18n).use(router)

useLocaleStore(pinia).initialise()
app.mount('#app')
