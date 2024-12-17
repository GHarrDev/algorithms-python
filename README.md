# Algorithms in Python
[![Python](https://img.shields.io/badge/Python-black?logo=python)]()
#### This repository defines implementations of the following algorithms:<br>
Binary Search<br>
Bubble Sort<br>
Quick Sort<br>
Insertion Sort<br>
Merge Sort<br>
Shell Sort<br>
Selection Sort<br><br>

#### `time_it` Decorator

The `time_it` decorator, located in the `utils.py` file, allows you to easily measure the runtime of your algorithms for performance benchmarking. 

To use the `time_it` decorator import it from the `utils.py` file into your script (ensure the correct relevant file path):

   ```python
   from utils import time_it  # Ensure the correct relative or absolute path to utils.py
  ```

Decorate your function with `@time_it` before its definition:

```python
@time_it
def my_algorithm():
    # Your algorithm implementation
    ...
```
