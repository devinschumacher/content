Snapshot tests are a very useful tool whenever you want to make sure the output of your functions does not change unexpectedly.

When using snapshot, Vitest will take a snapshot of the given value, then compare it to a reference snapshot file stored alongside the test. 

The test will fail if the two snapshots do not match: **either the change is unexpected, or the reference snapshot needs to be updated to the new version of the result.**

To snapshot a value, you can use the [`toMatchSnapshot()`](https://vitest.dev/api/expect#tomatchsnapshot) from `expect()` API:

```js
import { expect, it } from 'vitest'

it('toUpperCase', () => {
  const result = toUpperCase('foobar')
  expect(result).toMatchSnapshot()
})
```

The first time this test is run, Vitest creates a snapshot file that looks like this:

```js
// Vitest Snapshot v1, https://vitest.dev/guide/snapshot.html

exports['toUpperCase 1'] = '"FOOBAR"'
```

> The snapshot artifact should be committed alongside code changes, and reviewed as part of your code review process

**WARNING**

*When using Snapshots with async concurrent tests, `expect` from the local [Test Context](https://vitest.dev/guide/test-context) must be used to ensure the right test is detected.*



## References

- https://vitest.dev/guide/snapshot