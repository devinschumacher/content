---
title: JavaScript Imports & Exports - Guide & Reference Sheet
tags:
 - javascript
---
JavaScript modules (in the context of imports/exports) refers to the methods and syntax used to share code between different files or scripts, enabling developers to organize, encapsulate, and reuse functionality across their projects.

**Related topics to know:**
- [Destructuring](Destructuring.md)

## JavaScript module import/export categories

There are two types (syntaxes) of javascript modules:

1. CommonJS: the traditional way of doing imports in node.js
2. ES Modules: the way of doing imports in the browser

## JavaScript module import/export types

### Common JS

1. Node modules
2. Node built-in modules
4. Node npm packages
5. Node modules (ES Module syntax)

#### Node modules

**Defined:**

Node modules are reusable pieces of code in a Node.js application that can be exported from one program and imported for use in another program.

**Use case:**

They are used to organize code into separate files, making it easier to maintain and reuse functionality across different parts of an application.

**Syntax:**

```js
// exportFile.js
module.exports = <value>

// importFile.js
const importedValue = require('<path-to-module>')
```

**Example:**

```js
// logger.js
function log(message) {
    console.log(`[LOG]: ${message}`);
}

module.exports = log;

// app.js
const logger = require('./logger');

logger('Hello, Node.js!');  // Output: [LOG]: Hello, Node.js!
```

**For exporting:**

- Use `module.exports` to export a single value (function, object, primitive).
- You can also use `exports.<property>` to export multiple values.

**For importing:**

- Use the `require()` function to import modules.
- The path to the module is specified as a string argument to `require()`.

#### Node built-in modules

**Defined:**

Node built-in modules are core modules that come pre-installed with Node.js and provide essential functionalities.

**Use case:**

They offer a wide range of utilities for tasks such as file system operations, networking, cryptography, and more, without the need for external dependencies.

**Syntax:**

```js
const moduleName = require('module-name')
```

**Example:**

```js
const fs = require('fs');

fs.readFile('example.txt', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(data);
});
```

**For importing:**

- Use the `require()` function with the module name as a string argument.
- No file path is needed; Node.js knows where to find its built-in modules.

**Note:** Some commonly used built-in modules include `fs` (file system), `http` (HTTP server), `path` (file path utilities), and `crypto` (cryptographic functionality).

#### Node npm packages

**Defined:**

Node npm packages are third-party modules available through the npm (Node Package Manager) registry, which can be installed and used in Node.js projects.

**Use case:**

They extend the functionality of Node.js applications by providing pre-built solutions for common tasks, frameworks, and libraries.

**Syntax:**

```js
const packageName = require('package-name')
```

**Example:**

```js
// First, install the package: npm install lodash

const _ = require('lodash');

const numbers = [1, 2, 3, 4, 5];
console.log(_.sum(numbers));  // Output: 15
```

**For importing:**

- First, install the package using npm: `npm install package-name`
- Use the `require()` function with the package name as a string argument.
- No file path is needed; Node.js looks in the `node_modules` directory.

**Note:** Always check the package documentation for specific usage instructions, as some packages may have different import methods or configurations.

#### Node modules (ES Module syntax)

**Defined:**

Node.js supports ES Module syntax, allowing you to use `import` and `export` statements instead of `require()` and `module.exports`.

**Use case:**

ES Module syntax provides a more standardized way of working with modules, aligning Node.js more closely with browser-based JavaScript and improving code consistency across environments.

**Syntax:**

```js
// exportFile.mjs
export const <name> = <value>

// importFile.mjs
import { name } from '<path-to-module>'
```

**Example:**

```js
// math.mjs
export function add(a, b) {
    return a + b;
}

// app.mjs
import { add } from './math.mjs';

console.log(add(2, 3));  // Output: 5
```

**For exporting:**

- Use `export` keyword before declarations to export named values.
- Use `export default` for a default export.

**For importing:**

- Use `import` statement with curly braces for named imports.
- Use `import` without curly braces for default imports.

