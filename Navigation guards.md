Navigation guards are functions/methods which are called automatically by Vue router when a page changes or when a navigation action has started (similar to middleware).

```
router.beforeEach(function(to, from, next) {
next();
});
```

- `next()` confirms the route navigation, and allows it