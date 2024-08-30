---
tags:
  - SOP
---
# How to connect Supabase to a Nuxt project

## 1. Create a new Supabase project

Create a new supabase project

## 2. Add supabase credentials to .env

```.env
SUPABASE_URL=<your-supabase-project-url>
SUPABASE_KEY=<your-supabase-public-key>
```

## 3. Install the @nuxtjs/supabase module

1. Install the nuxt supabase module:

```bash
pnpm install -D @nuxtjs/supabase
```

2. Add "@nuxtjs/supabase" to `nuxt.config.js` in the `modules` array

```nuxt.config.js
export default defineNuxtConfig({
	modules: ['@nuxt/ui', '@nuxtjs/supabase'],
})
```

3. Set the supabase "redirect" setting default to False in `nuxt.config.js`

```nuxt.config.js
export default defineNuxtConfig({
	modules: ['@nuxt/ui', '@nuxtjs/supabase'],
	supabase: {
		redirect: False
	}
})
```