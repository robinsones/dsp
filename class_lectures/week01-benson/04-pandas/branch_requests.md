# Branches and Pull Requests


### Objectives:

 * Use branches to organize work on a repository.
 * Use pull requests to submit challenges.
 * Get feedback and discuss work on GitHub.
 * Improve work and re-submit as needed.


### Ideas:

 * Git history is like a tree of commits, and you can work on different named "growth points" called branches.
 * On GitHub, you can submit changes by asking that they be pulled in by someone else - this is called a pull request.


### Process:

* First, get into the right directory (any directory in your local repository) and make sure you're on the master branch:

```
    git branch
    git checkout master
```

* Get up to date with the "official" repo:
```
    git pull upstream master
```
    
 * Create a new branch to use:
```
    git checkout -b benson_challenges
```
 * Change branches:

```
git checkout master
git checkout benson_challenges
```
Work on some files (or add files from elsewhere) and make commits:

```
    cp ~/my_great_homework.py ./correct/path/nyc16_ds8/challenges/submissions/00-practice(for_example)/username
    git add ./correct/path/nyc16_ds8/challenges/submissions/00-practice(for_example)/username/my_great_homework.py
    git commit -m "initial version"
```

 * Push your branch to your fork on GitHub:
```
    git push origin benson_challenges
```

* Make a pull request on GitHub.

* When you sync up, sync up `master`! 

```
git checkout master
git pull upstream master
```

It's possible to do pull requests from your `master` branch, but this puts you in an awkward position where you're waiting for the pull request to get merged before it's safe for you to sync up again. Topic branches are highly recommended.


 * (BTW) Note that you have a `~/.gitconfig` file, which you can customize. I never type this, for example:
```
git log --graph --decorate --pretty=oneline --abbrev-commit --all
```
