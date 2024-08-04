# Schema Glossary: Structured Data Terminology, Syntax & Vocabulary

[Schema.org](http://Schema.org) is a set up standards created for website's to clarify the things on them for web crawlers to more easily understand what they're reading.

It's a collection of 'items' in a hierarchical structure.

These items start with just 2 types at the top of the hierarchy: **types** & **data types**.

Already kind of confusing that they started the f-ckin' thing by having a hierarchy with "Type" and "DataType" at the top.

Logically, a "DataType" would already be underneath "Type" IMO.

[**Schema.org**](http://Schema.org) **also says this:**

*>[Schema.org](http://Schema.org) is defined as two hierarchies: one for textual property values, and one for the things that they describe.

*> This is the main* [*schema.org*](http://schema.org)* hierarchy: a collection of types (or "classes"), each of which has one or more parent types. Although a type may have more than one super-type, here we show each type in one branch of the tree only. There is also a parallel hierarchy for* [*data types*](https://schema.org/docs/full.html#datatype_tree)*.**

- A hierarchy for textual property values
- A hierarchy for things that they describe
- The main hierarchy "a collection of types"
- A parralell hierarchy for data types.

It almost made sense, if the main hierarchy was "a collection of types" that included textual property values & the things they describe…

And the other hierarchy was just the paralell data types…

But they make it sound like there is 4 hierarchies, right after saying there's two.

🤦‍♂️

But whatever - welcome to the internet where nothing really ever fully makes sense.

## Types

Types (also called "classes") define things.

Each **type** can have one or more **parent types** (aka "superclasses") and one or more **child types** (aka "subclasses").

Each

## Data Types

## Terminology

### Property

A `Property` is a characteristic or attribute of an entity (e.g. a person, place, organization, etc.) that can be described using a value. For example, the `name` property of a `Person` entity might have a value of "John Doe".

John Doe

- Entity: Person

### Properties

[Schema.org](http://Schema.org) "properties" are a set of standards for describing and organizing information about a particular topic on a website.

Think of it like a label for the information you're trying to convey.

By using these standardized labels, search engines like Google can better understand the content of your website and display it more accurately in search results.

Here's an example of [schema.org](http://schema.org) "properties" being used in JSON-LD:

```json
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "John's Pizza",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "New York",
    "addressRegion": "NY",
    "postalCode": "10001",
    "addressCountry": "USA"
  },
  "telephone": "(123) 456-7890",
  "priceRange": "$$"
}
</script>
```

Common "properties" and examples of corresponding "values", along with a brief explanation:

- `@type`: The type of entity being described, e.g. `Person`, `Organization`, `Place`, `Event`, etc.
- `name`: The name of the entity being described.
- `address`: The physical address of the entity, often including `streetAddress`, `addressLocality`, `addressRegion`, `postalCode`, and `addressCountry`.
- `telephone`: The telephone number of the entity.
- `priceRange`: A general indicator of the cost of goods or services at the entity, e.g. `$`, `$$`, `$$$`, etc.
- `image`: A URL to an image that represents the entity.
- `description`: A brief description of the entity.
- `url`: The URL of the entity's website.

## Syntax

## Vocabulary

