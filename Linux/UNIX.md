# UNIX

## File System Hierarchy

> The root `/` directory is main directory under which all the other directories or files stay.

### Default directories

| **Directory** | **Use** |
| ----------- | ----- |
| `/bin` | Contains the essential binary files for user commands. |
| `/boot` | Files of boot loader required for booting process. |
| `/dev`| Device files. |
| `/etc`| Contains all the system specific configuration files. |
| `/home` | Contains the home directory of all regular users. |
| `/lib` | Contains shared libraries. |
| `/media` | Mount point used to mount removable media like CD, DVD etc. |
| `/mnt` | Legacy mount point used to mount removable media. |
| `/root` | Home directory of root users. |
| `/sbin` | Contains system binary files. |
| `/tmp` | Contains temporary files. Not advisable to store crusial files in this location. |
| `/var` | Contains variables files like logs, mails, etc. |

### Paths

- `Absolute path` - Path from the root directory.
```text
/home/some/file/path
``` 

- `Relative Path` - Path from the present working directory.
```text
root/Desktop
```

## `root` user

- It is the user who can manage users, can read/write any files, install or remove software, modify system configuration.
- Normal users if cannot create, read, write, delete any files unless they have proper permissions.

## Basic Commands

### `pwd` - It will print the present working directory.

### `cd` or `cd ~` - Change directory to home directory of the active user.

* `cd ..` - Go to parent directory.
* `cd /absoulte/path/to/directory` - Go to the directory **/absoulte/path/to/directory** which is absolute path.
* `cd relative/path/to/directory` - Go to the directory **relative/path/to/directory** from the current directory.
* `cd -` - Go to previous location.

### `whoami` - Displays the current username associated with the active user session.

### `man` - Gives interface to details about any commands. 

* E.g. `man pwd`. 
* Use `Page Up` and `Page Down` keys to navigate through the manual page. 
* Press `q` to exit the page.

### `ls` - For listing the contents of the directory(Files present in the directory).

* `ls -l` - For listing files with more information like size, owner, permissions,etc.
* `ls -a` - For listing all the files including hidden files.
* `ls -t` - To list the files in modified time sorted manner.

### `date` - To display system date and time.

### `cal` - To display calendar of current month.

* `cal -y` - Gives calendar of current year.
* `cal -3` - GIves calendar of previous, current and next month.

### `alias` - To display currently available aliases including the default and customized aliases.

* Also used to create an alternate name for a frquently used command.
* Alias defined in a shell session gives the desirable output during that session only.
* `alias alias_name=<command>` - E.g. `alias list='ls -l'` and then you can use the command `list` during that session.

### `unalias` - To remove any alias(system defined or user defined).

* system defined alias will be always be present in a new session but the user defined aliases will not.

### `echo` - To display any text on the terminal.

* E.g. `echo "Something ...anything ..."`

### `uname` - To display system information.

* `uname -a` - Print all information about the system.

### `clear` - To clear the contents of the terminal screen by removing previously displayed text.

### `history` - To view the list of commands you have previously executed.

### `cat` - Gives output of the input, normally a file.

* `cat fileName` - Prints the contents of the file **fileName**. 

### `who` - Displays the users that are currently logged on in the system.

## File Creation

### `touch` - To create file.

* `touch fileName` - Will create a file named **fileName** in present working directory.
* `touch file1 file2` - Will create files **file1** and **file2** in present working directory.
* `touch /path/to/file` - WIll create a file named **file** in directory **/path/to**.

### `mkdir` - To create directory.

* `mkdir dirName` - Will create a directory named **dirName** in current directory.
* `mkdir dir1 dir2` - Will create two directories named **dir1** and **dir2**.
* `mkdir grandparent/parent/child` - Will give an error if the **grandparent/parent** directory is not already present else create the **grandparent/parent/child** directory.
* `mkdir -p parent/child` - Will create the parent directory **parent** if it does not exist and then create **parent/child** directory.

## Redirection

