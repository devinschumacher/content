
the tailwind theme function allows you to grab config values.

## tailwind theme() function

```js /* tailwind.config.js */

module.exports = {
	theme: {
		extend: {
			spacing: {
				128: '32rem',
			}
		}
	}
}
```

you can then use that spacing value in your `input.css` file like:

```css

.content-area {
	@apply bg-blue-200;
	height: theme('spacing.128);
}
```

## tailwind screen() function

```css

@media screen(xl) {
	body {
		@apply bg-black text-white;
	}
}
```