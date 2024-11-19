---
title: JavaScript Arrow Functions
tags:
  - javascript
  - glossary
---
Arrow function expressions (often called "arrow functions" or, rarely, "lambda functions") provide a concise syntax for creating anonymous [function expressions](Function%20expression.md) with some unique behaviors.

You can create an arrow function wherever an [expression](Expression.md) is expected.

## Arrow functions syntax

**In its most common form, an arrow function is made up of:** 
1. A pair of matched parentheses containing zero or more parameters: ` () `
2. An arrow made up of a single equals sign and greater-than character: `=>`
3. A pair of matched curly braces containing the function body: ` { } `

```js
const myArrowFunction = () => {};
```

Under certain conditions, you can make the syntax even more compact. 
If you're only using one parameter, you can leave out the starting parentheses:
```js
const myCompactArrowFunction = myParameter => {};
```

