# Python Lambda

Python Lambda is a way to create small, anonymous functions in Python. They are called "anonymous" because they don't have a name, unlike traditional Python functions.

Lambdas are typically used when you need to create a function quickly for a short period of time, and you don't want to go through the trouble of defining a traditional function.

They are also useful for creating simple, one-line functions that you might use as an argument to another function.

## Python Lambda Syntax

The syntax for a lambda is simple: you use the `lambda` keyword, followed by the function's arguments (if any), and then a colon.

lambda *arguments* : expression

After the colon, you put the expression that you want the function to return.

For example:

double = lambda x: x * 2

This creates a lambda that takes one argument (which we've called "x"), and returns that argument multiplied by 2.

We can call this lambda like any other function:

result = double(5)

print(result) # prints 10

Lambdas can be used anywhere you would use a regular function in Python, such as as an argument to the `map()` function, or as a key function for sorting a list.

## Python Lambda Examples (IRL)

Let's look at some real life examples of why/when to use python lambdas.

### Web development

Lambdas are often used in web development frameworks like Flask and Django, where they can be used to define small, one-off functions for handling specific HTTP requests.

For example, you might define a lambda to handle a POST request to a login form:

@app.route('/login', methods=['POST'])

def login():
username = request.form['username']
password = request.form['password']
user = User.query.filter_by(username=username).first()
if user and user.check_password(password):
login_user(user)
return redirect(url_for('dashboard'))
else:
return render_template('login.html', error='Invalid username or password')

Here, the `def login()` is a traditional function, but the lambda is used inside it to filter the user by username.

### Data analysis

Lambdas are commonly used in data analysis with Python libraries like NumPy and Pandas.

For example, you might use a lambda to compute the mean of a column of data:

import numpy as np

data = [3.4, 4.5, 2.3, 5.6, 1.2]

mean = np.mean(data, axis=0, keepdims=True, initial=0, where=lambda x: x > 2.5)

print(mean)

Here, the lambda is used to specify a condition that filters out any values less than or equal to 2.5 before computing the mean.

### Sorting

Lambdas are commonly used for sorting lists in Python.

For example, you might sort a list of tuples based on the second element of each tuple:

data = [(1, 2), (3, 1), (5, 3), (2, 4)]

sorted_data = sorted(data, key=lambda x: x[1])

print(sorted_data)

Here, the lambda is used to specify the second element of each tuple as the sorting key. This will sort the list based on the second element of each tuple.

## Python Lambda tidbits

- Lambda functions can take any number of arguments

\-

