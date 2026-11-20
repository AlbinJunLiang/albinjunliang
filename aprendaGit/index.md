# Git Note and annotations 

- https://www.youtube.com/watch?v=UJGKWMHX038&list=PLTd5ehIj0goMCnj6V5NdzSIHBgrIXckGU&index=3


[1 - If a initialize a repository locally before creating it on github, what should i do?](1-init%20repository.ipynb)


[2 -  How to clone a remote repository from github.](2-clone%20repository.ipynb)


[3 - What do i have to do if someone make a change in a remote repository and i want to get the changes?](3-pull.ipynb)


[4 - If i want to know what branch i am working?](#git-status)

[5 - Changes not staged for commit](#git-status)


[6 - Verify that the files are ready to be committed.](#git-status)

[7 - View commits history.](#git-log)

[8 - View  changes after the last commit.](#git-log)


[9 - Modify the last commit.](#modify-and-add-changes-the-last-commit)


[10 - Undo a change or modification (deshacer)](#undo-a-change)


[11 - Remove a add . or remove changes after make a add .](#git-reset)

[12 - Remove a commit from the stage](#git-reset)

[13 -  Go to specific commit and wath the phisical files](#git-checkout)

[14 - Revert a commit](#git-revert)

[15 - branch](#git-branch)

[16 - Merge branches](#git-merge)

[17 - Make or delete config alias](#git-config)

[18 - Git tag](#git-tag)

[19 -  Save changes temporary without commit](#git-stash)


[20 - Restore changes in specific point](#git-restore)

[21 - command used to search for code for matching](#git-grep)

[22 - Exclude files in the stage](#git-ignore)

[23 - Check which files to add](#git-add)


[24 - Patch in files](#git-apply)













### Git status


```
git status
```


### Git log

press **q** to exit.

```
git log

# Watch results in one line

git log --oneline

# Watch commit from all branches
git log --oneline --decorate --all

# Graph
git log --oneline --decorate --all --graph
```



### Git diff

```
git diff

# unlike between two branches

git diff <BRANCH1>...<BRANCH2>

# resume with files
git diff <BRANCH1>...<BRANCH2> --stat

```

### Modify and add changes the last commit

```
 git commit --amend -m "feat: añadir validación al formulario de registro"
```


## git checkout
```
# Go to specific commit and wath the phisical files

git checkout <HASH>

# Go back o undo 

git checkout <BRANCH NAME (master or main)>
```


## Undo a change

Only works before to do git add .
```
 git checkout .

 # for a single file

 git checkout -- index.html
```

## Git reset

You should make git checkout . after make git reset for restart the changes
```
 git reset HEAD index.html

  # Remove a commit from only the stage
 git reset i9j0k1l
 
 # Remove a commit from the stage and the physicals files
 git reset --hard i9j0k1l


```

## Git revert

```
git revert 7a3b5c1

# Without having to create a new commit
git revert -n 7a3b5c1

```



## Git branch

```
# Check my currently branch
git branch

# Create a new brach
git branch <NEW-BRANCH>

# Switch a branch

git checkout <NEW-BRANCH>

# Create a change a branch

git checkout -b <NEW-BRANCH>


# Rename a branch name

git branch -m <NEW-NAME> <NAME>

# Delete a branch

git branch -d <NAME>


```


## Git merge

```
git merge <RAMA_A_MEZCLAR>

# Undo merge only in conflicts

git merge --abort

```


## Git config

```
git config --global alias.<ALIAS_NAME> 'ALIAS COMMAND'

# Example 
ALBIN@mxlinux-albin:~/Documentos/albinstack/aprendaGit
$ git config --global alias.lodag 'log --oneline --decorate --all --graph'
ALBIN@mxlinux-albin:~/Documentos/albinstack/aprendaGit
$ git lodag

Remove or delete a alias

```

Remove or delete a alias

```
git config --global --unset alias.<ALIAS_NAME>

```




## Git tag

```

# Light tag (Ligero)
git tag <VERSION_NAME>

# Create a tag in a specific commit

git tag <VERSION_NAME> <COMMIT_HASH>

# You can swich by tag instead of commit hash

git checkout <VERSION_NAME>

# Show all the tags i have created

git tag


# delete a tag

git tag -d

# tag annotated (Anotado)

git tag -a <VERSION_NAME> <COMMIT_HASH>


# Check tag info
git show <VERSION_NAME>

```

## Git stash

- Hide changes temporary

Cambiar de rama de emergencia: Si estás mitad de una tarea y te piden corregir un error urgente en otra rama, puedes guardar tu avance con git stash, cambiar de rama, resolver el problema y luego volve

```
git stash

# List the stashes

git list stash

# Redo the changes from the stage

git stash apply

# Remove the last stages at the stack

git stash drop

# Save stage with description (OPTIONAL)

git stash save "<DESCRIPTION>"

# Apply the changes in a specific stash

git stash apply stash@{n}

```

## git restore

```
# Restore all the changes before make a add,
git restore .

# Restore even when you make add then .
git restore --staged --worktree <FILE>
git restore --staged --worktree .


# Restore in a specific TAG

git restore --source=<TAG_VERSION> <FILE_ROOT>

```

## git grep

```
git grep <CODE>

# Find in a specific folder

git grep <CODE> -- <FOLDER>

# Ignore uppercase
git grep -i <CODE>


# Ignore uppercase and only the whole word
git grep -iw <CODE>

# Specify the line
git grep -n <CODE>
```


## git ignore

```
# Drop a file in a stage after a add .
git rm --cached <FILE> 


```



## git add
 sirve para agregar fragmentos específicos de tus cambios al área de preparación (staging area), en lugar de incluir todo el archivo de golpe.

 Does not work in new files
```
# Check files to add

git add --patch
```


## git apply

El comando git apply sirve para aplicar un archivo de parche (generalmente con extensión .patch o .diff) directamente sobre los archivos de tu repositorio local, sin crear un commit ni modificar el historial

https://www.youtube.com/watch?v=mMRDe60mjD8

**Fist you have to crate a patchfile**

```
git diff > file.patch
```




```
# Restore changes from a batch o file

git apply <FILE_CONTENT>

```
