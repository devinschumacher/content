# News Article Schema

Adding `Article` structured data to your news, blog, and sports article pages can help Google understand more about the web page and show better [title text](https://developers.google.com/search/docs/appearance/title-link), images, and [date information](https://developers.google.com/search/docs/appearance/publication-dates) for the article in search results on Google Search and other properties (for example, Google News and the [Google Assistant](https://developers.google.com/assistant/content/overview)).

While there's no markup requirement to be eligible for Google News features like [Top stories](https://support.google.com/news/publisher-center/answer/9607026), you can add `Article` to more explicitly tell Google what your content is about (for example, that it's a news article, who the author is, or what the title of the article is).

## Example

```html
<script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "NewsArticle",
      "headline": "Title of a News Article",
      "image": [
        "https://example.com/photos/1x1/photo.jpg",
        "https://example.com/photos/4x3/photo.jpg",
        "https://example.com/photos/16x9/photo.jpg"
       ],
      "datePublished": "2015-02-05T08:00:00+08:00",
      "dateModified": "2015-02-05T09:20:00+08:00",
      "author": [{
          "@type": "Person",
          "name": "Jane Doe",
          "url": "https://example.com/profile/janedoe123"
        },{
          "@type": "Person",
          "name": "John Doe",
          "url": "https://example.com/profile/johndoe123"
      }]
    }
    </script>
```