* Standard Input Stream: Keyboard - Normally the input is given through the keyboard.
* Standard Output Stream: Terminal - Normally the output id shown on the terminal.
* Standard Error Stream: Terminal - If there's any error will be shown on the terminal.

### `<` or `0<` - Input redirection operator

* `cat < fileName` - Same as normal `cat` but here we just gave the input to `cat` command of the file **fileName**.

### `>` or `1>` - Output redirection operator

* `cat > fileName` - You need to give input to the Keyboard and it will write to file **fileName**. 
Press `ctrl + d` to close the file.
* `cat >> fileName` - To add the content to the end(append at the end)

### `2>` - Error redirection operator

* `cat someFile 2> errorFile` - If the opening the file gives error it will be redirected to the file named **errorFile**.

### `|` - Used to give output of one command to another

* `first_command | second_command` - The output of **first_command** is passed on to **second_command** to process and display the output.

## Copying and Directories

### `cp` - To copy the files from one file to a different.

* The user must have proper permissions to create the files at the destination location.
* `cp path/to/sourceFile path/to/destination` - File **sourceFile** will be copied to **path/to/destination**. The destination can be a file if **destination** is the file name or can be a directory if **destination** is a directory and the filename will be **sourceFile** itself.
* `cp file1 file2 destinationDir` - Might give an error if the **destinationDir** does not exist or will copy multiple files to the directory.
* `cp -r sourceDir path/to/destinationDir` - Contents of the directory **soruceDir** will be copied to the **path/to/destinationDir**.
* `cp` overwrites the contents of a file in the new file.

## Moving Files and Directories

### `mv` - To move files from one location to another.

* `mv file1 file2` - File **file1** is renamed to **file2**. 
* `mv file1 path/to/dir` - File **file1** is moved to directory **path/to/dir**.
* `mv file1 path/to/file2` - File **file1** is moved to directory **path/to** and renamed **file2**.
* `mv file1 file2 path/to/dir` - Files **file1** and **file2** are moved to directory **path/to/dir**.
* While moving a file to a different directory if the file with a same name already exists, you will be prompted to overwrite the file. Type *y* for yes and *n* for no.

## Removing Files and Directories

### `rm` - To remove the file.

* `rm fileName` - Will remove the file named **fileName**.
* `rm` is system alias for `rm -i` which will prompt you to comfirm before deletion.
* `rm file1 file2` - Will remove both the files **file1** and **file2**.
* `rm -f` - Will remove files without prompts.
* `rm path/to/fileName` - Will remove the file **fileName** at location **path/to**.
* `rmdir dirName` or `rm dirName` - Will remove the directory named **dirName** if it is empty.
* `rm -r dirName` - To remove all the subdirectories and files inside and delete the directory itself.

## Archiving Files and Directories

### `tar` - To archive files.

* `tar -cvf files.tar file1 file2` - Will create an file **files.tar** of files **file1** and **file2**.
* `tar -cvzf files.tar.gz file1 file2` - Will create a zipped file **files.tar.gz** of files **file1** and **file2**.
* `tar -tvf files.tar` - Will list the contents of the archive without extracting(list the files in the archive).
* `tar -tvzf files.tar` - Will list the contents of the zipped archive without extracting.
* `tar -xvf files.tar` - Will extract the contents of the archived file **files.tar**.
* `tar -xvzf files.tar.gz` - Will extract the contents of the zipped archive file **files.tar.gz**.
* `tar -rvf files.tar file1` - Will add the file **file1** to archive **files.tar**.

## Soft and Hard links

### **Soft Link** is just a pointer to the original file. 

* **Soft Link** will have a different inode number from the original file.
* Can be created for both files and directories.
* Becomes corrupted when the original file is deleted.
* `ln -s originalFile softLinkFile`

### **Hard Link** is a pointer to the contents of the original file.

* **Hard Link** will have a same inode number as of the original file.
* Can only be for created files.
* Still remians after the removal of the original file.
* `ln originalFile hardLinkFile` 

