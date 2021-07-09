# web solution

import os
program = "python3"
arguments = ["e018_os_child_process.py"]
print("Parent process")
print(os.execvp(program, (program,) + tuple(arguments)))
print("Goodbye")
