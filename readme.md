Command Line Application - Todo List

A commandline application using Python 3.6+ that allows you to build and maintain a TODO list.

```shell
	$ Create a task : todo.py create "task details"
	$ Create multiple tasks : todo.py create "task1" "task2"
	$ Read all tasks : todo.py list-all
	$ Read a specific task : todo.py list-all --substring "task description"
	$ Read all tasks which are not complete : todo.py list-all --no-complete ""
	$ Read all tasks which are complete : todo.py list-all --complete ""
	$ Read a task which is not complete : todo.py list-all --no-complete "task description"
	$ Read a task which is complete : todo.py list-all --complete "task description"
	$ Update a task description : todo.py toggle "Task description" "Updated description"
	$ Update a task state : todo.py update "task description"
	$ Delete a task : todo.py delete "task description"
	$ Delete multiple tasks : todo.py delete "task1" "task2"
	$ Delete all tasks : todo.py delete



## Documentation

 * [User guide](https://github.com/sayansatpati/Todo-list/blob/main/Help.txt

### Contributing

Submit issues for bug reports or enhancement ideas.