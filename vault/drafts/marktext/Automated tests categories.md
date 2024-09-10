# test categories

A build should be fully automated. 

In order to run tests for a CI system, the tests must be automated. 

Writing your tests in an xUnit framework such as NUnit or JUnit will provide the capability of running these tests in an automated fashion. (for SERP that is framework is probably **Pytest**)

³ Continuous Integration (Kent Beck & Martin Fowler)

### Categorize Developer Tests

Writing and running tests is obviously a good thing, but unless we treat them as
an architectural component that requires proper categorization and structure,
they can start looking like a hurdle, instead of the key, to success. 

As the code base increases during your project, we’re talking about a lot of tests—and if you run all written tests at all times in your CI system, builds take longer and longer to complete.

1. Unit Tests

2. Component Tests

#### Unit Tests

People often use the term “unit test” rather broadly. This can cause confusion, especially when people start claiming their unit tests “take too long to run.”

Unit tests verify the behavior of small elements in a software system, which are most often a single class. Occasionally, though, the one-to-one relationship between a unit test and a class is slightly augmented with additional classes because the classes under test are tightly coupled.

A true unit test should run to completion (successfully) in a fraction of a second. 

If a unit test takes longer, take a close look at it—it’s either broken, or instead of being a unit test, it is really a component-level test.

If unit testing takes enough time that the developer can focus on something else, it’s taking too long. It will become a burden, and will soon become something to avoid instead of depend on.

In a CI environment, builds are run any time someone applies a change to the version control repository.¹

Therefore, unit tests should be run each time someone checks in code (called the commit build). There is little configuration cost, and the resource cost to run them is negligible.

- These unit tests should have no external dependencies such as a file system or database.

## Agile Testing (Lisa Crispin & Janet Gregory)

Software quality has many dimensions, each requiring a different testing
approach. 

- How do we know all the different types of tests we need to do?

- How do we know when we’re “done” testing? 

- Who does which tests and how? 

The Agile Testing Quadrants to make sure your team covers all needed categories of testing.

![agile testing quadrants.webp](/Users/devin/Library/Application%20Support/marktext/images/ba141e4fa8cec850173ec6c36070fb44ff537f36.webp)

### Quadrant 1

Quadrant 1, the lower left quadrant, represents **test-driven development** - a core agile
development practice.

- Unit Tests - verify functionality of a small subset of the system, such as an object or method.

- Component Tests - verify the behavior of a larger part of the system, such as a group of classes that provide some service.

We refer to these tests as "programmer tests", "developer-facing tests", or "technology-facing tests".

They enable the programmers to measure the internal quality of their code. 

Both types of tests are usually automated with a member of the xUnit family of test
automation tools.²

We can’t overemphasize the importance of automating the unit tests. 

If your programmers are using TDD as a mechanism to write their tests, then they are not only creating a great regression suite, but they are using them to design high-quality, robust code. 

💀 If your team is not automating unit tests, its chances of long-term success are slim. 

🚨 **Make unit-level test automation and continuous integration your first priority.**

---

¹ I think the Github equivalent of this statement is the "remote repository" (not your local).

² I think in Python language an "xUnit test family of test automation tools" would equate to our chosen unit test tool: Pytest

**References:**

- [Continuous Integration (Kent Beck & Martin Fowler)]()

- [Agile Testing (Lisa Crispin & Janet Gregory)](https://github.com/serpcompany/_books/blob/main/Agile%20Testing%20-%20A%20Practical%20Guide%20for%20Testers%20and%20Agile%20Teams.pdf)

- 
