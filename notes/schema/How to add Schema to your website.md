# How to add Schema to your website

Schema can be added to your website in a variety of ways. First are the options for choosing what type of code you will use.

[Schema.org](http://Schema.org) supports "many different encodings, including [RDFa](https://rdfa.info/), [Microdata](https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata) and [JSON-LD](https://json-ld.org/)."

JSON-LD is used for data in a simple [JavaScript](https://devinschumacher.com/category/javascript/)-oriented object notation and is Google's preferred format for structured data[^1].

JSON-LD should be inside `<script>` tags, and can be added either to the `<head>` section or `<body>` section of your HTML.

### Example adding schema to your website

1. Add a `script` tag with the `type` attribute set to `application/ld+json` to your website's HTML.

```html
<html>
	<head>
		<script type="application/ld+json">
		</script>
	</head>
</html>
```

Inside the tags, define which 'standard' for schema you're using (whos rules are you following here?) with the [schema.org](http://schema.org) `@context`

- > The order of the properties doesn't matter.

—

## "Collection" pages

Some pages focus on a single thing. Like an 'author page' for example. For these types of pages you use use the single "item type", in this case the "Person" item type.

Other pages have multiple instances of a single type of thing (let's call them "collection pages"), like a page with multiple people on it. Maybe an "authors" page that lists all of the website's writers and links down to their individual author pages.

For these collecion pages, mark up each item individually, and add the url property to the link to the page that corresponds with each item.

