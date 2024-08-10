A function is a modular, reusable block of [Statements](Statements.md) used to perform a set of related tasks.

## Function declarations

A function declaration (aka "function statements", "function definitions") creates a named function that can be invoked elsewhere in its containing scope.

**Function declarations consist of:**
1. the `function` keyword followed by an identifier
2.  a list of comma-separated parameters enclosed in parentheses
3. a block [Statements](Statements.md) called the "function body."

## Function calling

The identifier used when declaring a function acts as a symbolic name for the function/value:

```js
function myFunction() {
  console.log( "This is my function." );
};


myFunction;
> myFunction() {   
>   console.log( "This is my function." );
> }
```

To execute the code inside the function body, _call_ (or _invoke_) the function by following the function name with a matched pair of parentheses:

```js
function myFunction() {
  console.log( "This function has been executed / called / invoked." );
};


myFunction();
> "This function has been executed / called / invoked."
```

## Function parameters

Parameters in the function declaration act as placeholder variables for values that can be passed into the function body when the function is called:

```js
function myFunction( myParameter ) {   
console.log( `The value is: ${ myParameter }.` );
};


myFunction( "this string" );
> "The value is: this string."
```

### Default parameter values

You can set default parameter values by initializing them the same way you would initialize a variable: an assignment operator (`=`) followed by a value. 

```js
function myFunction( myParameter = "omitted" ) {   
  console.log( `The value is: ${ myParameter }.` );
};


// call the function without specificy a parameter value
// will result in the default value assigned when the func was delcared
myFunction();
> "The value is: omitted."
```

If you later specify an argument for that function, that new value overrides the default value:


```js
myFunction( "this string" );
> "The value is: this string."
```


## Function expressions

Function expressions are functions created where an expression is expected. You'll frequently encounter function expressions as values assigned to a variable.

Although a function declaration always requires a name, you can use function expressions to create anonymous functions by omitting the identifier and following the `function` keyword with a pair of parentheses containing optional parameters:\

```js
const myVariable = function() { };
```

- Read more about [Function expression](Function%20expression.md)

