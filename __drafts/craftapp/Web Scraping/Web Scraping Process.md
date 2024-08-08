# Web Scraping Process

1. Extract the HTML content using the `requests` library.
2. Analyze the HTML structure and identify the tags which have our content.
3. Extract the tags using Beautiful Soup and put the data in a Python list.

**Tools:**

- [https://webscraper.io/](https://webscraper.io/)

---

## 1. Get HTML

```python
from bs4 import BeautifulSoup
import requests
```

```python
url = 'https://notes.ayushsharma.in/technology'
r = requests.get(url)
  
soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
```

### GET CONTENT *from* HTML

1. identify the html `tags` that have the data you want

## 2. Analyze structure

## 3.Beautiful Soup

Beautiful Soup transforms a complex HTML document into a complex tree of Python objects. But you’ll only ever have to deal with about four kinds of objects:

1. Tag
2. NavigableString
3. BeautifulSoup
4. Comment

---

## Tags

A `Tag` object corresponds to an XML or HTML tag in the original document.

### Tag attributes

- `t.name`: the text between the html tags

### HTML tag examples

**HTML Text Tags:**

`<p>, <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, <strong>, <em>, <abbr>, <acronym>, <address>, <bdo>, <blockquote>, <cite>, <q>, <code>, <ins>, <del>, <dfn>, <kbd>, <pre>, <samp>, <var>, <br>`

**HTML Link Tags:**

`<a>, <base>`

**HTML Image and Object Tags:**

`<img>, <area>, <map>, <param>, <object>`

**HTML List Tags:**

`<ul>, <ol>, <li>, <dl>, <dt>, <dd>`

## Attributes

A tag may have any number of attributes.

The tag `<b id="boldest">` has an *attribute* “id” whose *value* is “boldest”.

You can access a tag’s *attributes* by treating the tag like a dictionary:

