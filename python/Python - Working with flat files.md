# Python - Working with flat files

---

```python
# assign file to a variable
filename = 'book.txt'

# open the file in 'read mode'
file = open(filename, mode='r')

# save the contents of the text file to a variable
text = file.read()

# close the file
file.close()
```

To avoid needing to close the file, you can use a ‘context manager’ - in this case, ‘with’.

Once outside of the ‘with’ context, the file is no longer open.

```python
with open('book.txt', 'r') as file:
	print(file.read())
```

```python
# opening the file in 'write mode'
file = open(filename, mode='w')
```

## Reading contents files
