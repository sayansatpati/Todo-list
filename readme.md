Problem¤
Create a commandline application using Python 3.6+ that allows you to build and maintain a TODO list. Your code should be well documented with a docstrings, comments and a README describing how your program works, unit tests to ensure it works as expected, type annotations to allow other developers to understand how to help build upon your program and finally well formatted code (using Black).

You should add a summary to your README that includes the next steps (dot points) and also the strengths and weaknesses of your program in its current state. A list of operations that your should support, as well as how we expect them to be called can be found in the table below.

A TODO item should have at least a description, id and completion state

Operation	Usage	Required
Create a todo	python todo_list.py create "Take the washing out"	TRUE
Create multiple todos	python todo.py create "Take the washing out" "Walk the dog"	TRUE
Read (list) all todos	python todo.py list-all	TRUE
Read (list) all todos that contain a given substring	python todo.py list-all --substring "dog"	TRUE
Read (list) all todos that are complete	python todo.py list-all --complete "dog"	TRUE
Read (list) all todos that are not complete	python todo.py list --no-complete "dog"	TRUE
Update a todo description	python todo.py toggle "f7f6d502-dc35-40d2-b348-287a714b6978"	TRUE
Update the state of a todo	python todo.py update "f7f6d502-dc35-40d2-b348-287a714b6978" "Walk all the dogs"	TRUE
Delete a todo	python todo.py delete "f7f6d502-dc35-40d2-b348-287a714b6978"	TRUE
Delete multiple todos	python todo.py delete "f7f6d502-dc35-40d2-b348-287a714b6978" "2be6199a-abec-42c8-8744-255cbb152d9c"	TRUE
Delete all todos	python todo.py delete-all	TRUE