the typescript enum type assigns labels to numbers, which helps with human-readable situations.

the typescript enum type is a 'special type' (not built-in).

you create an enum type with the syntax: `enum TypeName {}`

for example

```ts

enum Role { ADMIN, READ_ONLY, AUTHOR }
// ADMIN: 0
// READ_ONLY: 1
// AUTHOR: 2

```

this will automatically associate index numbers with each property.



if you want to bypass/customize this default behavior of assigning numbers starting with 0, you can manually assign what you want like this:

```ts

enum Role { ADMIN = 5, READ_ONLY, AUTHOR}
// ADMIN: 5
// READ_ONLY: 6
// AUTHOR: 7


enum Role { ADMIN = 5, READ_ONLY = 180, AUTHOR = 'banana' }
// ADMIN: 5
// READ_ONLY: 180
// AUTHOR: banana
```