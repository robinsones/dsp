# Upstream


### Objectives:

 * Make (or break) fork relationships.
 * Keep in sync by pulling from an "upstream" remote.


### Ideas:

 * You can `pull` commits from a remote repository to your local one to keep it in sync. (Equivalently, `fetch` and then `merge`.)
 * Local git repositories can reference more than one remote.


### Process:

 * Fork the class repository.
 * Clone your fork.
 * If there are changes in the original, how do you get them? You need to tell your local repo that it can also get updates from the original:

```bash
# add remote with the appropriate reference
git remote add upstream ...

# display configured remotes
git remote -v

# pull in changes
git pull upstream master
```
