---
title: Vue/Nuxt Slots <slot>
tags:
  - Vue
  - Nuxt
---
1. Create a component: `ExampleComponent.vue`
2. Put a `<slot></slot>` in the component

```html
<!-- ExampleComponent.vue -->
<template>
	<span class="px-4 py-2 bg-white text-primary">
		<slot></slot>
	</span>
</template>
```


3. In the page (or other component) you want to use your `ExampleComponent.vue` in you can put tags and whatever goes in between the component tags ( `<example-component></example-component>` ) is the content that will be displayed in place of those slots

So, if you have a page to display this example component twice, like this:

```html
<!-- somePage.vue -->
<div>
	<example-component>JS</example-component>
	<example-component>Vue</example-component>
<div>
```

The text "JS" and "Vue" would effectively 'built' and styled, etc. like this:

```html
<span class="px-4 py-2 bg-white text-primary">JS</span>
<span class="px-4 py-2 bg-white text-primary">Vue</span>
```

Notice how the `<template></template>` tags in the component do not exist in the rendered HTML - they are just so Vue knows how to properly build/compile your code into something for the browser.