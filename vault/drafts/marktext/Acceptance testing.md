# Acceptance testing

An acceptance test is a formal description of the behavior of a software product, generally expressed as an example or a usage scenario.

They are written first in TDD to describe the behavior / user story of a particular feature about to be worked on. 

The developer will work on the feature by writing tests & code line by line (with unit tests, which test individual lines of code) to develop the full feature/behavior.

**Once enough code has been written to satisfy the behavior of the feature:**

- the acceptance test should pass

- the developer should consider the "issue" or "tassk" as ready to be pushed into the remote repository & kick off CI.

<img title="" src="file:///Users/devin/Library/Application%20Support/marktext/images/7d464ff7c08c474feed896c75eb53d33bac6a364.jpg" alt="double-loop-tdd-simpler.jpg" data-align="center" width="555">

---

>  The terms “functional test”, “acceptance test” and “customer test” are used more or less interchangeably. A more specific term “story test”, referring to [user stories](https://www.agilealliance.org/glossary/user-stories/) is also used, as in the phrase “story test driven development”.

## Acceptance test benefits

- Definining a clear scope of work for a task, and guiding the developer to stay focused on the task (not going off track, or scope creeping).

- Decreasing the chance and severity both of new defects and regressions.
