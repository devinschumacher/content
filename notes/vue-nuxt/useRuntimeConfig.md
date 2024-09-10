`useRuntimeConfig` in Nuxt is a built-in composable for accessing runtime configurations.
## How to use it

Runtime configurations for Nuxt are stored in `nuxt.config.ts` using the `runtimeConfig` attribute.

1. define them in your `nuxt.config.ts`
2. use them in your app
### 1. define them in your `nuxt.config.ts`

```ts
// nuxt.config.ts

export default defineNuxtConfig({
// ...other configs

	runtimeConfig: {
		public: {
			weatherApiKey: '1f6ec271f3da959c1db1575514f66264'
		}
	}
});
```

- "public" keyws will be accessible on the client side (and public).
- "secret keys" will be accessible only on the server.

### 2. use them in your app `<script>`

```ts
<script setup lang='ts'>
async function citiesLookup(query: string) {
	// get access to the runtimeConfig object in nuxt.config.ts
	const config = useRuntimeConfig();
	
	// get the API KEY from the runtimeConfig object
	const apiKey = config.public.weatherApiKey;
	
	const response = await $fetch(
	`http://api.openweathermap.org/geo/1.0/direct?q=${query}&limit=5&appid=${apiKey}`
	);

return response;
}

// test out the API call & display the response in the console
const data = await citiesLookup('seattle')
console.log(data)
</script>
```

## 3. use them in your app `<template>`



