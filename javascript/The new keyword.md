Calling a function with `new` creates a new object using the called function as the "constructor" for that object:

```js
function MyFunction() {}
const myObject = new MyFunction();

typeof myObject;
> "object"`
```

This lets a "constructor function" provide a template for the creation of objects that follow the same structural pattern:

```js
function MyFunction() {  
  this.myProperty = true;
}
const myObject = new MyFunction();

myObject.myProperty;
> true
```

The value of `this` within a constructor function refers to the object being created, letting the object be populated with properties and methods at the time of creation.

This allows for the creation of objects that contain data values and any methods needed to act on that data as a single portable unit, a concept called "encapsulation":

```js
function MyFunction( myArgument ) {
  this.myValue = myArgument;
  this.doubleMyValue = () => myArgument * 2;
}
const myObject = new MyFunction( 10 );


myObject.myValue;
> 10

myObject.doubleMyValue();
> 20
```

`this` refers to the current execution context of a function, meaning that a constructor function follows the same rules for the value of `this` as any other function.

