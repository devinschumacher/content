JavaScript's array de-structuring syntax is a concise way to extract values from an array and assign them to distinct variables.

In this example, each value in the `numberOfMoons` array is assigned to its corresponding planet:

```js
const numberOfMoons = [0, 2, 14]; 
const [venus, mars, neptune] = numberOfMoons; 

neptune; // => 14
```
