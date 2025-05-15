JavaScript has a built-in `...` operator that makes it easier to work with an unknown numbers of items.

Depending on the context, it's called either a _rest operator_ or _spread operator_.

## rest elements

When `...` appears on the left-hand side of an assignment, the three dots are known as the `rest` operator.

```js
const [a, b, ...everythingElse] = [0, 1, 1, 2, 3, 5, 8];

console.log(everythingElse);
[1, 2, 3, 5, 8]
```

In this example the `...everythingElse` variable is the "rest element".

A "rest element" cannot have a trailing comma. It _must_ be the last element in the de-structuring assignment: as you can see in the example it is the last element in the `const []` part.

## spread elements

When `...` appears on the right-hand side of an assignment, it's known as the `spread` operator. 

It takes an array and 'expands it' (puts it) into a list of elements.

```js
const oneToFive = [1, 2, 3, 4, 5];
const oneToTen = [...oneToFive, 6, 7, 8, 9, 10];

console.log(oneToTen);
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

Unlike the rest element, the spread element *can* appear anywhere in an array literal expression, and there can be more than one.


## extract elements (de-structuring)

In a de-structuring assignment, you **extract values from an array or object** into variables. For example:

```js
const [firstCard, ...remainingDeck] = deck;
```

Here, the **rest element** (`...remainingDeck`) **must be the last element** in the pattern. 

This is because JavaScript needs to know where to stop extracting values. 

## expand elements (spread operator in array literals)

In an array literal (like when creating a new array), the spread operator (`...`) is used to **expand an array into individual elements**.

```js
return [firstCard, ...FACE_CARDS, ...remainingDeck];
```

**Here, the spread operator is used to:**
- Insert all elements of `FACE_CARDS` into the new array.    
- Insert all elements of `remainingDeck` into the new array.

This is valid because the spread operator in this context is not about **extracting values** but about **combining arrays**. JavaScript knows exactly how to handle this: it simply expands the arrays into the new array.
