a union type allows you to have a value that can be more than one type.

`type1 | type2 | type3`

let's say you have a function called combine() that should work with both numbers and strings.

```js
function combine(input1: number | string, input2: number | string) {
	return input1 + input2;
}
```

however this will cause typescript to squigly line your `return input1 + input2` because when you have a union type typescript just sees that it is a union type, and does not look into the actual union types it can be.

for `input1: number | string` typescript just sees "this is a union type" and squiglys your `return input1 + input2`  because you could have put a boolean as one of the union type options and booleans cannot be combined with the `+` operator.

to fix this you would add a "runtime type check" check to the function

```js
function combine(input1: number | string, input2: number | string) {
	if (typeof input1  === 'number' && typeof input2 === 'number') {
		result = input1 + input2;
	} else {
		result = input1.toString() + input2.toString();
	}
	return result
}
```