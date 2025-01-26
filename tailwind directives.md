---
tags: ['tailwind', 'css', 'frontend']
---

tailwind directives are @rules ("at" rules) that you can use that do special things.

in the default generated `input.css` file from tailwind, you can see some the @tailwind directive being used:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## @tailwind directive

the @tailwind directive is used to insert tailwind's `base`, `components`,  `utilities`  and `variants` styles into your CSS. aka, the main CSS default rules that ship out of the box will get compiled into your final `.css` file.

## @layer directive

the @layer directive lets you create custom styles for your HTML elements without having to add a bunch of tailwind classes to it directly. 

### @layer base

```css /* index.css */
@layer base {
	h1 {
		font-size: 2rem;
	}
}
```

this would show up in your compiled .css file like:

```css /* styles.css */
h1 {
	font-size: 2rem;
}
```

you can also use existing tailwind utility classes in your @layer css (instead of writing vanilla css):

```css /* index.css */
@layer base {
	h1 {
		@apply text-3xl;
	}
	h2 {
		@apply text-xl;
	}
}
```

this would show up in your compiled .css file like:

```css /* styles.css */
h1 {
	font-size: 1.875rem;
	line-height: 2.25rem;
}

h2 {
	font-size: 1.25rem;
	line-height: 1.75rem;
}
```

### @layer components

great for repetitive combinations of tailwind utility classes being used on the same element -- you can refactor that into a @layer and then use that (similar to how a library liike Bootsrap might consolidate styles for components to use less HTML markup)

```css /* index.css */
@layer components {
	.btn-blue {
		@apply bg-blue-500 py-2 px-4 rounded-xl hover:bg-blue-700	
	}
}
```

```html
<button class="btn-blue">Click me</button>
```

you can also create your own 'custom classes' by just declaring them in the index.css file:

```css /* index.css */
.serp-blue-button {
	@apply bg-blue-500 py-2 px-4 rounded-xl hover:bg-blue-700	
}
```

```html
<button class="serp-blue-button">Click me</button>
```

