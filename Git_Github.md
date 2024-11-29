# Git

- It is used for version control locally.

## Commands

### `git init`

- This command will begin the usage of git locally.
- It will create a hidden directory named `.git` in current location.

### `git status`

- This command is used to know the current status of the repository like what are the new changes, are those added, commited, etc,.
  
### `git add`

- This command is used to add the files that you want to commit to repository.
- Files can be added individually or all the files that were changed.

#### Example:

-> To add all the files that were modified.
```
git add .
```

-> To add the individual file.
```
git add fileName
```

### `git commit`

- It is used to commit the files to the repository.

#### Example

-> We need to use the `-m` option to pass the message. 

```
git commit -m "The message"
```

### `git restore`

- This command can used when you want to remove the files that were added.

#### Example

-> We need to specify the files which is added and is now needed to be removed using option `--staged`

```
git restore --staged fileName
```

### `git log`

- This command is used to check the entire history of all the commits.

#### Example

```
git log
```

### `git reset`

- This commad is used to move to the previous commit.

#### Example

-> If you have made some changes which got you into trouble and now you want to move back to a commit where everything was good.

-> We can check the exact hash of the commit using `git log` and the same you can use with this command.

-> In below example, replace the __HASH__ with the exact hash value.

```
git reset HASH
```

### `git stash`

-> This command can be used when you have made the changes and currently do not want to commit to those changes, but still want them to be there whenever needed.

#### Example

```
git stash
```

-> If you want to bring back the things saved in the _stash_ then you can use `pop` option.

-> This bring the changes back to the unstaged.

```
git stash pop
```

-> If you want to remove the changes completely that you stashed, then you can use the `clear` option.

-> Thi will remove the changes from the unstaged and you will never be able to bring them back.

```
git stash clear
```

### `git remote`

- This command can be used when you want to connect the local repository to the one on the Github.
- For this first you need to create a repository on the Github

#### Example

-> In below example the __URL__ is the url to your git repository.

```
git remote add URL
```





