# Python Booleans

## What are python booleans?

Python Booleans are data types that are used to represent True or False values. They are key in decision-making processes, such as if statements. By executing a boolean statement, a program can make a decision to execute a certain set of instructions.

## Types of Booleans

1. True Booleans - These are the simplest possible Booleans, and represent true values.
2. False Booleans - These are the opposite of True Booleans, representing a false value.
3. Numerical Booleans - These Booleans can also represent a True or False value and are based on numerical values.
4. Logical Booleans - These Booleans are used to represent more complex relationships between variables and are used in combination with mathematical and comparison operators.

### Properties of Booleans

- Booleans are immutable and cannot be changed once set.
- Booleans can be combined using logical operators such as 'and', 'or', and 'not'.
- Booleans have a value of either True or False.
- Booleans use a lexicographical order when compared to each other.
- Booleans can be used to control decision logic in a program.

## Boolean Operators

Boolean operators are special symbols that are used in comparison statements and decisions making structures in programming. These operators combine two or more values and evaluate them according to a set of conditions. Boolean operators are also referred to as logical operators or comparison operators.

The three main Boolean operators are:

AND – Represents a logical AND operation. This operator will return true if both values being evaluated are true.

OR – Represents a logical OR operation. This operator will return true if either of the two values being evaluated are true.

NOT – Represents a logical NOT operation. This operator will reverse the value of the expression being evaluated.

How to Evaluate Expressions

# Working with Booleans

To evaluate an expression, we must first understand the syntax for the expression and the logic behind it. A basic Boolean expression can contain the following components:

1. A comparison operator (>, <, =, !=, >=, <=)
2. Two terms to be compared
3. A Boolean expression (True or False)

To evaluate the expression, we must first check the comparison operator to determine which type of comparison is being made. For example, if the operator is '>' then the expression is asking if the left side of the expression is greater than the right side of the expression.

The next step is to look at the two terms being compared. These can be either expressions or values. If they are expressions, we must evaluate them first to see what they are equal to.

Finally, we must evaluate the entire expression to determine if it is either True or False. Depending on the type of comparison being made and the values of the two terms being compared, the result of the expression can be either True or False.

```bash
# Example using Booleans in Python 
is_adult = True 
age = 20 

if (is_adult == True and age >= 18): 
  print("This person is an adult") 
else: 
  print("This person is not an adult")
```

## bool() Syntax

The syntax of `bool()` is:

```other
bool(argument)
```

---

## bool() Parameter

The `bool()` method takes in a single parameter:

- argument - whose boolean value is returned

---

## bool() Return Value

The `bool()` method returns:

- `False` - if argument is **empty**, **False**, **0** **or** **None**
- `True` - if argument is **any number** **(besides 0),** **True** **or a** **string**

---

# bool() with a string

```bash
test = 'Hello'

print(test, 'is' ,bool(test))
```

# bool() with an integer

```bash
test1 = 8

print(test1, 'is' ,bool(test1))
```

# bool() with a float

```bash
test2 = 3.14

print(test2, 'is' ,bool(test2))
```

# bool() with a dictionary

```bash
test3 = {'name': 'John', 'age': 28}

print(test3, 'is' ,bool(test3))

Example 2: bool() with False Arguments
```

# bool() with an empty argument

```bash
test = []

print(test, 'is' ,bool(test))
```

# bool() with zero

```bash
test1 = 0

print(test1, 'is' ,bool(test1))
```

This code assigns the value 0 to the variable `test1`, then prints the value of `test1` and a message that indicates whether `test1` is considered "truthy" or "falsy" in Python.

In this case, `bool(test1)` returns `False` because `0` is considered "falsy" in Python.

Therefore, the output of the code will be: `0 is False`

# bool() with none

```bash
test2 = None

print(test2, 'is' ,bool(test2))
```

# bool() with False

```bash
test3 = False

print(test3, 'is' ,bool(test3))
```

## bool() with False Arguments

```other
test = []
# bool() with an empty argument
print(test, 'is' ,bool(test))

test1 = 0
# bool() with zero
print(test1, 'is' ,bool(test1))

test2 = None
# bool() with none
print(test2, 'is' ,bool(test2))

test3 = False
# bool() with False
print(test3, 'is' ,bool(test3))
```

