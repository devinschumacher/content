# vite.config .xx - the Vite config file

The configuration file for Vite that allows developers to customize various aspects, behaviors, settings, etc. of their Vite powered project.

The VIte config file is typically written in javascript: `vite.config.js` or typescript:`vite.config.ts`although it also supports `vite.config.mjs` for JavaScript modules & `vite.config.cjs` for CommonJS.

You can even explicitly specify a config file to use with the `--config` CLI option (resolved relative to `cwd`):
```bash
vite --config my-config.js
```

... And it exports a configuration object that Vite will use for both development & production.

```js
// vite.config.js
export default {
  // config options
}
```

Under the hood Vite uses Rollup.js for development & esbuild for production builds, and supports having different configurations for dev vs. production

The Vite config file is automatically created when you scaffold a project using Vite, for example:
```bash
pnpm create vite@latest <project-name>
```

## An example vite.config.js file + explainer

```js
// vite.config.js
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

export default defineConfig({
  plugins: [vue()],
  resolve: {
    extensions: [".mjs", ".js", ".ts", ".jsx", ".tsx", ".json", ".vue"],
    alias: {
      "@": path.resolve(__dirname, "src"),
      "@components": path.resolve(__dirname, "src", "components"),
    },
  },
});
```

1. Imports
- `defineConfig`: A utility function from Vite that provides type hinting for the configuration object.
- `vue`: The Vue plugin for Vite, enabling Vue single-file component support.
- `path`: A Node.js built-in module for handling file and directory paths.

2. `export default defineConfig({...})`
- The `defineConfig` function wraps our configuration object.
- `export default` specifies the main export of a module. Default exports are imported without curly braces, while named exports use them.

3. Plugins ( `plugins: [vue()],` )
- An array that specifies the plugins Vite should use.

4. resolve+
```js
resolve: {
    extensions: [".mjs", ".js", ".ts", ".jsx", ".tsx", ".json", ".vue"],
    alias: {
      "@": path.resolve(__dirname, "src"),
      "@components": path.resolve(__dirname, "src", "components"),
    },
  },

```

- The `resolve` option customizes how Vite resolves module imports.
- `alias` creates shortcuts for import paths:
	- `"@components"` creates an alias (named @components) mapped to the project's path /src/components, so when we import components we can avoid writing relative or absolute paths and instead simply reference the imports inside components with the syntax import MyComponent from "@components/MyComponent.vue"
	- `path.resolve()` generates an absolute path, ensuring consistency across different environments.
	- `__dirname` represents the directory of the current module (where `vite.config.js` is located).
- `extensions` 
	- Specifies file extensions to try when resolving imports without extensions.
	- this "extension resolution" allows you to write `import './utils'` instead of `import './utils.js'`.