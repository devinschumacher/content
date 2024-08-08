# Write Tests for Defects

Developer testing and CI may decrease the frequency of software defects, but

the fact of the matter is that defects will still occur. That’s okay, though—
mistakes happen and mistakes can be fixed and, ideally, learned from. Making
the same mistake twice, though, is quite unforgivable.

Some use the term defect-driven development when referring to writing tests
for defects; however, that term has always sounded rather negative. Defects
don’t drive development—preventing those nasty aberrations drives
development! If anything, defects halt development—it’s the act of addressing
them and then ensuring they don’t come back that keeps the wheels moving.
Here is a proven strategy for guaranteeing that once a defect is found, it doesn’t
come back.

When a defect is discovered, find and isolate the offending code. If the project
has a healthy number of test cases, it’s probably a good bet that the defect has
occurred in some portion of untested code (maybe an unconsidered path)—and
most likely in the interaction of components. For example, Listing 6-12 presents
a method in a DAO class, which attempts to retrieve a
word from a database.

## Example 6-12. DAO with a Defect

![Screenshot 2023-12-13 at 23.32.55.png](/Users/devin/Library/Application%20Support/marktext/images/2aa5cb522bd27da31fe3b560d75c0b77a5fa1640.png)

This class has been reasonably tested in a series of component-level tests that
utilize DbUnit. These tests verify the basic CRUD (create, read, update, and
delete) operations. For example, Listing 6-13 shows a test for the  
method.

## Example 6-13. Sample Sunny Day Test Case

![](/Users/devin/Library/Application%20Support/marktext/images/2747ac35609d616d73784f6b4f6260628b8090ab.png)

During functional testing of the larger application (in this case, a dictionary), it is
discovered that if the user attempts to search for a word that isn’t in the
dictionary, the application heaves a nasty exception stack trace, which utterly
confuses users. After some crafty detective work, someone discovers that the

method in throws an unexpected (which is masked by a) if no word is returned via the API.

This aberrant behavior wasn’t accounted for! A defect has been discovered! All
is not lost, though. Remember, we are forgiven for creating this defect, but only once. We have an opportunity to fix this nefarious glitch, but if it breaks again we should rethink our approach.

The first step in regaining your pride is to write a test case that exposes the
defect. Read that sentence again slowly. Your first reaction may be to fix the
offending code and move on to other, more exciting things (happy hour!);
however, if you go that route, you lose an excellent chance to ensure that the
same bug never comes back again. Start by writing a test case that triggers the
same exact behavior that was reported in the defect summary. In this case, we
need to cause the code to throw an , such

as the one shown in Listing 6-14. Remember that we’re writing a test to pass on
the behavior, not to fail.

## Example 6-14. Test Case Verifying the Defect

![](/Users/devin/Library/Application%20Support/marktext/images/2e9a3f184638f17c1bbc82072af4d9820d03be5a.png)

If you run this test, it passes. Therefore, you’ve proven that there is a defect.
Now you can fix it.

This methodology, by the way, is slightly different than the prevailing “defect-
driven development” approach, which suggests writing a failing test case first
and then to keep running that test (while fixing the defect) until the test stops
failing. For example, the code in Listing 6-15 is a defect-driven test case.

## Example 6-15. Sample Defect-Driven Style Test Case

![](/Users/devin/Library/Application%20Support/marktext/images/3c79dd384cd8118b33ae7a56d0e57ed716866c0a.png)

This test case, of course, fails when first run (assuming the defect is still
present). This practice does work; however, it presents some opportunities for
refinement. Writing a test case that purposely fails at first present these
challenges.

It is difficult to write a failing test in this scenario that uses an assert properly.
Because of this, asserts may not ever be added, even after the test case
doesn’t fail anymore. This means the test case isn’t necessarily passing—it is
merely not failing.

At this point in the game, it is tricky to know how the fix will affect behavior,
so in attempting to fail the test you end up guessing what the fix may be.  
In Listing 6-15, the assumption is made that the fix will cause the code to no
longer throw an exception. This is true, but it’s only part of the whole story.
Once a fix has been made in the code under test, the failing test works;
however, it doesn’t actually verify the change in behavior.

At this point, because the test case works, most people don’t go back to update
it. In our case, in order to fix the defect we in essence need to break the test,
which is the opposite of what defect-driven development advocates.

Examining the code closely reveals that we need to check for an empty list
before attempting to grab the first element. We’re left with a design choice at
this point—should the code return , return an empty , or throw an
exception? The decision is made to return if the parameter value cannot
be retrieved from the database via Hibernate (see Listing 6-16).

## Example 6-16. Updated Code That Fixes the Defect

![](/Users/devin/Library/Application%20Support/marktext/images/11ad47921dc50d60f9a0870442e2837a3d3a0e1e.png)

With the code under test conceivably fixed, the test is run again and this time it
fails. This next decision is what differentiates this approach from others—in
fixing our test case, we will assert the new behavior. The defect-driven example
would work by now, and the chances are we’d leave the test case as so. But that
test case doesn’t provide too much value now. We need to assert that when an
invalid word is passed into the method, is returned. We
also need to assert than an isn’t thrown. The updated test case is
shown in Listing 6-17.

## Example 6-17. Updated Test Case Verifying the Fix

![](/Users/devin/Library/Application%20Support/marktext/images/a628c799db9aa2e487288c1598717fd017a84ac7.png)

Now we’re done and we’ve accomplished two things. First, the defect has been
corrected. Congratulations! Second, a regression test is now in place that truly
asserts the correct behavior of the fix.

Which practice should we follow: defect-driven development, or should we call
it continuous-prevention development? They both drive you to:

1. Fix the defect 

2. And prevent the defect from recurring

Continuous-prevention development, however, has the tendency to drive you to
carry out a third step, which is asserting any new behavior triggered by the
defect’s fix.
