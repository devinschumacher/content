1. Create an account and get your API key
2.  `<script>` section

```ts
// put this in whatever component or page you want
// app.vue

<script setup lang='ts'>
async function citiesLookup(query: string) {
	const apiKey = '1f6ec271f3da959c1db1575514f66264';
	const response = await $fetch(
	`http://api.openweathermap.org/geo/1.0/direct?q=${query}&limit=5&appid=${apiKey}`
	);
	return response;
};

// testing the API (use devtools console to see)
const data = await citiesLookup('los angeles');
console.log(data)

</script>
```

3. 