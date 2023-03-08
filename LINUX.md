# Linux commands

## *General*
### `cat` command

The `cat` command concatenates the contents of multiple files and displays the result on the standard output.

```bash
cat file1 [files]
```

Example 1 - Displaying the contents of a file to the standard output:

```bash
$ cat /etc/passwd
```

Example 2 - Displaying the contents of multiple files to standard output:

```bash
$ cat /etc/passwd /etc/group
```

Example 3 - Combining the contents of multiple files into one file using output redirection:

```bash
$ cat /etc/passwd /etc/group > usersAndGroups.txt
```

Example 4 - Displaying the line numbering:

```bash
$ cat -n /etc/profile
     1    # /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
     2    # and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).
     3
     4    if [ "`id -u`" -eq 0 ]; then
     5      PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
     6    else
…
```

Example 5 - Shows the numbering of non-empty lines:

```bash
$ cat -b /etc/profile
     1    # /etc/profile: system-wide .profile file for the Bourne shell (sh(1))
     2    # and Bourne compatible shells (bash(1), ksh(1), ash(1), ...).

     3    if [ "`id -u`" -eq 0 ]; then
     4      PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
     5    else
…
```

### `cd` command

The `cd` (Change Directory) command allows you to change the current directory -- in other words, to move through the tree.

```bash
$ cd /tmp
$ pwd
/tmp
$ cd ../
$ pwd
/
$ cd
$ pwd
/home/rockstar
```

As you can see in the last example above, the command `cd` with no arguments moves the current directory to the `home directory`.


### `clear` command

The `clear` command clears the contents of the terminal screen. More accurately, it shifts the display so that the command prompt is at the top of the screen on the first line.

On a physical terminal, the display will be permanently hidden, whereas in a graphical interface, a scrollbar will allow you to go back in the history of the virtual terminal.

### `cp` command

The `cp` command copies a file.

```bash
cp file [file ...] destination
```

Example:

```bash
$ cp -r /home/rockstar /tmp
```

| Options | Information                                                      |
| ------- | ---------------------------------------------------------------- |
| `-i`    | Request confirmation if overwriting (default).                   |
| `-f`    | Do not ask for confirmation if overwriting the destination file. |
| `-p`    | Keeps the owner, permissions and timestamp of the copied file.   |
| `-r`    | Copies a directory with its files and subdirectories.            |
| `-s`    | Creates a symbolic link rather than copying.                    |

```bash
cp file1 /repexist/file2
```

`file1` is copied to `/repexist` under the name `file2`.

```bash
$ cp file1 file2
```

`file1` is copied as `file2` to this directory.

```bash
$ cp file1 /repexist
```

If the destination directory exists, `file1` is copied to `/repexist`.

```bash
$ cp file1 /wrongrep
```

If the destination directory does not exist, `file1` is copied under the name `wrongrep` to the root directory.

### `mv` command

The `mv` command moves and renames a file.

```bash
mv file [file ...] destination
```

Examples:

```bash
$ mv /home/rockstar/file1 /home/rockstar/file2
$ mv /home/rockstar/file1 /home/rockstar/file2 /tmp
```

| Options                                                                        | Information                                                     |
| ------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| `-f`                                                                           | Don't ask for confirmation if overwriting the destination file. |
| `-i`                                                                           | Request confirmation if overwriting destination file (default). |

A few concrete cases will help you understand the difficulties that can arise:

```bash
$ mv /home/rockstar/file1 /home/rockstar/file2
```

Renames `file1` to `file2`. If `file2` already exists, replace the contents of the file with `file1`.

```bash
$ mv /home/rockstar/file1 /home/rockstar/file2 /tmp
```

Moves `file1` and `file2` into the `/tmp` directory.

```bash
$ mv file1 /repexist/file2
```

Moves `file1` into `repexist` and renames it `file2`.

```bash
$ mv file1 file2
```

`file1` is renamed to `file2`.

```bash
$ mv file1 /repexist
```

If the destination directory exists, `file1` is moved to `/repexist`.

```bash
$ mv file1 /wrongrep
```

If the destination directory does not exist, `file1` is renamed to `wrongrep` in the root directory.


### `rm` command

The `rm` command deletes a file or directory.

```bash
rm [-f] [-r] file [file] [...]
```

!!! Danger

    Any deletion of a file or directory is final.

