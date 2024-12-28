---
title: JavaScript Callback Functions
tag:
 - javascript
 - glossary
---
In JavaScript, a callback function is a function passed as an argument to another function, to be executed after some operation has been completed or at a specified time.

**For example:**

```js
setTimeout(() => {}, 2000)
```

This function (`setTimeout()`) takes 2 arguments:
1. The first argument is the "callback function"
2. The second argument is the amount of time to 'wait' or 'timeout' for.

The first function here is the callback function. In this case it is `() => {}` - which happens to be an [Arrow Function](Arrow%20Functions.md) that does nothing - however, it is a valid callback function because it is passed to the `setTimeout()` function to be executed after `2000` passes (2000 miliseconds aka 2 seconds).

So this code will wait for 2 seconds and then execute the empty function.

