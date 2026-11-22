import skipFormatting from '@vue/eslint-config-prettier/skip-formatting'
import { defineConfigWithVueTs, vueTsConfigs } from '@vue/eslint-config-typescript'
import pluginVue from 'eslint-plugin-vue'

export default defineConfigWithVueTs(
  {
    name: 'nasq/files-to-lint',
    files: ['**/*.{ts,mts,vue}'],
  },
  {
    name: 'nasq/ignores',
    ignores: ['dist/**', 'coverage/**', 'playwright-report/**', 'test-results/**'],
  },
  pluginVue.configs['flat/recommended'],
  vueTsConfigs.strictTypeChecked,
  skipFormatting,
)
