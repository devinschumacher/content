---
tags:
  - SOP
  - Nuxt
  - Supabase
---

## 1. Initialize the Nuxt built-in Supabase composable

```js
<script setup>
	const supabase = useSupabaseClient();
<script>
```

*** not sure what #bestpractice is here for which component's/page's `<script setup>` to put this in. #TODO

## 2. Set a variable for your query to an empty ref()

In this example the DB table we are querying is called 'transactions'.

```js
<script setup>
	const transactions = ref([]);
<script>
```


## 3. Write your database query

You can get pre-made javascript database queries from the supabase DOCS in the javascript reference section.

Add your database query to the `<script setup>` area, wrapped in a Nuxt `useAsyncData()` function (so you dont query the data twice -- once from the server and once from the client).

```js
<script setup>
	const { data,pending } = await useAsyncData(
		'transactions', async () => {
			const { data,error } = await supabase
			.from('transactions')
			.select();

    if (error) return [];
    return data;
<script>
});
```


## 4. Add props to your component

> Switch over to the `Component.vue` file

Add props to your component relevant to the database query/object you're getting data from

```js
// Component.vue

<script setup>
	const props = defineProps({
		transaction: Object
	})	
```

## 5. Add your component props attributes to the `<template>` section

> Back in the page...

In your `<template>` section where you'er using the component that will be receiving/displaying the data, reference your props with normal Vue directives.

You will make the DB query data accessible in the component by binding the props object you made in the previous step ( `:transaction=transaction"` ):

```js
// let's say your adding stuff to your Transaction.vue component
<template>
	<Transaction v-for="transaction in transactions" :key="transaction.id" :transaction="transaction" />
</template>
```