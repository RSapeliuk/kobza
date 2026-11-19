# Contributors guidelines

This document summarizes the most important points for people interested in
contributing to Kobza, especially via bug reports or pull requests.

## Table of contents

- [Reporting bugs](#reporting-bugs)
- [Proposing features or improvements](#proposing-features-or-improvements)
- [Contributing pull requests](#contributing-pull-requests)

## Reporting bugs

Report bugs [here](https://github.com/RSapeliuk/kobza/issues/new?template=bug_report.yml).
Please follow the instructions in the template when you do.

Notably, please include a Minimal Reproduction Project (MRP), which is a small
project which reproduces the issue, with no unnecessary files included.

Make sure that the bug you are experiencing is reproducible on the latest
`master` branch. If you run into a bug which wasn't present in an earlier
version (what we call a _regression_), please mention it and clarify which
versions you tested (both the one(s) working and the one(s) exhibiting the bug).

## Proposing features or improvements

Open an issue in the [issue tracker](https://github.com/RSapeliuk/kobza/issues)
describing the problem you want to solve and how you would solve it. Discussing
a feature before implementing it saves time for everyone.

## Contributing pull requests

If you want to add new engine features, please make sure that:

- This functionality is desired, which means that it solves a common use case
  that several users will need in their real-life projects.
- It has been discussed in an issue first, see
  [Proposing features or improvements](#proposing-features-or-improvements).

Similar rules can be applied when contributing bug fixes - it's always best to
discuss the implementation in the bug report first if you are not 100% sure
about what would be the best fix.

### Be mindful of your commits

Try to make simple PRs that handle one specific topic. It's better to open 3
different PRs that each address a different issue than one big PR with three
commits. This makes it easier to review, approve, and merge the changes
independently.

When updating your fork with upstream changes, please use ``git pull --rebase``
to avoid creating "merge commits".

Also try to make commits that bring the engine from one stable state to another
stable state, i.e. if your first commit has a bug that you fixed in the second
commit, try to merge them together before making your pull request.

### Format your commit messages with readability in mind

A Git commit message is formatted as a short title (first line) and an extended
description (everything after the first line and an empty separation line).

Try to keep the title under 72 characters. It should be written in English,
starting with a capital letter, and usually with a verb in imperative form.
A prefix can be added to specify the engine area affected by the commit.
Some examples:

- Add C# iOS support
- Show doc tooltips when hovering properties in the theme editor
- Core: Fix `Object::has_method()` for script static methods

If your commit fixes a reported issue, mention it in the _description_ of the
PR using one of the [GitHub closing keywords](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue)
such as "Fixes #1234".

### Document your changes

If your pull request adds methods, properties or signals that are exposed to
scripting APIs, you **must** update the class reference XML files in `doc/`
to document those.

If your pull request modifies parts of the code in a non-obvious way, add
comments in the code as well.

### Write unit tests

When fixing a bug or contributing a new feature, include unit tests (in the
`tests/` folder) in the same commit as the rest of the pull request. For bugs,
the tests should cover the functionality that was previously broken. For new
features, they should cover both the "success" and "expected failure" cases.

### Disclose use of AI

Use of AI tools must be disclosed in the pull request description, together
with a short description of how they were used.

Thanks for your interest in contributing!
