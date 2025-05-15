---
tags: ["vue", "typescript", "type assertions", "type arguments"]
---


```js
defineEmits<{
	(e: "@create", entry: { text: string; emoji: Emoji | null}): void;
	(e: "@someOtherEvent", payload: string): void;
}>();
```

- the `< >` symbols signify that we are using type assertion
- the curly brackets `{ }` mean were passing a type literal as the type argument
- `{ text: string; emoji: Emoji | null}` is the payload
- 