**Note:** To use ES Module syntax in Node.js:
- Use the `.mjs` file extension, or
- Set `"type": "module"` in your `package.json`, or
- Use the `--experimental-modules` flag when running Node.js (for older versions)

Remember that when using ES Module syntax, you can't mix `require()` and `import` in the same file. Choose one approach and stick to it within a module.

### ES modules

1. Named imports
2. Default imports
3. Namespace imports
4. Mixed/list Imports (combining default and named)

#### Named imports

**Defined:** 

Named imports/exports in ES modules allow you to explicitly specify which functions, objects, or primitives you want to export from a module and import into another module.

**Use case:**

Named imports provides a way to share specific pieces of functionality between files while keeping the global scope clean.

**Syntax:**

```js
// exportFile.js
export const <name> = "<value>"

// importFile.js
import { name } from "<path-to-module>"
```

**Example:**

```js
// math.js
export const PI = 3.14159;
export function square(x) {
    return x * x;
}

// main.js
import { PI, square } from './math.js';

console.log(PI);  // 3.14159
console.log(square(4));  // 16
```

**For exporting:**

- You can export multiple named values from a module.
- The `export` keyword is placed before the declaration.
- You can export variables, functions, or classes.

**For importing:**

- You use curly braces `{}` to specify which named exports you want to import.
- You can import multiple named exports by separating them with commas.
- The `from` keyword is followed by the path to the module in quotes.

#### Default imports

**Defined:**

Default imports/exports in ES modules allow you to export a single main value from a module and import it without using curly braces.

**Use case:** 

They are designed to be imported as a whole. This is useful when a module primarily exports one thing. 

**Syntax:**

```js
// exportFile.js
export default <value>

// importFile.js
import anyName from "<path-to-module>"
```

**Example:**

```js
// person.js
export default class Person {
    constructor(name) {
        this.name = name;
    }
    sayHello() {
        console.log(`Hello, I'm ${this.name}`);
    }
}

// main.js
import Person from './person.js';

const john = new Person('John');
john.sayHello();  // Output: Hello, I'm John
```

**For exporting:**

- You can only have one default export per module.
- The `export default` keywords are placed before the value you want to export.
- You can export functions, classes, objects, or primitive values.

**For importing:**

- You don't use curly braces `{}` when importing a default export.
- You can choose any name for the imported value; it doesn't have to match the original name.
- The `from` keyword is followed by the path to the module in quotes.

**Note:** You can combine default and named exports/imports in the same module:

```js
// math.js
export const PI = 3.14159;
export default function square(x) {
    return x * x;
}

// main.js
import squareFunction, { PI } from './math.js';

console.log(PI);  // 3.14159
console.log(squareFunction(4));  // 16
```

#### Namespace imports

**Defined:**

Namespace imports in ES modules allow you to import all exports from a module as properties of a single object.

**Use case:** 

They are useful when you want to import multiple exports from a module and keep them organized under a single namespace, or when you're not sure which specific exports you'll need.

**Syntax:**

```js
// importFile.js
import * as ModuleName from "<path-to-module>"
```

**Example:**

```js
// math.js
export const PI = 3.14159;
export function square(x) {
    return x * x;
}
export function cube(x) {
    return x * x * x;
}

// main.js
import * as MathUtils from './math.js';

console.log(MathUtils.PI);  // 3.14159
console.log(MathUtils.square(4));  // 16
console.log(MathUtils.cube(3));  // 27
```

**For importing:**

- You use the `*` wildcard to import all exports from the module.
- The `as` keyword is used to assign a name to the namespace object.
- All exported items become properties of the namespace object.
- The `from` keyword is followed by the path to the module in quotes.

**Note:** Namespace imports can be combined with default imports:

```js
// myModule.js
export default function mainFunction() { /* ... */ }
export const helperFunction = () => { /* ... */ }

// main.js
import mainFunction, * as MyModule from './myModule.js';

