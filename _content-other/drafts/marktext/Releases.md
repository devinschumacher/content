# Release

Releases are ways to "checkpoint" code at various stages/iterations to say that it is ready for use. They allow you to refer to source code at any given point in time, and even deploy that version of it to see it, test it, etc.

Releases are accompanied by unique identifiers that can be used to reference it - most notably a "version number" - the most popular syntax being one that follows [Semantic Versioning](https://semver.org/).

## Semantic versioning

Semantic versioning is a simple set of rules and requirements that dictate how version numbers are assigned and incremented.

**Given a version number MAJOR.MINOR.PATCH, increment the:**

1. MAJOR version when you make incompatible API changes
2. MINOR version when you add functionality in a backward compatible manner
3. PATCH version when you make backward compatible bug fixes

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

## Creating a release

In Github, releases are tied to Github tags. You can create a release based on an existing tag, or you can create a release and let Github create its corresponding tag automatically (see example below).

**You can create a release in Github via:**

1. Github Website GUI

2. Github CLI

3. Github Actions

```bash
gh release create v1.0.0 --notes "My first release"
https://github.com/<organization>/<repo>/releases/tag/v1.0.0
```

When a release is created, Github will automatically build 2 assets for the release:

1. The source code as a .zip file

2. The source code as a tarball (tar.gz).

> *You can specify additional assets to include in a release upon creation*

### Release notes

When you make a release, you shoudl also make release notes - docs that explain what is in the release. Release notes will typically include:

- New features

- Bug fiex

- New project contributors

- Short guidelines on install/upgrade

You can have Github automaically generate release notes based on the diff between the current release, and the most recent previous release.

**This auto-generated release includes:**

- Release notes with each change on its own line

- A link to the "Full changelog"

- A link to the PR from the commit title

- A line for the release author

### Release via Github Actions Example

Github Action to create a new release everytime you create (and push upstream) a tag that starts with the letter `v`:

```yaml
name: Create new release

on:
  push:
    tags:
      - 'v*'

jobs:
  new-release:
    runs-on: ubuntu-latest

    steps:
      - name: Create new release
        uses: actions/create-release@v1
        with:
          tag_name: ${{ github.ref }}
          release_name: ${{ github.ref }}
          body: New release!
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```
