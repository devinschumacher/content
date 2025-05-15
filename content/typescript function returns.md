---
tags: ['typescript','void','function returns']
---

## void

if a function returns nothing you should use the type `void` (not the type `undefined`), because `void` makes it clear deliberately that a function does not have a return statement.

```ts
function printResult(num: number): void {
	console.log('The number is: ' num)
}
```


## undefined

If your function has a return statement, but it does not return a value, then you use `undefined`.