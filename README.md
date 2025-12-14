# Todo CLI

A lightweight command-line Todo manager built with *Typer* and *Rich*

## Features

- Add, delete, update, complete todos
- Categorize tasks
- Colorful table display with Rich

## PyPI Badge
[![PyPI](https://img.shields.io/pypi/v/omar1324-todo-cli)](https://pypi.org/project/omar1324-todo-cli/)


## How to use it 

1-install python >=3.9 https://www.python.org/downloads/

2- open your terminal and run this 
[![Install via pip](https://img.shields.io/badge/pip-install-brightgreen)](https://pypi.org/project/omar1324-todo-cli/)


```bash
pip install omar1324-todo-cli

```

3- After installation, you should see something like this:
```bash
Successfully installed omar1324-todo-cli-1.1.2

```
----

## commands :

1- (show) : Display your todo-list in a table:
```bash
todo show
```
2- (add)
```bash
todo add "name of your task" "category"

```

for category ther is 4 coloured category :
- sports ->  green 
- youtube -> red 
- learn -> blue 
- study -> purple 
- anything else -> white

Example 1

```bash
todo add "task1" "sports"

```

![Screenshot](https://raw.githubusercontent.com/Omarabdalgwad/Todo-list-cli/main/assets/Screenshot%202025-11-25%20151858.png)

Example 2

```bash
todo add "task2" "youtube"

```

![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20151940.png)


Example 3

```bash
todo add "task3" "learn"

```

![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152107.png)


Example 4

```bash
todo add "task4" "study"

```

![Screenshot](![Screenshot](https://raw.githubusercontent.com/Omarabdalgwad/Todo-list-cli/main/assets/Screenshot%202025-11-25%20151858.png))


Example 5
```bash
todo add "task5" "else"

```

![Screenshot](![Screenshot](https://raw.githubusercontent.com/Omarabdalgwad/Todo-list-cli/main/assets/Screenshot%202025-11-25%20151858.png))

---

3- (complete)
Mark a task as completed:

EXAMPLE 1
```bash
todo complete 1

```

![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152504.png)



Example 2

```bash
todo complete 2

```

![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152531.png)


Example 3

```bash
todo complete 3

```

![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152553.png)


Example 4

```bash
todo complete 4

```
![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152615.png)


Example 5

```bash
todo complete 5

```
![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152658.png)

---

4-(delete) 
Delete a task by its number:
```bash
todo delete 1

```

![Screenshot](https://github.com/Omarabdalgwad/Todo-list-cli/blob/main/assets/Screenshot%202025-11-25%20152720.png)









