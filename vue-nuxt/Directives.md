A Vue directive is a custom HTML attribute that changes the normal behavior of the HTML element it is added to. 

Think of them like "special [HTML Attributes](HTML%20Attributes.md)".

Vue has a number of built-in directives that come with the Vue application; they start with `v-` prefix.

They are part of the Vue template syntax.

Some directives have (require) "values", some don't.

**For example**: `v-cloak` as a directive in HTML: 

```vue
<div id="app" v-cloak>
```
It does not have a required "value", meaning it can be placed in the HTML as an attribute with no "value" (think key:value attribute pairs).

Some directives do require a value, like `v-model`.

**For example**: `<input type="text" v-model="firstName" />`

Some directives have "arguments", like: `v-bind`.

**For example**: `<div v-bind:id="dynamicId"></div>`

The part after the colon (`:`)  is the 'argument' of the directive.


## Vue Built-in Directives

Here are some of the more common Vue built-in directives:

- `v-bind:`
- `v-on:` - listens to DOM events
- `v-model`: two way binding for forms. automatically syncs the `<input>`'s value with the bound state, so we no longer need to use an event handler for that.
- `v-if`
- `v-cloak`


## Vue directives in the browser
Vue directives become HTML attributes in the browser. 

> **Remember**: HTML Attributes can be selected using CSS Selectors - the selector for HTML attributes is a pair of square brackets: ` [ ] `



## Vue custom directives

You can also create your own 'custom directives'.