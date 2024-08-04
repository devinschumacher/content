## What is Bundling?

Developers break up their application into modules, components, and functions that can be used to build larger pieces of their application. 

Exporting and importing these internal modules, as well as external third-party packages, creates a complex web of file dependencies:

![](bundling.png)

Bundling is the process of resolving the web of dependencies and merging (or ‘packaging’) the files (or modules) into optimized bundles for the browser. 

The goal is to reduce the number of requests for files when a user visits a web page.