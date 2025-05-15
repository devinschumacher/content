Type aliases can be used to "create" your own types; with the keyword `type`

```ts
// create a custom type for a union of number & string
type myCustomType = number | string;
```

Now you can use `myCustomType` anywhere in your code without having to continually declare its type, and manage the type from a single location / externally.