## 	Finding files

### `find` - To find the files.

* `find search/path criteria value_for_criteria` - Will search for the file based on the criteria **value_for_criteria** for the certain criteria **criteria** in the path **search/path**.
* `find . criteria value_for_criteria` - Same as mormal `find`, but will start from the current directory.
* `find search/path -name file1` - Will search for the file based on name of the file **file1**.
* `find search/path -name "n*"` - Will search for the files starting with the **n**.
* `find search/path -iname fileName` - Will search for the filename **fileName**, but will also allow the files with different alphabet case like **filename**, **FileName**, etc.
* `find search/path -type f -size +10c` - Will find the files with size larger than 10 bytes.

## Text Processing

### `more` - displays one page at a time

* `more fileName` - Displays one page of the file **fileName**.
* `(Space)` is used to move one page down.
* We can only move forward with the `more` command.

### `less` - displays one page at a time

* `less fileName` - Dislays one page of the file **fileName**.
* `PgUp` to move up and `PgDn` to move down.
* `q` to quit the command.

### `head` - To display the first part of the file

* `head fileName` - Will display 1st *ten* lines of the file **fileName**.
* `head -6 fileName` or `head -n 6 fileName` - Will dispaly 1st *six* lines of the **fileName**.

### `tail` - To display last part of the file

* `tail fileName` - Will display last *ten* lines of the file **fileName**.
* `tail -5 fileName` or `tail -n 5 fileName`- Will dispaly last *six* lines of the **fileName**.

### `cut` - To display only specific columns of the file

* `-d` is the option to divide one section from another.
* `-fNUMBER` is the option to select the column which needs to be displayed. 
* `cut -d "," -f2 fileName` - 2nd column of file **fileName** and a column is seperated by `,`.
* `cut -d "," -f2,3,4 fileName` - 2nd, 3rdand 4th columns will be displayed for the file **filename** where each column is seperated by `,`.

### `wc` - To count the lines, words and bytes of a file

* `wc fileName` - To display lines, words and bytes of a file **fileName**.
* `wc -l fileName` - To display number of lines in the file.
* `wc -w fileName` - To dispaly number of words in the file.
* `wc -c fileName` - To display number of bytes in the file.
* `wc file1 file2` - To display number of lines, words and bytes of both the files.

### `sort` - To display the contents of a file in a sorted manner

* `sort fileName` - To display the contents in alphabetical order. Not used for numbers.
* `sort -n fileName` - To display the contents in a numerical order. Only used for numbers.
* `sort -r fileName` - To display the contets in a reverse alphabetical order.
* `sort -t "delimiter" -kNUMBER fileName` - To display the contents in sorted manner based on a specific field. `-t` is used to specify the delimiter, `-kNUMBER` t specify the column number.

### `uniq` - To display unique contents

* `uniq fileName` - To display the unique contents of the file **fileName**.
* `uniq -c fileName` - To dislay the number of entries for duplicate entries.
* `uniq -u fileName` - To list only the non-repeating entries.
* `uniq -d fileName` - To list the duplicate entries only.

### `grep` - To print only those lines with the specified word

* `grep pattern fileName` - Will give the lines with the matching **pattern** from the file **fileName**.
* `-i` - For case insensitive search.
* `-w` - Entire word search.
* `-v` - Lines where the pattern is not found.
* `-n` - Line number and lines in which the pattern is found.
* `-c` - Number of lines in which pattern is found.
* `^pattern` - Lines which are starting with the **pattern**.
* `pattern$` - Lines which are ending with the **pattern**.
* `pattern *` - List all the files in which the **pattern** is found.
* `-L pattern *` - List all the files in which the **pattern** is not found.
* `^$` - Matching all the empty lines.
* `.` - Match all the lines with content.
* `\<pattern` - Words starting with the pattern.
* `pattern\>` - Words ending with the pattern.
* `-E "pattern1\|pattern2"` - Matching multiple patterns.