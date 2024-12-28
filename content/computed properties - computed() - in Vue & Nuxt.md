A "computed property" (aka "computed function" aka using  `computed()`) is a helper function provided by Vue that helps us interact with the Vue reactivity system.

Computed properties allow you to perform **calculations** or **transformations** of data in your `<script>` sections and then easily reuse the result in your `<template>` sections.

- The `computed()` function expected to be passed a getter function
- The returned value is a computed ref
- You access the returned value of a `computed()` function using `.value`
```
myComputedThing.value
```



## Example usage



## Best practices

Don't put logic in your HTML template syntax areas, instead make a computed() function to handle the logic, and then use that value in your template syntax areas.
```
const useThisInYourTemplateAreas = computed(() => {
	// do something
})
```


## Related
- https://vuejs.org/guide/essentials/computed