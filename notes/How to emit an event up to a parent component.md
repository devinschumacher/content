
## The child component

### in the `<script>` section

1. `defineEmits()` function

```vue
<script setup lang="ts">
	const emit = defineEmits(['change'])
</script>
```

This declares the "event emitter" in the const emit
### In the `<template>` section

1. An event listener
2. `$emit()` function

```vue
<!-- MyComponent.vue -->
<template>
	<USelectMenu
		v-model="activeCity"
		:searchable="citiesLookup"
		placeholder="Search for a city.."
		@update:model-value="$emit('change', $event)" <!-- here -->
		/>
</template>
```

- We `v-model` to the field that represents that thing were changing: `activeCity` .
- We add an event listener ( `@update` ) to the component and bind to: `modelValue`.

The `$emit()` function is used, taking arguments:
- 'change'
- $event

`@update:modelValue` will emit a *change event* whenever the `activeCity` value is changed. This emit will dispatch the newly selected city (contained within the `$event` parameter) to the parent component.

## The parent component

In the parent component, we catch the emitted updates and make the "change" by:
1. defining a function to make the change
2. listening for the emitted event in the `<template>`

```vue
<script setup>
	
</script>
```