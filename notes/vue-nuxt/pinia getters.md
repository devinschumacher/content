#WIP 

Think of a "getter" like a personal shopper. They go to a `store` and "get" some stuff, and do something with it - like try it on, or bring it to your house and present the options, whatever.

Getters access data from a pinia store and do something with that data.

Getter's data is not original. It's data based on other pre-existing data (aka computed data or dependent data) such as data from the pinia store.

Getters are defined in the `.js` pinia store file.

```js
// stores/jobs.js
export const useJobsStore = defineStore("jobs", {
  state: () => ({
    jobs: [],
  }),
  actions: {
    async [FETCH_JOBS]() {
      const jobs = await getJobs();
      this.jobs = jobs;
    },
  },
  getters: {
    [UNIQUE_ORGANIZATIONS](state) {
      const uniqueOrganizations = new Set();
      state.jobs.forEach((job) => uniqueOrganizations.add(job.organization))
      return uniqueOrganizations;
    }
  }
});

```

- Need to grab some raw, original data to use in your components? Go to the store, and access the "state".
- Need to grab some data and *do something with it*? Go to the store and access a "getter".


The structure of a pinia store, like `useJobsStore` mirrors your Vue components.

| Pinia Store Property | Vue Component Equivalent      |
|----------------------|-------------------------------|
| `state`              | `data()`                      |
| `actions`            | `methods`                     |
| `getters`            | `computed properties`         |


Your pinia store has some data. The getters do something with that data (compute/calculate) and your component accesses that data from the global state.