mainFunction();
MyModule.helperFunction();
```

**Considerations:**

- Namespace imports can make your code more verbose when accessing individual exports.
- They may prevent dead code elimination (tree shaking) by bundlers, as the entire module is imported.
- They're particularly useful when working with modules that export many related functions or values.

#### Mixed/list Imports

**Defined:**

Mixed or list imports in ES modules allow you to import both default and named exports from a module in a single import statement.

**Use case:** 

They are useful when you need to import a module's default export along with one or more of its named exports, combining the functionality of default and named imports.

**Syntax:**

```js
// importFile.js
import DefaultExport, { namedExport1, namedExport2 } from "<path-to-module>"
```

**Example:**

```js
// math.js
export const PI = 3.14159;
export function square(x) {
    return x * x;
}
export default function sum(a, b) {
    return a + b;
}

// main.js
import sum, { PI, square } from './math.js';

console.log(sum(2, 3));  // 5
console.log(PI);  // 3.14159
console.log(square(4));  // 16
```

**For importing:**

- The default import comes first, without curly braces.
- Named imports follow, enclosed in curly braces `{}`.
- You can import as many named exports as needed, separated by commas.
- The `from` keyword is followed by the path to the module in quotes.

**Note:** You can also use aliases with mixed imports:

```js
import MyDefaultExport, { export1 as alias1, export2 as alias2 } from './myModule.js';
```

**Considerations:**

- Mixed imports provide a concise way to import multiple types of exports from a single module.
- They're particularly useful when working with libraries or modules that provide both a main functionality (as a default export) and additional utilities (as named exports).
- When using mixed imports, make sure to keep track of which import is the default and which are named to avoid confusion in your code.

## Import paths

The path syntax in the import statement can vary depending on the location of the module you're importing from:

1. For local modules in your project:
- Use `./` for modules in the same directory
- Use `../` to go up one directory level

2. For installed packages (e.g., from npm):
- Use the package name directly, without `./`

3. For built-in Node.js modules:
- Use the module name directly, without `./`

**Some examples to illustrate:**

```js
// Local module in the same directory
import { someFunction } from './localModule.js';

// Local module in a subdirectory
import { anotherFunction } from './utils/helperModule.js';

// Local module in parent directory
import { parentFunction } from '../parentModule.js';

// Installed package (e.g., from npm)
import { useState } from 'react';

// Built-in Node.js module
import { readFile } from 'fs/promises';
```

### Path aliases

Path aliases are not a native feature of JavaScript or ES modules. They're typically set up through build tools, bundlers, or frameworks. Nuxt.js is a good example of a framework that provides this feature out of the box, but it's not limited to Nuxt.

**Examples:**

**Nuxt.js**: Nuxt provides the `@` alias by default, pointing to the `src/` directory (or the root if there's no `src/`). You can configure additional aliases in `nuxt.config.js`:

```js 
// nuxt.config.js
export default {
  alias: {
    '@': '/<rootDir>',
    '~': '/<rootDir>',
    '@components': '/<rootDir>/components'
  }
}
```


**Webpack**: If you're using Webpack (which Nuxt uses under the hood), you can set up aliases in your Webpack configuration:

```js
// webpack.config.js
module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src/'),
      '@components': path.resolve(__dirname, 'src/components/')
    }
  }
}
```

**TypeScript**: In TypeScript projects, you can set up path aliases in your `tsconfig.json`:

```ts
// tsconfig.json
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@components/*": ["src/components/*"]
    }
  }
}
```

**Vite**: If you're using Vite, you can set up aliases in your `vite.config.js`:

```js
// vite.config.js
import path from 'path'
import { defineConfig } from 'vite'

export default defineConfig({
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src'),
      '@components': path.resolve(__dirname, './src/components')
    }
  }
})
```


Once set up, you can use these aliases in your import statements:

```js
import MyComponent from '@components/MyComponent.vue'
```

This approach has several benefits:

- It makes imports more readable and maintainable.
- It allows you to move files without breaking import paths.
- It reduces the need for long relative paths.