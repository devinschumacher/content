Callback functions are functions that are passed to a "caller function" in the form of a parameter (argument).

Writing a callback function is no different from writing a function ; however, the callback function must expect the the possible argument from the caller function.

```js
const sideLength = 5; 

// Caller function
function applySideLength(callbackFunction) {
	return callback(sideLength); 
} 

// Callback function
function areaOfSquare(side) { 
	return side * side; 
} 

applySideLength(areaOfSquare); // => 25
```


You may also write callbacks as a function expression:

```js

// Caller function
applySideLength(function squarePerimeterLength(side) { 
	return side * 4; 
});
```