A _statement_ is a unit of instruction made up of one or more lines of code that represent an action.

For example, you can use the following statement to assign a value to a variable named `myVariable`:

```js
let myVariable = 4;myVariable;> 4
```

To be interpreted correctly, statements must end in a semicolon. However, these semicolons aren't always required when _writing_ JavaScript.

A feature called **automatic semicolon insertion** lets a line break following a complete statement be treated as a semicolon if a missing semicolon would cause an error.

Automatic semicolon insertion is error correction - relying too much on this error correction can lead to ambiguity that breaks your code, **you should still manually end every statement with a semicolon**.

## Block statements

A block statement groups any number of statements and declarations inside a pair of braces (`{}`). 

They let you combine statements in places where JavaScript expects only one.

```js
if ( x === 2 ) {  //some behavior;}
```

