---
title: How to Use Environment Variables & runtimeConfig Correctly in Nuxt
tags: ['nuxt', 'vue', 'guide']
---

- Ref: https://www.youtube.com/watch?v=_FYV5WfiWvs

## .env variable naming conventions

The naming convention for environment variables in Nuxt requires that your `.env` values match the key structure in `runtimeConfig`.

Specifically, if your public key is something like `somethingLikeThis`, then the corresponding `.env` variable should be in uppercase snake case, like `NUXT_PUBLIC_SOMETHING_LIKE_THIS`.

The `NUXT_` prefix is used by Nuxt to identify environment variables that are intended to be injected into the app at runtime.

Public runtime values in Nuxt, the corresponding environment variables in your `.env` file should have `NUXT_PUBLIC_` prepended to the key name. Private keys do not need to be pre-pended.

Environment variables prefixed with `NUXT_PUBLIC_` are exposed to both client and server, whereas variables without `NUXT_PUBLIC_` are only available on the server side

```.env
# .env

# public keys
NUXT_PUBLIC_API_URL=https://example.com
NUXT_PUBLIC_SOMETHING_LIKE_THIS=exampleValue

# private keys
API_SECRET_KEY=superSecret123
DATABASE_URL=mysql://user:password@localhost/db
```

```ts
// nuxt.config.ts
export default defineNuxtConfig({
  runtimeConfig: {
  // values in the public: key are exposed to client
    public: {
      apiUrl: process.env.NUXT_PUBLIC_API_URL,
      somethingLikeThis: process.env.NUXT_PUBLIC_SOMETHING_LIKE_THIS
    },
	// values outside of the public: key are private by default 
    apiSecretKey: process.env.API_SECRET_KEY,
    databaseUrl: process.env.DATABASE_URL
  }
});

```

> This allows Nuxt to map the environment variable to the runtime config key.


## Transforms

**Dont** use tranforms in runtimeConfig.

Transforms like `.trim()` in `runtimeConfig` will only be executed during build-time, not at runtime. Therefore, the result of the transformation will not change after the application is built.

For example, DONT do this:

```ts
export default defineNuxtConfig({
  runtimeConfig: {
    public: {
      myValue: process.env.NUXT_PUBLIC_MY_VALUE?.trim()
    }
  }
});

```


## Using/referencing .env variables in your app

To reference and use your `runtimeConfig` values in your app, you can access them in different ways depending on whether you are working on the server-side or client-side.

- **Public runtime values** are accessed via `config.public` and are available on both the client and server.
- **Private runtime values** are accessed directly from `config` and are only available on the server side​

### Client-Side (public)

- On client-side, only keys in `runtimeConfig.public` are available, and the object is both writable and reactive.

For public values, you can use the `useRuntimeConfig` composable:

```vue
<script setup lang="ts">
const config = useRuntimeConfig();
</script>

<template>
	<p>{{ config.public.myValue }}</p> 
	<!-- This renders the value of "myValue" from runtimeConfig, 
	which corresponds to the NUXT_PUBLIC_MY_VALUE variable in .env -->
</template>
```

> ⚠️ **Security:** Don't expose runtime config keys to the client-side by either rendering them or passing them to `useState`

### Server-side (private)

- On server-side, the entire runtime config is available, but it is read-only to avoid context sharing.

Private values are available only on the server-side, meaning you can use them in your server routes, middleware, or other server-specific files. 

> ⚠️ Don't use them outside of the `server/` directory.

To reference private runtime configuration values in a `server/` file in Nuxt, you use the `useRuntimeConfig()`

**Example 1:** 

```ts
// server/middleware/example.ts
export default defineEventHandler((event) => {
  const config = useRuntimeConfig();
  console.log(config.apiSecretKey); // Access secret on the server-side
});

```

**Example 2:**

```ts
// server/api/example.ts
export default defineEventHandler((event) => {
  const config = useRuntimeConfig();
  
  // Access private runtime config values
  const secretValue = config.apiSecret;
  
  console.log(secretValue); // Do something with the private value
  return {
    message: `Your secret value is: ${secretValue}`
  };
});

```