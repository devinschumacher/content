Function expressions are functions created where an [expression](javascript%20expression.md) is expected. 

You'll frequently encounter function expressions as values assigned to a variable.

```
const myVariable = function() { };
```

You can then call those function expressions using the variable's identifier:

```js
const myVariable = function() {    
  console.log( "This is my function." );
};

myVariable();
> "This is my function."
```

## Grouping operators

The 'grouping operator' is a matched pair of parenthesis, used to group parts of an expression to ensure that portion is evaluated as a single unit.

For example, you might use a grouping operator to override the mathematical order of operations, or to improve the readability of code:

```js
2 + 2 * 4;
> 10

( 2 + 2 ) * 4;
> 16

let myVariable = ( 2 + 2 );

myVariable;
> 4
```

Or, you will see them used in IIFEs ([Immediately Invoked Function Expressions (IIFE)](Immediately%20Invoked%20Function%20Expressions%20(IIFE).md)).
