---
title: "Django 101: Introduction to the Python Web Framework"
author:
	- Devin Schumacher
...

# Introduction to Django

**Django**: The web framework for perfectionists with dealines.

Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

With Django, you can take web applications from concept to launch in a matter of hours. Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

Django is a free, open source web framework written in the Python programming language. First released in 2005, Django has been in continuous development since then and today powers many of the largest websites in the world including Instagram, Pinterest, Bitbucket, and Disqus.

At the same time, it is flexible enough to be a popular choice for early-stage startups and side projects.

## How Django Works

Most websites need the same basic functionality: the ability to connect to a database, set URL routes, display content on a page, handle security properly, and so on. 

So, Rather than recreate all of this from scratch, programmers over the years have created web frameworks in all the major programming languages.

Django is classified as a website *framework*. A collection of tools that abstract away much of the difficulty, and repetition, inherent in web development.

For example: You can use Django *without* a database, but it does come with an [object-relational mapper](https://en.wikipedia.org/wiki/Object-relational_mapping) that allows you to easily describe your database layout in Python code.

> Django is a Python framework that makes it easier to create web sites using Python.

> Django takes care of the difficult stuff so that you can concentrate on building your web applications.

### Django + MVT

**Django**, a Python framework to create web applications, is based on Model-View-Template (MVT) architecture. **MVT** is a software design pattern for developing a web application. It consists of the following three entities:

1.  Model
2.  View
3.  Template

#### Model

A **Model** is an object that defines the structure of the data in the Django application.

It is responsible for maintaining the entire application’s data for which it provides various mechanisms to add, update, read and delete the data in the database.

In Django, the data is delivered as an Object Relational Mapping (ORM), which is a technique designed to make it easier to work with databases.

The most common way to extract data from a database is SQL. One problem with SQL is that you have to have a pretty good understanding of the database structure to be able to work with it.

Django, with ORM, makes it easier to communicate with the database, without having to write complex SQL statements.

The models are usually located in a file called `models.py`.

#### Views

A **View** is a function, or method, that accepts HTTP requests, processes them, and returns the HTTP response.

It retrieves the necessary data to fulfill the request using Models and renders them on the user interface using Templates.

The views are usually located in a file called `views.py`.

Let's think of views as instructions for what to do when URLs (aka pages) are clicked on and visited, for now.

#### Templates

A **Template** is a text file that defines the structure or layout of the user interface - where you describe how the result should be represented. 

The text file can be any type of file; for example HTML, XML, etc.

Django uses standard HTML to describe the layout, but adds tags to add functionality & logic.

```html

<h1>Welcome to my website</h1>

<p>My name is {{ firstname }}.</p>

```

The templates of an application is located in a folder named `templates`.

#### URLs

Cant have a websit without URLs!

Django provides a way to navigate around the different pages in a website.

When a user requests a URL, Django decides which _view_ it will send it to - remember those 'instructions' from earlier?

This is done in a file called `urls.py`.

### Putting it together

You install Django, and create your first Django web application. When the browser requests a URL, this is how it shakes out:

1.  Django receives the URL, and checks the `urls.py` file, then calls the `view` that matches the URL.
2.  That `view` (found in `views.py`) checks for relevant `models`.
3.  The `models` are imported from the `models.py` file.
4.  Then `view` sends the data to a template specified by the `template` folder
5.  That `template` file contains the HTML & Django tags needed to return the data as finished HTML content back to the browser.


#### Getting Started

At this point you know enough to about Django to have a decent idea of what it does, and probably a mostly convoluted-understanding of what it is.

Which means it's time to toss the theory and get started on the installation and setup. 

Let's put a face to the name!




