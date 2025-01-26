
## core primitive types

core primitive types in TypeScript are all lowercase,  like `string` or `number`... **NOT** `String`, `Number`

## object type

a javascript object consists of curly brackets `{ }` and `key:value` pairs of information inside the curly brackets:
```js

// example 1
{ age: 30 }

// example 2
{ name: devin, age: 30 }

```

any javascript object is of type `object` in typescript.

however,  there are 'more specific types of objects' in typescript - ie: an object that has to have specific properties.

```js

const person = {
	name: 'Devin',
	age: '30'
}
```

if you hover your cursor in your IDE over person (above) you would see typescript infers this object as:

```ts
const person: {
	name: string;
	age: number;
}
```

You can tell this is a typescript "object type" (and not a javascript object) because:

1. it has a colon (`:`) after `person` -- javascript has an equal sign (`=`)
2. it has semi-colons (`;`) after its `key: type` pairs -- javascript has a comma (`,`) after its `key: value` pairs

This is called a "concrete object".


## generic object type

typescripts generic object type is: `object`


## specialized object type

typescripts specialized object type is: `{ }`


