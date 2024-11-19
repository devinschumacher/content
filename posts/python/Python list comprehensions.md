# Python List Comprehensions

## List comprehension syntax

```python
list = [ expression for item in iterable if condition == True ]
```

1. **Expression**: The expression is the current item in the iteration (loop), and also the result.
2. **Iterable**: The `iterable` is any 'iterable object' in the list. Since lists can be made up of items, or other lists/tuples/etc, and list/tuples/etc. are iterable objects, the `iterable` can be a specific list item, or an entire list/tuple/etc.
3. **Condition**: The condition is optional. With the condition, it will apply when true. Without the condition, every item will be looped over.


### Example 1

```python
shapes = ['circle', 'square', 'triangle', 'rectangle']

list_comprehension = [ shape for shape in shapes if "a" in shape ]
```

1. **Expression**: `shape`
2. **Iterable**: the list `shapes` is the iterable. The 4 list items ('circle', 'square', 'triangle', 'rectangle') will be looped over - aka `iterated` over.
3. **Condition**: The condition in this case is if the letter "a" is found in the name of name (string) of the shape.

**Result**: `['square', 'triangle', 'rectangle']`

The expression is the current item (the shape), and the result. In this case, we asked the list comprehension for the "shape".


### Example 2

In example 1, we just said "shape for shape in shapes ...", which meant the outcome would result in the shape, as we saw above in "Result".

This time let's change the `expression` so it affects the outcome more distinctly.

```python
shapes = ['circle', 'square', 'triangle', 'rectangle']

list_comprehension = [ '💩' for shape in shapes if "a" in shape ]
```

In this case we asked the list comprehension to take a 💩 everytime there was a shape in the list 'shapes' that had "a" in its string.

**Result**: `['💩', '💩', '💩']`

Because the condition was met 3 times, the outcome included 3 💩. 
