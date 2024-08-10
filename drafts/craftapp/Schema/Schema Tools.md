# Schema Tools

1. [Schema Markup Validator](https://validator.schema.org/) - for testing generic [schema.org](http://schema.org) markup, without Google specific validation.
2. [Rich Results Test](https://search.google.com/test/rich-results) - for testing [schema.org](http://schema.org) markup, with specific Google rich snippet validation.
3. [URL Inspection Tool](https://support.google.com/webmasters/answer/9012289?hl=en) - for getting info about an indexed version of specific page, or tests if a URL if indexable, with info about: structured data, video, linked AMP indexability.
4. [Google Search Central: Structured Data Guidelines](https://developers.google.com/search/docs/guides/sd-policies)
5. [Google Structured Data Markup Helper](https://www.google.com/webmasters/markup-helper/u/0/?)
6. [Merkle Schema Markup Generator](https://technicalseo.com/seo-tools/schema-markup-generator/)

## Schema Markup Validator

## Rich Results Test Tool

The Rich Results Test displays what rich result types were found on your page, and any errors or recommendations for your structured data.

If it finds errors/warnings, you can click on them to drill down and get specifics on the issue & how to fix them.

- [Rich Results Testing Tool](https://search.google.com/test/rich-results)

### URL status

The tool can report any the following status values for a tested URL where ***N*** depends on the number of items found.

- N valid item(s) detected
- No items detected
- N valid item(s) with warnings detected
- N valid items detected: All have warnings
- N valid items detected: Some have warnings
- N items detected: Some are invalid
- N invalid item(s) detected
- URL cannot be crawled
- Structured data with syntax errors detected

### [Crawling](https://support.google.com/webmasters/answer/7646114)

This section describes whether Google is permitted to crawl the page. If Google is prevented from crawling the page as part of its regular crawl cycle (for example, is prevented from crawling by a [robots.txt](https://support.google.com/webmasters/answer/12818275) rule or noindex directive), the page cannot be tested with this tool.

- [**Crawled**](https://support.google.com/webmasters/answer/7643010) **successfully /** [**Crawl**](https://support.google.com/webmasters/answer/7643418)** failed:**
- **Crawled as:** Shows the type of user agent used for the crawl (smartphone or desktop)
- **Crawl allowed?** Tests whether a robots.txt rule on the site prevents this page from being crawled.
- **Page fetch:** Whether the page could be fetched by the test. If crawling failed, this will always fail.

### Detected Items / Detected structured data

Whether any structured data items were found on the page. If structured data was found but could not be parsed, that will be indicated here.

Any items found, whether good, with warnings or errors, or unparseable, will be listed here, along with a description of the item and any issues.

## URL Inspection Tool

The URL Inspection tool allows you to check whether a URL might be indexable and provides details about the version of a specific page that Google has indexed.

Such as: specifics regarding video, linked AMP, structured data, and indexing/indexability.

### Use Cases

**URL index check**: Get details about the version of your page that Google has indexed. Find out why Google was unable to index your page.

**Check live URL**: Check to if a page is potentially indexable.

**Request URL indexing**: Ask Google to crawl a URL.

**View rendered page**: a screenshot of the page as seen by Googlebot. Look at the loaded resources, the JavaScript output, and other data: Click View crawled page > More info (indexed result) or View tested page > More info to view a list of resources, the page's code, and other details (live test).

**Investigate missing pages:** There are numerous reasons a page may not have been indexed. Some of them can be troubleshooted using URL Inspection.

**Discover canonical pages**: Check the Page indexing > Google-selected canonical field on the page's indexed version. Only the indexed data can be used to identify the canonical version; a live test cannot foretell whether a version will be regarded as canonical or not.

## Google Search Central:Structured Data Guidelines

## Google Structured Data Markup Helper

## Merkle Schema Markup Generator

