The `app.config.ts` file is a central UI configuration file.

It lets you customize/tailer your app's themes and component styles by doing things like: 
- setting theme colors
- integrating with Tailwind CSS

It's defined with:

```ts
// app.config.ts
export default defineAppConfig({})
```

The `ui` property of the object let's you provide specific component customizations.


```ts
// app.config.ts
export default defineAppConfig({
	ui: {
		primary: 'sky'
	}
})
```

