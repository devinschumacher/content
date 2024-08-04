# Parallelization

Running tests in parallel means that you can run a category of tests much faster.

In general, you can run 1 test per CPU core, so if you have an 8-core CPU you can theoretically run 8 tests in parallel - making your full category of tests run 8x faster.

## When can tests run in parallel

For tests to be able to run in parallel they need to meet the following criteria:

1. Must not depend on each other

2. Must be able to run in any order

3. Must not interfere with each other
