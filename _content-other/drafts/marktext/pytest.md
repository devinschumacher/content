# pytest

pytest is a software testing framework, and command line tool, that automatically finds tests you've written, runs them and reports the results.

We (the programmer) write "test code" that tests our "application code". 

>  **Application code**: The code we are validating with tests.

Application code has other names:

- production code

- code under test (CUT)

- system under test (SUT)

- device under test (DUT)

- etc.

## Test naming conventions

- Test files: should start with `test_` or end with `_test`(ex: `test_something.py` o``r `something_test.py`)

- Test methods & functions: should start with `test_` (ex: `test_something`)

- Test classes: should start with `Test` (ex: `TestSomething`)

## Running pytest

To run pytest, you will call `pytest` by itself, or with an optionally added file or directory - which will tell pytest where to look for tests.

## Test discovery

How does pytest find your tests?

- No arguments - pytest looks at your current directory and all subdirectories for test files
  
   - `$ pytest`

- Directory name - pytest will look there, and all subdirectories
  
   - `$ pytest directory_name`

- File name - pytest will look there
  
   - `$ pytest file_name.py`

- Testname - 

- Class name - 

- Method name - 