| Options | Information                              |
| ------- | ---------------------------------------- |
| `-f`    | Do not ask whether to delete. |
| `-i`    | Ask whether to delete.       |
| `-r`    | Delete a directory and recursively delete its subdirectories.      |

!!! Note

    The `rm` command itself does not ask for confirmation when deleting files. However, with a Red Hat/Rocky distribution, `rm` does ask for confirmation of deletion because the `rm` command is an `alias` of the `rm -i` command. Don't be surprised if on another distribution, like Debian for example, you don't get a confirmation request.

Deleting a folder with the `rm` command, whether the folder is empty or not, will require the `-r` option to be added.

The end of the options is signaled to the shell by a double dash `--`.

In the example:

```bash
$ >-hard-hard # To create an empty file called -hard-hard
hard-hard
[CTRL+C] To interrupt the creation of the file
$ rm -f -- -hard-hard
```

The hard-hard file name starts with a `-`. Without the use of the `--` the shell would have interpreted the `-d` in `-hard-hard` as an option.


### `history` command

The `history` command displays the history of commands that have been entered by the user.

The commands are stored in the `.bash_history` file in the user's login directory.

Example of a history command

```bash
$ history
147 man ls
148 man history
```

| Options | Comments                                                                                                           |
| ------- | ------------------------------------------------------------------------------------------------------------------ |
| `-w`    | Writes the current history to the history file.                                                |
| `-c`    | Deletes the history of the current session (but not the contents of the `.bash_history` file). |

* Manipulating history:

To manipulate the history, the following commands entered from the command prompt will:

| Keys               | Function                                                  |
| ------------------ | --------------------------------------------------------- |
| <kdb>!!</kdb>      | Recalls the last command placed.                           |
| <kdb>!n</kdb>      | Recalls the command by its number in the list.             |
| <kdb>!string</kdb> | Recalls the most recent command beginning with the string. |
| <kdb>↑</kdb>       | Navigates through your history working backward in time from the most recent command. |
| <kdb>↓</kdb>       | Navigates through your history working forward in time. |

### `ls` command

The `ls` command displays the contents of a directory.

```bash
ls [-a] [-i] [-l] [directory1] [directory2] […]
```

Example:

```bash
$ ls /home
.    ..    rockstar
```

The main options of the `ls` command are:

| Option                                                       | Information                                                                                                                          |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| `-a`                                                         | Displays all files, even hidden ones. Hidden files in Linux are those beginning with `.`.                                            |
| `-i`                                                         | Displays inode numbers.                                                                                                              |
| `-l`                                                         | Use a long listing format, that is, each line displays long format information for a file or directory.                                 |

The `ls` command, however, has a lot of options (see `man`):

| Option                                                       | Information                                                                                                                          |
| ------                                                       | ------------                                                                                                                         |
| `-d`                                                         | Displays information about a directory instead of listing its contents.                                                              |
| `-g`                                                         | Like -l option, but do not list owner.                                                                                               |
| `-h`                                                         | Displays file sizes in the most appropriate format (byte, kilobyte, megabyte, gigabyte, ...). `h` stands for Human Readable. Needs to be used with -l option.         |
| `-s`                                                         | Displays the allocated size of each file, in blocks. In the GNU/Linux operating system, "block" is the smallest unit of storage in the file system, one block equals 4096Byte. |
| `-A`                                                         | Displays all files in the directory except `.` and `..`                                                                              |
| `-R`                                                         | Displays the contents of subdirectories recursively.                                                                                 |
| `-F`                                                         | Displays the type of files. Prints a `/` for a directory, `*` for executables, `@` for a symbolic link, and nothing for a text file. |
| `-X`                                                         | Sorts files according to their extensions.                                                                                           |

* Description of columns generated by running the `ls -lia` command:

```bash
$ ls -lia /home
78489 drwx------ 4 rockstar rockstar 4096 25 oct. 08:10 rockstar
```

| Value           | Information                                                                                                   |
| --------------- | ------------------------------------------------------------------------------------------------------------- |
| `78489`         | Inode Number.                                                                                                 |
| `drwx------`    | File type (`d`) and rights (`rwx------`).                                                                     |
| `4`             | Number of subdirectories (`.` and `..` included). For a file, it represents the number of hard links, and 1 represents itself. |
| `rockstar`      | User ownership.                                                                                               |
| `rockstar`      | Group ownership.                                                                                              |
| `4096`          | For files, it shows the size of the file. For directories, it shows the fixed value of 4096 bytes occupied by the file naming. To calculate the total size of a directory, use `du -sh rockstar/` |
| `25 oct. 08:10` | Last modified date.                                                                                           |
| `rockstar`      | The name of the file (or directory).                                                                          |

