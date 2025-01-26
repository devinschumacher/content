a function type describes a function regarding the function's parameters & return value.

you create a function type using: 
- a `() =>` syntax
- on the right side you specify the return value

```ts

// a function that takes no parameters & returns a number
let myFunctionType: () => number;


// a function that takes 2 parameters that are
// both numbers and returns a number
let myFunctionType: (a: number, b: number) => number;

```