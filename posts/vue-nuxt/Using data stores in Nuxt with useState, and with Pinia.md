---
tags: ['nuxt', 'useState', 'pinia']
---

## useState

useState is the official method for creating global states in Nuxt, unless you use a store management library like Pinia.

- useState is a `ref` replacement
- useState is SSR friendly
- any global shared state that is created using `useState` is reactive by default

### example using useState

1. create a `count` variable which represents the global state, by putting it in `app.vue`

```js
// app.vue

<script setup>
const count = useState('count', () => 0);
</script>
```

2. on a specific page that you want to access data from the global state, for example the homepage `index.vue`

```js
// pages/index.vue

<script setup>
const count
```


// #WIP


---

## Pinia

Example: Creating a Pinia store and "counter" component.

1. *Install* pinia and the nuxt pinia module:

```
pnpm i pinia @pinia/nuxt
```

2. *Register* `@pinia/nuxt` in `nuxt.config.ts`

```ts
// nuxt.config.ts
export default defineNuxtConfig({
	modules: ['@pinia/nuxt']
})
```

3. Create `stores/counter.ts`

```ts
/// stores/counter.ts
import { defineStore } from 'pinia';
export const useCounterStore = defineStore('count', () => {
    // set the count = 0 by default
    const count = 0;
    return {
        count
    };

    // increment the count
    function increment() {
        count.value++;
    }
    return {
        increment
    };

});
```

4. Create `pages/counter.vue` & import your "counter store" (`useCounterStore`)

```ts

```



