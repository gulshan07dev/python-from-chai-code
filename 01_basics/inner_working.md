# Understanding Python's Internal Workings

Python, as an interpreted, high-level programming language, is known for its simplicity and readability. The standard implementation of Python is called “cpython”. It is the default and widely used implementation of Python. When you write Python code and execute it, several steps occur behind the scenes to translate your code into instructions that the computer can understand and execute.

## Step 1: Compilation to Bytecode

The Python code undergoes compilation into bytecode (.pyc), which is a low-level representation of the code that is platform-independent. This bytecode is mostly hidden from the user and and this byte code can’t be understood by the CPU. So we need an interpreter called the Python virtual machine (PVM) to execute the byte codes. Compiling Python code into bytecode allows for faster execution.

- **Bytecode Advantages**:
  - Platform-independent.
  - Runs faster.
  - Facilitates the creation of frozen binaries (`*.pyc` files) for distribution.

### `__pycache__` Folder

When Python compiles a module (a Python source file), it generates bytecode and stores it in a special folder called `__pycache__`. This folder is created to cache the compiled bytecode, which helps improve the performance of subsequent executions of the same module. The `__pycache__` folder serves as a cache for bytecode, enhancing performance by avoiding unnecessary recompilation.

- **Naming Convention**:
  - Bytecode files in the `__pycache__` folder are version-specific and include information about the Python version used (`filename.cpython-<version>.pyc`).
  - Helps maintain compatibility between bytecode and the Python interpreter.

- **Usage**:
  - Applicable only for imported modules, not for top-level files.
  - Ensures efficient caching and reuse of compiled bytecode.

## Step 2: Execution

After compilation into bytecode, the Python interpreter (PVM) reads the bytecode instructions one by one and executes them. This execution process results in producing the desired output from the Python code.

### Python Virtual Machine (PVM)

- The Python interpreter, also known as the Python Virtual Machine (PVM), acts as a runtime engine responsible for executing bytecode instructions.
- It interprets the bytecode and executes the corresponding operations, ensuring the correct behavior of the Python code.
- Additionally, for top-level Python scripts (i.e., scripts executed directly), the PVM can directly interpret and execute the Python code without generating bytecode files. This allows for seamless execution of Python scripts without the need for intermediate bytecode files.

## Important Notes

- Bytecode is not machine code; it is specific to Python's interpretation.

- ### implementation of python
  - CPython: standard implementation
  - Jpython / Jython
  - PyPy
  - RubyPython
  - IronPython
  - StacklessPython
  - Pythonxy
  - AnacondaPython

--- 

## explore more: 
video: https://www.youtube.com/watch?v=3HTKc-ZgZbg&list=PLu71SKxNbfoBsMugTFALhdLlZ5VOqCg2s&index=4

blog: https://medium.com/@kaushik.k/internal-working-of-python-415572929e7a