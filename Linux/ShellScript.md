# Shell Script

## Visual Editor

* One of the popular editor is **VIsual editor**
* Type `vi fileName` to create andopen the file to edit it.
* There are three modes in VI:
	* **Command mode** - By default, the VI opens in command mode.
	* **Insert mode** - To start editing the file press `i`
      * To switch back to Command mode use `Esc`.
    * **Escape mode** - To save or quit the file, you should be in this mode.
      * Press `:` once you are in command mode to enter escape mode.

### Move in the editor

| **Command** | **Description** |
| ----------- | --------------- |
| `h` | Move the cursor one character to the left |
| `l` | Move the cursor one character to the right |
| `k` | Move the cursor one line up |
| `j` | Move the cursor one line down |

### Inserting data

| **Command** | **Description** |
| ----------- | --------------- |
| `i` | Inserts data before current cursor location |
| `I` | Inserts data at the beginning of the line |
| `o` | Inserts data in the new line below the current line |
| `O` | Inserts data in the new line above the current line |
| `a` | Inserts data after the current cursor location |
| `A` | Inserts data at the end of the current line |

### Deleting data

| **Command** | **Description** |
| ----------- | --------------- |
| `dw` | Deletes the characters from current cursor till the end of the word |
| `dd` | Deletes the entire line where the cursor is present |
| `ndd` | Deletes *n* lines from the line where cursor is present |
| `D` | Deletes from the cursor location till the end of the line |
| `d^` | Deletes from the current cursor position to the beginning of the line |
| `d$` | Deletes from the current cursor position to the end of the line |

### Copying and Pasting

| **Command** | **Description** |
| ----------- | --------------- |
| `yy` | Copies the current line where the cursor is present |
| `yw` | Copies the current word where the cursor is present till the end of the word |
| `p` | Pastes the copied data after the cursor |
| `P` | Pastes the copied data before the cursor |

### Saving and Quiting

| **Command** | **Description** |
| ----------- | --------------- |
| `:wq` | Save and quit the file |
| `:w` | Just save the file |
| `:q` | Lets you quit the file if no changes has been made to the file |
| `:q!` | Lets you quit the file without saving the made changes |

## Variables

* Variable is a string of character to which a value can be assigned.
* Once a value is assigned to a variable in UNIX, the variable can be accessed by prefixing the variable with dollar sign(*$*).
* Variable name must start with alphabet(*a-z*, *A-Z*) or underscore(*_*). 
* Variable name cannot start with a number(*0-9*).
* Variable name may contain alphabets(*a-z*, *A-Z*), numbers(*0-9*) and special character *_*.

### Predefined variables

| **Variables** | **Description** |
| ------------- | --------------- |
| `$SHELL` | The path to the shell being used |
| `$UID` | The user ID of the current user |
| `$USER` | The current user's name |
| `$HOSTNAME` | The hostname of the system |
| `$HOME` | The user's home directory |

### Defining and Accessing a variable

* `variable_name=value` is the way to define the variable in shell script.
* `$variable_name` is the way to access the defined variable.
* `readonly variable_name=value` is a way to define readonly variables.
* `read variable_name` is the command to take the user input from terminal and save it in the shell variable.
* `read -p "some prompt" variable_name` - To read the variable **varaible_name** and user will be prompted with prompt **some prompt**.

### Special variables

| **Variable** | **Description** |
| ------------ | --------------- |
| `$?` | Exit status of the previous command |
| `$0` | Shell name or the current program name |
| `$#` | Total number of positional arguments |
| `$*` | Displays all the positional arguments |
| `$@` | Displays all the positional arguments |
| `$$` | Process ID of the current process |

## Positional Arguments

* To run a shell scirpt program use command:
```bash
sh script.sh arg1 arg2 arg3
```

* `$1` if present in the above **script.sh** file would give *arg1*.
* `$2` if present in the above **script.sh** file would give *arg2*.
* `$#` if present in the above **script.sh** file would give *3*.
* `$@` will store the arguments as different strings.
* `$*` will store the arguments as a single string.

## Command Substitution

```bash
current_directory=`pwd`
echo $current_directory
```
* The output will give the current working directory.

## Operators

* If the exit status of the program is *0* means the expression eavluated to *False*.
* If the exit status of the program is *1* means the expression eavluated to *True*.

### Integer comparision operators

| **Operator** | **Meaning** | **Usage** |
| ----------- | ----------- | --------- |
| `-eq` | equal to | `[$a -eq $b]` |
| `ne` | not equal to | `[$a -ne $b]` |
| `-gt` | greater than | `[$a -gt $b]` |
| `-ge` | greater than or equal to | `[$a -ge $b]` |
| `-lt` | less than | `[$a -lt $b]` |
| `-le` | less than or equal to | `[$a -le $b]` |

### String comparision operators

| **Operator** | **Meaning** | **Usage** |
| ----------- | ----------- | --------- |
| `==` | equal to | `["$a" == "$b"]` |
| `!=` | not equal to | `["$a" != "$b"]` |
| `-n` | not a null string | `[-n "$a"]` |
| `-z` | null string | `[-z "$a"]` |

### File operators

| **Operator** | **True if** |
| ------------ | ----------- |
| `[-a file]` | file exists |
| `[-f file]` | file exists and is a regular file |
| `[-d file]` | file exists and is a directory |
| `[-r file]` | file is readable by the current user |
| `[-w file]` | file is writable by the current user |
| `[-x file]` | file is executable by the current user |
| `[-s file]` | file exists and is non-empty |

> `test some_expression` is used to evaluate an expression.

## Selection constructs

### If else blocks

```bash
if [some_expression]
then
# some statements
elif [other_expression]
then
# other statements
else
# default statements
fi
```

### Case block

```bash
case $variable in
choice1) # block of commands;;
choice2) # other block of commands;;
.
.
*) # default block of commands # this should only be placed at last or will get evaluated.
esac
```

## Iterative constructs

### For loop

* Repeat the execution of the of code for definite number of iterations.

```bash
for var in argument_list
do
# some block of statements repeated for all the value in the argument_list
done
```

#### Example 1

```bash
for lang in Python Java Javascript
do
echo "$lang is a programming Language"
done
```

#### Output

```
Python is a programming Language
Java is a programming Language
Javascript is a programming Language
```

#### Example 2

```bash
for i in file{1..3}
do
echo ${i}
done
```

#### Output

```
file1
file2
file3
```

### While loop

* Repeat the execution of the section as long as the expression is true.

```bash
while expression
do
# block of commands
done
```

#### Example:

```bash
echo "Enter the value of n"
read n
echo "The numbers are"
x=1
while [ $x -le $n ]
do
echo $x
x=`expr $x + 1`
done
```

#### Output:

```
1
2
3
4
5
```

### Until loop

* Executes a block of commands as long as a specified condition remains false.

```bash
until condition
do
# block of commands
done
```

#### Example:

```bash
num=5
until [ $num -gt 10 ]
do
echo $num
num = `expr $num + 1`
done
```

#### Output:

```
5
6
7
8
9
10
```

* `break` is used to when you want to terminate the loop if that condition is met.
* `continue` is used when you want to want to continue the execution of the loop from next iteration.

