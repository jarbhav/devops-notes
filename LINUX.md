# Linux commands

## **find**

Examples:
```
find . -name '*js'
```
Find all the files under the current tree that have the .js extension and print the relative path of each file matching

```
find . -type d -name src
```
Find directories under the current tree matching the name "src"

```
find folder1 folder2 -name filename.txt
```
Search under multiple root trees

```
find . -type f -size +100k -size -1M
```
Search files bigger than 100KB but smaller than 1MB

```
find . -type f -mtime +3
```
Search files edited more than 3 days ago

```
find . -type f -exec cat {} \;
```
Execute a command on each result of the search. In this example we run cat to print the file content notice the terminating \\; . The {} is filled with the file name at execution time.

## **ln**

Hard Links : Can't link to directories, and can't link to external filesystems
```
ln <original> <link>
```

Soft Links : Can link to other filesystems and to directories, but when the original is removed, the link will be broken
```
ln -s <original> <link>
```

## **crontab**

```
crontab -l
```
list cron jobs

```
crontab -e
```
To edit cron jobs

* To generate cronjob commands use [this](https://crontab-generator.org/).


## **export**

The `export` command is used to export variables to child processes.

```
export TEST="test"
```

```
export PATH=$PATH:/new/path
```