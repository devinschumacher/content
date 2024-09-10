
Create `types/index.ts` at the root of your project where you will define your "types".

For example, you need to create two entities for a real estate site "Property" and "Category", you would start by defining the types like:

```ts
export { };
	declare global {
		type Property = {};
		type Category = {};
};
```


- `export {}`:  exporting an empty object
- `declare global {...}`: declaring a global object that contains your entities and their types

By doing these two things together, it makes your types globally available in the application and eliminates the need to import those types into each component.

> Note: The empty objects for each of those 2 types just represents where you put in the type information for their respective fields.


