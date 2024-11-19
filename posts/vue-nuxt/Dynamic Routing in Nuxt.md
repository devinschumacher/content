
## How to add dynamic routes

1. Add a`.vue` file in the `pages/` directory with a 'route parameter' in brackets (  `[]` ).

The brackets act as a placeholder for your route parameter.

Route parameter is just a variable in the filename that represents something that will be put into the URL structure, and can be used in the template to do things dynamically.

Example: `pages/category/[category].vue`

This would make the url `site.com/category/<category>/` where anything put after `/category/` would become the URL slug and be able to be used for filter that page (for example by the category of something)


## How to use dynamic routing in Nuxt to create a filterable category page

The script section: 

```js

```


## How to use dynamic routing validation