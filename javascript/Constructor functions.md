In JavaScript, constructor functions are used to create objects with predefined properties and methods; intended to act on a newly-constructed object when invoked with the `new` keyword.


**They follow these key principles:**
1. **Naming Convention**: Constructor functions typically start with a capital letter (e.g., `Person`, `Car`).
2. **The `new` Keyword**: Objects are created by invoking the constructor function with the `new` keyword.
3. **The `this` Keyword**: Inside the constructor, `this` refers to the newly created object.

```js
function Person(name, age) {
  this.name = name;
  this.age = age;
}

```

Calling a function with `new` creates a new object using the called function as the "constructor" for that object:

```js
let john = new Person("John", 30);

console.log(john.name); // Output: John
```

The value of `this` within a constructor function refers to the object being created, letting the object be populated with properties and methods at the time of creation.

## the Class syntax

While constructor functions still work, modern JavaScript (ES6 and later) introduced the `class` syntax. 

This new syntax does the same thing as constructor functions, but in a way that's easier to use and understand, and is now often preferred over the older constructor function style.