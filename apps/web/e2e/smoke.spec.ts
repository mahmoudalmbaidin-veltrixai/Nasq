import { expect, test } from '@playwright/test'

test('home page switches between English and Arabic', async ({ page }) => {
  await page.goto('/')

  await expect(page.locator('html')).toHaveAttribute('dir', 'ltr')
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('Nasq')

  await page.getByRole('button', { name: 'العربية' }).click()

  await expect(page.locator('html')).toHaveAttribute('dir', 'rtl')
  await expect(page.locator('html')).toHaveAttribute('lang', 'ar')
  await expect(page.getByRole('heading', { level: 1 })).toHaveText('نسق')
})