!!! Note

    **Aliases** are frequently positioned in common distributions.

    This is the case of the alias `ll`:

    ```
    alias ll='ls -l --color=auto'
    ```

The `ls` command has many options. Here are some advanced examples of uses:

* List the files in `/etc` in order of last modification:

```bash
$ ls -ltr /etc
total 1332
-rw-r--r--.  1 root root    662 29 may   2021 logrotate.conf
-rw-r--r--.  1 root root    272 17 may.   2021 mailcap
-rw-------.  1 root root    122 12 may.  2021 securetty
...
-rw-r--r--.  2 root root     85 18 may.  17:04 resolv.conf
-rw-r--r--.  1 root root     44 18 may.  17:04 adjtime
-rw-r--r--.  1 root root    283 18 may.  17:05 mtab
```

* List `/var` files larger than 1 megabyte but less than 1 gigabyte. The example here uses advanced `grep` commands with regular expressions. Novices don't have to struggle too much, there will be a special tutorial to introduce these regular expressions in the future.

```bash
$ ls -lhR /var/ | grep ^\- | grep -E "[1-9]*\.[0-9]*M" 
...
-rw-r--r--. 1 apache apache 1.2M 10 may.  13:02 XB RiyazBdIt.ttf
-rw-r--r--. 1 apache apache 1.2M 10 may.  13:02 XB RiyazBd.ttf
-rw-r--r--. 1 apache apache 1.1M 10 may.  13:02 XB RiyazIt.ttf
...
```

Of course, we highly recommend that you use the `find` command.

```bash
$ find /var -size +1M -a -size -1024M  -a -type f  -exec ls -lh {} \;
```

* Show the rights on a folder:

To find out the rights to a folder, in our example `/etc`, the following command would **not** be appropriate:

```bash
$ ls -l /etc
total 1332
-rw-r--r--.  1 root root     44 18 nov.  17:04 adjtime
-rw-r--r--.  1 root root   1512 12 janv.  2010 aliases
-rw-r--r--.  1 root root  12288 17 nov.  17:41 aliases.db
drwxr-xr-x.  2 root root   4096 17 nov.  17:48 alternatives
...
```

The above command will display the contents of the folder (inside) by default. For the folder itself, you can use the `-d` option.

```bash
$ ls -ld /etc
drwxr-xr-x. 69 root root 4096 18 nov.  17:05 /etc
```

* Sort by file size, largest first:

```bash
$ ls -lhS
```

* time/date format with `-l`:

```bash
$ ls -l --time-style="+%Y-%m-%d %m-%d %H:%M" /
total 12378
dr-xr-xr-x. 2 root root 4096 2014-11-23 11-23 03:13 bin
dr-xr-xr-x. 5 root root 1024 2014-11-23 11-23 05:29 boot
```

* Add the _trailing slash_ to the end of folders:

By default, the `ls` command does not display the last slash of a folder.
In some cases, like for scripts for example, it is useful to display them:

```bash
$ ls -dF /etc
/etc/
```

* Hide some extensions:

```bash
$ ls /etc --hide=*.conf
```

### `man` command

Once found by `apropos` or `whatis`, the manual is read by `man` ("Man is your friend").
This set of manuals is divided into 8 sections, grouping information by topic, the default section being 1:

1. Executable programs or commands.
2. System calls (functions given by the kernel).
3. Library calls (functions given by the library).
4. Special files (usually found in /dev).
5. File Formats and conventions (configuration files such as etc/passwd).
6. Games (such as character-based applications).
7. Miscellaneous (e.g. man (7)).
8. System administration commands (usually only for root).
9. Kernel routines (non-standard).

Information about each section can be accessed by typing `man x intro`, where `x` is the section number.

The command:

```bash
man passwd
```

will tell the administrator about the passwd command, its options, etc. While a:

```bash
$ man 5 passwd
```

will inform him about the files related to the command.

Navigate through the manual with the arrows <kbd>↑</kbd> and <kbd>↓</kbd>. Exit the manual by pressing the <kbd>q</kbd> key.

### `mkdir` command

The `mkdir` command creates a directory or directory tree.

