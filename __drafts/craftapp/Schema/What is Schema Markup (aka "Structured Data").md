# What is Schema Markup (aka "Structured Data")

Webpages are built with HTML, which tell your web browser what information to display and a bit about how to display it (is it a heading, a bullet point list, a table, an image, etc.) using HTML 'tags'.

Let's say you had a page on your website about Mercury, and the main heading on the page was:

# Mercury

Maybe you even have a subheading under that which reads:

## Everything you need to know about Mercury

Pop quiz: What is this page about?

A. a [planet](https://www.britannica.com/place/Mercury-planet)

B. a [chemical element](https://www.epa.gov/mercury/basic-information-about-mercury)

C. a [car company](https://en.wikipedia.org/wiki/Mercury_(automobile))

D. the [lead singer Queen](https://en.wikipedia.org/wiki/Freddie_Mercury)

E. a song by [Bloc Party](https://www.blocparty.com/)

F. an [indian horror film](https://en.wikipedia.org/wiki/Mercury_(film))

At this point it's just a string of text, there's no way to know. And even though it is "marked up" with HTML, HTML only adds *structure* to a webpage, not details about the things on it.

This is where schema comes in to the mix, as a way to further "mark up" (aka add details) to things on websites so that web crawlers (namely search engines) can easily understand what's on them.

The example above was a simple one, but language is complex and so is the way we write things. There are many ways to say the same thing, and many ways to write the same thing.

Just think about dates for example. How many different ways are there to write the date?

Here's just a few examples, from a table taken from Oracle's documentation:

| **Format** | **Date order** | **Description**                                                                                                                                                                                                |
| ---------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | MM/DD/YY       | Month-Day-Year with leading zeros (02/17/2009)                                                                                                                                                                 |
| 2          | DD/MM/YY       | Day-Month-Year with leading zeros (17/02/2009)                                                                                                                                                                 |
| 3          | YY/MM/DD       | Year-Month-Day with leading zeros (2009/02/17)                                                                                                                                                                 |
| 4          | Month D, Yr    | Month name-Day-Year with no leading zeros  <br>(February 17, 2009)                                                                                                                                             |
| 5          | M/D/YY         | Month-Day-Year with no leading zeros (2/17/2009)                                                                                                                                                               |
| 6          | D/M/YY         | Day-Month-Year with no leading zeros (17/2/2009)                                                                                                                                                               |
| 7          | YY/M/D         | Year-Month-Day with no leading zeros (2009/2/17)                                                                                                                                                               |
| 8          | bM/bD/YY       | Month-Day-Year with spaces instead of leading zeros  <br>( 2/17/2009)                                                                                                                                          |
| 9          | bD/bM/YY       | Day-Month-Year with spaces instead of leading zeros  <br>(17/ 2/2009)                                                                                                                                          |
| A          | YY/bM/bD       | Year-Month-Day with spaces instead of leading zeros (2009/ 2/17)                                                                                                                                               |
| B          | MMDDYY         | Month-Day-Year with no separators (02172009)                                                                                                                                                                   |
| C          | DDMMYY         | Day-Month-Year with no separators (17022009)                                                                                                                                                                   |
| D          | YYMMDD         | Year-Month-Day with no separators (20090217)                                                                                                                                                                   |
| E          | MonDDYY        | Month abbreviation-Day-Year with leading zeros (Feb172009)                                                                                                                                                     |
| F          | DDMonYY        | Day-Month abbreviation-Year with leading zeros (17Feb2009)                                                                                                                                                     |
| G          | YYMonDD        | Year-Month abbreviation-Day with leading zeros (2009Feb17)                                                                                                                                                     |
| H          | day/YY         | Day of year (counting consecutively from January 1)-Year (48/2009)                                                                                                                                             |
| I          | YY/day         | Year-Day of Year (counting consecutively from January 1—often called the Julian date format) (2009/48)                                                                                                         |
| J          | D Month, Yr    | Day-Month name-Year (17 February, 2009)                                                                                                                                                                        |
| K          | Yr, Month D    | Year-Month name-Day (2009, February 17)                                                                                                                                                                        |
| L *        | Mon-DD-YYYY    | Month abbreviation, Day with leading zeros, Year  <br>(Feb 17, 2009)                                                                                                                                           |
| M *        | DD-Mon-YYYY    | Day with leading zeros, Month abbreviation, Year  <br>17 Feb, 2009.                                                                                                                                            |
| N          | YYYYY-Mon-DD   | Year, Month abbreviation, Day with leading zeros  <br>(2009, Feb 17)<br><br>This format defaults to a two-digit year, but can be overridden to have four digits.                                               |
| O          | Mon DD, YYYY   | Month abbreviation, Day with leading zeros, Year  <br>(Feb 17, 2014)                                                                                                                                           |
| P          | DD Mon, YYYY   | Day with leading zeros, Month abbreviation, Year  <br>(17 Feb, 2014)                                                                                                                                           |
| Q          | YYYY, Mon DD   | Year, Month abbreviation, Day with leading zeros  <br>(2014, Feb 17)                                                                                                                                           |
| X          | (hexadecimal)  | Eight-character hexadecimal representation of the system date. Valid dates range from 12/31/1969 to 01/18/2038. Valid dates may differ depending on the type of machine (PC or host) and the type of CPU chip. |

… you get it.

Adding this 'structured markup' to your website adds specificity to the data and defines exactly what to do & how to do so, ie: terminology, syntax and rules for marking up your websites - the same way humans have spelling & grammar rules for effective & precise communication.

## Benefits of Schema

*Well that sounds like a shitload of work, do I really have to go through all that?*

Google Search works hard to understand the content of a page, and structured data can help provide explicit clues about the meaning of a page to Google.

Structured data is a standardized format for providing information about a page and classifying the page content, such as ingredients and cooking time on a recipe page.

You add this structure by "marking up" your existing website content with additional code that follows a specific set of rules, that help Googlebot better understand what a web page is about.

Doing this will help your website show up on the search engine in the form of [SERP Features](https://devinschumacher.com/serp-features), which provide a more engaging experience for users, take up additional SERP real estate that increases your traffic, and help the overall performance of your SEO.

From here on out I'm just going to refer to it as "schema".

> TL;DR: Schema improves your SEO & get your website more visibility and traffic

## Terminology & Syntax

The syntax & vocabulary of structured data that you will follow is defined by [Schema.org](https://schema.org).

*"*[*Schema.org*](http://Schema.org)* is a collaborative, community activity with a mission to create, maintain, and promote schemas for structured data on the Internet, on web pages, in email messages, and beyond."*

[Schema.org](http://Schema.org) was founded by Google, Microsoft, Yahoo and Yandex specifically to develop a unified method of marking up data on the internet in a structured way so that it was easier to understand.

> TL;DR: Follow [schema.org](http://schema.org) standards because it Google like you more.

## Adding Schema to your website

Schema can be added to your website in a variety of ways. First are the options for choosing what type of code you will use.

[Schema.org](http://Schema.org) supports "many different encodings, including [RDFa](https://rdfa.info/), [Microdata](https://developer.mozilla.org/en-US/docs/Web/HTML/Microdata) and [JSON-LD](https://json-ld.org/)."

JSON-LD is used for data in a simple [JavaScript](https://devinschumacher.com/category/javascript/)-oriented object notation and is Google's preferred format for structured data[[^1]](craftdocs://open?blockId=27BF2874-C9A4-4E5A-B05D-884BCA09AD93&spaceId=null).

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

—

## Citations

#### 1

[https://codelabs.developers.google.com/codelabs/structured-data/index.html#2](https://codelabs.developers.google.com/codelabs/structured-data/index.html#2)

