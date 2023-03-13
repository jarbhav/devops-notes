# Git Commands

## **git init**
> Executing this command will create a new .git subdirectory in your current working directory. This will also create a new main branch. 

![](images/git-cmds/00-init.png)

![](images/git-cmds/01-init.png)

## **git clone**
>It is used to create a copy or clone of remote repositories.

![](images/git-cmds/21-clone.png)

## **git status**
> To view the state of the working directory and the staging area

![](images/git-cmds/02-status.png)

## **git config**
> This command is a convenience function that is used to set Git configuration values on a global or local project level

![](images/git-cmds//03-config.png)

## **git add**
>It adds a change in the working directory to the staging area

![](images/git-cmds/04-add.png)

## **git commit**
> It captures a snapshot of the project's currently staged changes.

![](images/git-cmds/05-commit.png)

## **git remote**
> This lets you create, view, and delete connections to other repositories

![](images/git-cmds/06-remote.png)

## **git push**
> Most commonly used to publish an upload local changes to a central repository

![](images/git-cmds/07-push.png)

## **git log**
> Lets you explore the previous revisions of a project. It provides several formatting options for displaying committed snapshots

![](images/git-cmds/08-log.png)

## **git reset**
> Undoes changes to files in the working directory. Resetting lets you clean up or completely remove changes that have not been pushed to a public repository.

![](images/git-cmds/09-rem_commit.png)

![](images/git-cmds/10-rem_commit.png)

## **git stash**
> Temporarily shelves (or stashes) changes you've made to your working copy so you can work on something else, and then come back and re-apply them later on.

![](images/git-cmds/11-stash.png)

### **git stash pop**
> Bring back changes to the staging area from the stash

![](images/git-cmds/12-stash_pop.png)

### **git stash clear**
> Clear the stash area

![](images/git-cmds/13-stash_clear.png)

## **git branch** & **git checkout**
> `git branch` lets you create, list, rename, and delete branches.
>
> `git checkout` command lets you navigate between the branches created by `git branch`

![](images/git-cmds/14-branch.png)

Pushing changes to a branch other than main
![](images/git-cmds/15-branch.png)

## **git merge**
> It will combine multiple sequences of commits into one unified history
>
> Used to combine two branches.

## ***git pull***
> `git pull` command first runs `git fetch` which downloads content from the specified remote repository. Then a `git merge` is executed to merge the remote content refs and heads into a new local merge commit

![](images/git-cmds/22-pull.png)

## **git rebase**
> This command is used for squashing multiple commits into a single commit

![](images/git-cmds/16-rebase.png)

![](images/git-cmds/17-rebase.png)

![](images/git-cmds/18-rebase.png)

![](images/git-cmds/19-rebase.png)

![](images/git-cmds/20-rebase.png)

# Other git concepts

## .gitignore
> Ignored files are tracked in a special file named .gitignore that is checked in at the root of your repository
>
>.gitignore files contain patterns that are matched against file names in your repository to determine whether or not they should be ignored.

## gitk
> `gitk` is a graphical history viewer. This is the tool to use when you’re trying to find something that happened in the past, or visualize your project’s history.
* [Blog](https://riptutorial.com/git/example/18336/gitk-and-git-gui)


# Git

Version control systems: Programs that keep track of changes made in a set of files. Used for:
* Tracking bugs
* Managing releases
* Collaborate with other developers

Git is a distributed version control system, there is no central server and each clone is a full first class repository.

Git was implemented as a user space content addressable file system

plumbing commands : Low level commands(creating a file)

porcelain commands : High level commands(creating a branch)

|Delta storage|Snapshot storage|
|-------------:|--------------:|
|Records only the diffs|Records entire state of the projects|
|A delta is stored|New Version of file is stored|
|Less storage usage|More storage usage|
|Slow|Better Performance|

##  Git Objects

Resides in `.git/objects` directory

### Blobs

* Represent a file
* `Hash = SHA1("blob " + filesize + '\0' + file_contents)`
* Two files with the same content will have only a single blob in the repository

### Trees
* A tree is a list of blobs or other trees.
* They are the “directories” of the git filesystem.

### Commits

* A commit is an annotated point in the history of the project along with information on how we got there.
> It contains a pointer to the tree which represents the file system at this point in
time, the name of the committer, the name of the author (both along with time
stamps), the commit message and finally, pointers to one or more parents.
A short note on the difference between the author and committer here. The
author of a commit is the person who actually made the patch associated with
the commit. The committer is the person who inserted it into the DAG. This
distinction is necessary because of gits highly distributed nature. The author
could be someone else while the committer could be the branch manager.
For the initial commit, the number of parents will be zero. For most commits
after that, it will be 1. For a merge commit, it will be more than 1.

> If blob content changes the tree content changes, which internally changes commit content

## Git Repository Elements

* The `COMMIT_EDITMSG` contains the last commit message.

* The `config` file contains the repository config. It is the default config file
updated with the `git config` command.

* The `description` file has a description of the repository and it’s purpose.
This is useful for publishing the repository.

* `HEAD` is a symbolic reference which contains the name of the current branch.

* The `hooks` directory contains scripts that are run when various operations
take place.

* The `index` is a special data structure that contains the staging area.