```bash
mkdir [-p] directory [directory] [...]
```

Example:

```bash
$ mkdir /home/rockstar/work
```

The "rockstar" directory must exist to create the "work" directory.

Otherwise, the `-p` option should be used. The `-p` option creates the parent directories if they do not exist.

!!! Danger

    It is not recommended to use Linux command names as directory or file names.

### **dir**

### `find` command
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

### `date` command

The `date` command displays the date and time. The command has the following syntax:

```bash
date [-d AAAAMMJJ] [format]
```

Examples:

```bash
$ date
Mon May 24 16:46:53 CEST 2021
$ date -d 20210517 +%j
137
```

In this last example, the `-d` option displays a given date. The `+%j` option formats this date to show only the day of the year.

!!! Warning

    The format of a date can change depending on the value of the language defined in the environment variable `$LANG`.

The date display can follow the following formats:

| Option  | Format                                                    |
| --------| --------------------------------------------------------- |
| `+%A`   | Locale's full weekday name (e.g., Sunday)                 |
| `+%B`   | Locale's full month name (e.g., January)                  |
| `+%c`   | Locale's date and time (e.g., Thu Mar  3 23:05:25 2005)   |
| `+%d`   | Day of month (e.g., 01)                                   |
| `+%F`   | Date in `YYYY-MM-DD` format                               |
| `+%G`   | Year                                                      |
| `+%H`   | Hour (00..23)                                             |
| `+%j`   | Day of the year (001..366)                                |
| `+%m`   | Month number (01..12)                                     |
| `+%M`   | Minute  (00..59)                                          |
| `+%R`   | Time in `hh:mm` format                                    |
| `+%s`   | Seconds since January 1, 1970                             |
| `+%S`   | Second (00..60)                                           |
| `+%T`   | Time in `hh:mm:ss` format                                 |
| `+%u`   | Day of the week (`1` for Monday)                          |
| `+%V`   | Week number (`+%V`)                                       |
| `+%x`   | Date in format `DD/MM/YYYY`                               |

The `date` command also allows you to change the system date and time. In this case, the `-s` option will be used.

```bash
date -s "2021-05-24 10:19"
```

The format to be used following the `-s` option is this:

```bash
date -s "[AA]AA-MM-JJ hh:mm:[ss]"
```

### `touch` command

The `touch` command changes the timestamp of a file or creates an empty file if the file does not exist.

```bash
touch [-t date] file
```

Example:

```bash
$ touch /home/rockstar/myfile
```

| Option                            | Information                                                                |
| --------------------------------- | -------------------------------------------------------------------------- |
| `-t date`                         | Changes the date of last modification of the file with the specified date. |

Date format: `[AAAA]MMJJhhmm[ss]`

!!! Tip

    The `touch` command is primarily used to create an empty file, but it can be useful for incremental or differential backups for example. Indeed, the only effect of executing a `touch` on a file will be to force it to be saved during the next backup.

### **export**

The `export` command is used to export variables to child processes.

```
export TEST="test"
```

```
export PATH=$PATH:/new/path
```

### `shutdown` command

The `shutdown` command allows you to **electronically shut down** a Linux server, either immediately or after a certain period of time.

```bash
shutdown [-h] [-r] time [message]
```

Specify the shutdown time in the format `hh:mm` for a precise time, or `+mm` for a delay in minutes.

To force an immediate stop, use the word `now` in place of the time. In this case, the optional message is not sent to other users of the system.

Examples:

```bash
shutdown -h 0:30 "Server shutdown at 0:30"
shutdown -r +5
```

Options:

| Options | Remarks                          |
| ------- | -------------------------------- |
| `-h`    | Shuts down the system electronically. |
| `-r`    | Restarts the system.              |


## **Text manipulation**
### `cut` command
The `cut` command lets you remove sections from each line of files. Print selected parts of lines from each FILE to standard output. With no FILE, or when FILE is -, read standard input.

1. Selecting specific fields in a file
```
cut -d "delimiter" -f (field number) file.txt
```

2. Selecting specific characters:
```
cut -c [(k)-(n)/(k),(n)/(n)] filename
```
Here, **k** denotes the starting position of the character and **n** denotes the ending position of the character in each line, if _k_ and _n_ are separated by “-” otherwise they are only the position of character in each line from the file taken as an input.

