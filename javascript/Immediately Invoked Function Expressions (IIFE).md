An Immediately Invoked Function Expression (IIFE), also sometimes called a "self-executing anonymous function," is a [Function expression](Function%20expression.md) that is called immediately when it's defined.

An IIFE uses a [Function expression](Function%20expression.md) created by enclosing the function in a grouping operator.

A second matched pair of parentheses then calls the function, either immediately following  the grouping operator:

```js

// Immediately following the function definition itself
// OUTSIDE of the initial matched parenthesis 'grouping operator'

(function() {console.log( "IIFE.")} )();

> "IIFE."
```

Which also looks like this when you break it apart:

```js
(function() {    
  console.log( "IIFE.")    
  }
)();
> "IIFE."
```


...or immediately following the function definition itself:
```js

// Immediately following the function definition itself
// INSIDE the initial matched parenthesis 'grouping operator'

(function() {console.log( "IIFE.")} ());
> "IIFE."
```

Which also looks like this when you break it apart:

```js
(function() {    
  console.log( "IIFE.")    
  }
());
> "IIFE."
```

The result is the same in either case.

## IIFEE Arrow functions

When your IIFE is an arrow function, the parentheses used to call the function must be *outside* the grouping operators, because an [Arrow function](Arrow%20functions.md) on its own isn't an expression.

