---
title: How to Make a Scrollable Carousel Component/Element with TailwindCSS without Using a Carousel
---
> **Note**: This it's not technically a carousel because it doesn't go around when you've hit the end, but it's a much lighter / simpler implementation for the SEO benefit.

All you have to do to make a component scrollable horizontally like a carousel is to apply `overflow-x-auto` to it's surrounding `<div>` element.

Here is the same component without, and then with, the `overflow-x-auto` utility class on it's surrounding `<div>` :

**Without `overflow-x-auto`:**

![](without%20overflow-x-auto.png)


**With `overflow-x-auto`:**

![](with%20overflow-x-auto.png)