3. Selecting specific bytes:
```
cut -b 1,2,3 filename 			//select bytes 1,2 and 3
cut -b 1-4 filename				//select bytes 1 through 4
cut -b 1- filename				//select bytes 1 through the end of file
cut -b -4 filename				//select bytes from the beginning till the 4th byte
```
**Tabs and backspaces** are treated like as a character of 1 byte.

```
cut OPTION... [FILE]...
```

#### Additional Flags and their Functionalities:

|**Short Flag**   |**Long Flag**   |**Description**   |
|:---|:---|:---|
|`-b`|`--bytes=LIST`|select only these bytes|
|`-c`|`--characters=LIST`|select only these characters|
|`-d`|`--delimiter=DELIM`|use DELIM instead of TAB for field delimiter|
|`-f`|`--fields`|select only these fields;  also print any line that contains no delimiter character, unless the -s option is specified|
|`-s`|`--only-delimited`|do not print lines not containing delimiters|
|`-z`|`--zero-terminated`|line delimiter is NUL, not newline|


### `echo` command

The `echo` command is used to display a string of characters.

This command is most commonly used in administration scripts to inform the user during execution.

The `-n` option indicates no newline output string (by default, newline output string).

```bash
shell > echo -n "123";echo "456"
123456

shell > echo "123";echo "456"
123
456
```

For various reasons, the script developer may need to use special sequences (starting with a `\` character). In this case, the `-e` option will be stipulated, allowing interpretation of the sequences.

Among the frequently used sequences, we can mention:

| Sequence | Result                |
| -------- | --------------------- |
| `\a`     | Sends a sonar beep      |
| `\b`     | Back                  |
| `\n`     | Adds a line break     |
| `\t`     | Adds a horizontal tab |
| `\v`     | Adds a vertical tab     |


### `grep` command

The `grep` command searches for a string in a file.

```bash
grep [-w] [-i] [-v] "string" file
```

Example:

```bash
$ grep -w "root:" /etc/passwd
root:x:0:0:root:/root:/bin/bash
```

| Option                                                                                  | Description                             |
| --------------------------------------------------------------------------------------- | --------------------------------------- |
| `-i`                                                                                    | Ignores the case of the searched string. |
| `-v`                                                                                    | Excludes lines containing the string.   |
| `-w`                                                                                    | Searches for the exact word.              |

The `grep` command returns the complete line containing the string you are looking for.
* The `^` special character is used to search for a string at the beginning of a line.
* The special character `$` searches for a string at the end of a line.

```bash
$ grep -w "^root" /etc/passwd
```

It is possible to search for a string in a file tree with the `-R` option.

```bash
grep -R "Virtual" /etc/httpd
```

### `head` command

The `head` command displays the beginning of a file.

```bash
head [-n x] file
```

| Option                                                                                                | Description                            |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------- |
| `-n x`                                                                                                | Display the first `x` lines of the file |

By default (without the `-n` option), the `head` command will display the first 10 lines of the file.

### `tail` command

The `tail` command displays the end of a file.

```bash
tail [-f] [-n x] file
```

| Option   | Description                             |
| -------- | ----------------------------------------- |
| `-n x`   | Displays the last `x` lines of the file   |
| `-f`     | Displays changes to the file in real time |

Example:

```bash
tail -n 3 /etc/passwd
sshd:x:74:74:Privilege-separeted sshd:/var/empty /sshd:/sbin/nologin
tcpdump::x:72:72::/:/sbin/nologin
user1:x:500:500:grp1:/home/user1:/bin/bash
```

With the `-f` option, the change information of the file will always be output unless the user exits the monitoring state with <kbd>CTRL</kbd> + <kbd>C</kbd>. This option is very frequently used to track log files (the logs) in real time.

Without the `-n` option, the `tail` command displays the last 10 lines of the file.


## **sysadmin**
### **passwd**

### **adduser**

### **addgroup**

### **deluser**

### **delgroup**

### **chmod**

### **chown**

### **ps**

### **uname**

### **which**

### **ln**

Hard Links : Can't link to directories, and can't link to external filesystems
```
ln <original> <link>
```

Soft Links : Can link to other filesystems and to directories, but when the original is removed, the link will be broken
```
ln -s <original> <link>
```

### **crontab**

```
crontab -l
```
list cron jobs

```
crontab -e
```
To edit cron jobs

* To generate cronjob commands use [this](https://crontab-generator.org/).

## *Networking*
### **ssh**

### **scp**

### **rsync**
